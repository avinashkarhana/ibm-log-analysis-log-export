import requests
import json
import sys
from datetime import datetime
from pytz import timezone, utc
import os
from time import sleep

apps = []
hosts = []
service_id = ""
from_timestamp = 0
to_timestamp = 0
ibm_log_analysis_region = "us-east"
api_path = "/v2/export"
# Construct the endpoint
endpoint = f"https://api.{ibm_log_analysis_region}.logging.cloud.ibm.com"

# import config file
from config import *

def timestamp_str_to_est(epoch_timestamp):
    '''Converts a timestamp string to EST time'''
    epoch_timestamp = int(epoch_timestamp)
    if len(str(epoch_timestamp)) == 13:
        # Millisecond timestamp (e.g., 1609459200000)
        epoch_timestamp = epoch_timestamp / 1000

    utc_datetime = datetime.utcfromtimestamp(epoch_timestamp)
    utc_datetime = utc_datetime.replace(tzinfo=utc)
    toronto_timezone = timezone('US/Eastern')
    toronto_datetime = utc_datetime.astimezone(toronto_timezone)
    toronto_datetime_str = toronto_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')
    return toronto_datetime_str

try:
    # Construct the full API URL
    api_url = f"{endpoint}{api_path}"

    # Initialize pagination_id to None
    pagination_id = None

    if len(hosts) == 0:
        hosts.append(None)
    if len(apps) == 0:
        apps.append(None)

    log_item_dict = {}

    for host in hosts:
        for app_name in apps:
            os.makedirs("Logs", exist_ok=True)
            logs_folder_name = "Logs/Logs_from_timestamp_" + str(from_timestamp) + "_to_timestamp_" + str(to_timestamp)
            file_name_prefix = "All_source"
            
            if host:
                if file_name_prefix == "All_source":
                    file_name_prefix = ""
                file_name_prefix = host
            if app_name:
                file_name_prefix += "_" + app_name

            log_file_name = f"{file_name_prefix}-log.txt"
            log_file_path = f"{logs_folder_name}/{log_file_name}"
            print("> Starting Log Backup in " + log_file_path)
            os.makedirs(logs_folder_name, exist_ok=True)
            with open(log_file_path, 'w') as log_file:
                pass
            
            log_item_dict[log_file_name] = "(BLANK)"

            while True:
                # Make the API request with parameters
                params = {'to': to_timestamp, 'from': from_timestamp}
                if host and len(host) > 0:
                    params['hosts'] = host
                if app_name and len(app_name) > 0:
                    params['apps'] = app_name
                if pagination_id:
                    params['pagination_id'] = pagination_id

                response = requests.get(api_url, params=params, auth=(service_id, ''))

                # Check if the request was successful (status code 200)
                if response.status_code >= 200 and response.status_code < 300:
                    # Parse the JSON response
                    data = json.loads(response.text)

                    # Extract the "_line" property from the JSON data
                    line_data = data.get('lines', [])
                    if line_data:
                        line_values = []
                        for item in line_data:
                            line = ""
                            timestamp = item.get('_ts')
                            # timestamp to EST
                            estDateTimeString = timestamp_str_to_est(timestamp)
                            line += estDateTimeString + " "
                            if item.get("_host"):
                                line += f' {str(item.get("_host"))}'
                            if item.get("_ip"):
                                line += f' {str(item.get("_ip"))}'
                            if item.get("pod"):
                                line += f' {str(item.get("pod"))}'
                            if item.get("_app"):
                                line += f' {str(item.get("_app"))}'
                            if item.get("_line"):
                                if item.get("_logtype") == "json": 
                                    try:
                                        line += f' ${json.loads(item.get("_line")).get("message")}'
                                    except:
                                        line += f' ${item.get("_line")}'
                                else:
                                    line += f' {item.get("_line")}'
                            line_values.append(line)
                            
                        # Append the "_line" data to the dynamic log file
                        with open(log_file_path, 'a') as log_file:
                            for item in line_values:
                                if len(item) > 1:
                                    log_item_dict[log_file_name] = ""
                                item = item.replace("\/", "/")
                                log_file.write(item + '\n')

                    # Get the pagination_id from the response
                    pagination_id = data.get('pagination_id')

                    # If there's no more pagination_id, exit the loop
                    if not pagination_id:
                        # open(log_file_path, 'a') as log_file and reverse the file
                        lines = []
                        with open(log_file_path, 'r') as log_file:
                            lines = log_file.readlines()
                        
                        lines.reverse()
                        with open(log_file_path, 'w') as log_file:
                            log_file.writelines(lines)
                        
                        break

                else:
                    raise ValueError("Failed to fetch data from the API.\nStatus code: "+ str(response.status_code) + "\nResponse: " + str(response.text))
                    break
            print("# Done taking Log Backup in " + log_file_path)
            sleep(1)
    
    # Convert timestamps to datetime objects
    from_datetime_srt_est = timestamp_str_to_est(from_timestamp)
    to_datetime_srt_est = timestamp_str_to_est(to_timestamp)
    
    # Create the readme.txt with formatted variables
    readmeTxt = "Logs from following:\n"

    for item in log_item_dict:
        readmeTxt += f"    - {str(item)} {str(log_item_dict[item])}\n"

    readmeTxt += f"""
These logs are from the following time frame:
    - From unix timestamp: {from_timestamp} ({from_datetime_srt_est})
    - To unix timestamp: {to_timestamp} ({to_datetime_srt_est})
    """
    print("Writing Readme.txt")
    with open(f"{logs_folder_name}/README.txt", 'w') as log_file:
        log_file.write(readmeTxt)
        

except Exception as e:
    print(f"An error occurred: {str(e)}")
    sys.exit(2)
