# IBM Log Analysis Log Export
A Python based Log Export Tool for IBM Log Analysis.

This tool uses IBM Log Analysis API to export logs.

This tool tries to get logs in a format as close to as they are shown in IBM Log Analysis UI

# Usage
First make required changes in the `config.py` file.

    # In config.py file

    # Use this to set your IBM Log Analysis Instance Region
    ibm_log_analysis_region = "us-east"

    # Use this list to specify the Apps for which you want Logs to be Exported (Empty means all apps)
    apps = []

    # Use this list to specify the Sources/Hosts for which you want Logs to be Exported (Empty means all Sources/Hosts)
    hosts = []

    # Update this with your instance's Service Key (API) for the IBM Log Analysis Instance
    service_id = ""

    # Update this this to specify time Frame for which you want to Export Logs. Note: This is in Numeric Unix Timestamp - NUMERIC
    from_timestamp = 1697288400
    to_timestamp = 1697293800


    ############### Usually below data should not be changed  ###############

    # API path
    api_path = "/v2/export"

    # Construct the IBM Log Analysis API endpoint
    endpoint = f"https://api.{ibm_log_analysis_region}.logging.cloud.ibm.com"

Then run the `LogDNAExportLogs.py` script

Example:

    python3 LogDNAExportLogs.py


This will generate a folder in current path with all logs requested.


# Contribution Guide
- Make sure you are not committing code with any sensitive information like service_id.
- Make sure your config.py has variables with preferably empty, or if not possible generic value.