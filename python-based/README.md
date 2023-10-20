# IBM Log Analysis Log Export - Python Tool

A Python-based Log Export Tool for IBM Log Analysis.

## Note

- This tool uses IBM Log Analysis API to export logs.

- This tool tries to get logs in a format as close as it can to what is shown in the IBM Log Analysis UI.

- This tool relies on the Service_ID/Key and other configuration to be stored in the `config.py` file, therefore it is recommended to keep the `config.py` file secure.

## Usage

Install dependencies from requirements.txt

    pip install -r requirements.txt

Then, make the required changes in the `config.py` file.

    # In config.py file

    # Use this to set your IBM Log Analysis Instance Region
    ibm_log_analysis_region = "us-east"

    # Use this list to specify the Apps for which you want Logs to be Exported (Empty means all apps)
    apps = []

    # Use this list to specify the Sources/Hosts for which you want Logs to be Exported (Empty means all Sources/Hosts)
    hosts = []

    # Update this with your instance's Service Key (API) for the IBM Log Analysis Instance
    service_id = ""

    # Update this to specify the time frame for which you want to Export Logs. Note: This is in Numeric Unix Timestamp - NUMERIC
    from_timestamp = 1697288400
    to_timestamp = 1697293800


    ############### Usually below data should not be changed  ###############

    # API path
    api_path = "/v2/export"

    # Construct the IBM Log Analysis API endpoint
    endpoint = f"https://api.{ibm_log_analysis_region}.logging.cloud.ibm.com"

Then run the `IBMLogAnalysisExportLogs.py` script

Example:

    python3 IBMLogAnalysisExportLogs.py

This will generate a folder in the current path with all logs requested.

## Contribution Guide

- Make sure you are not committing code with any sensitive information like service_id.
- Make sure your config.py has preferably empty variables; if not possible, use a generic value.
