# IBM Log Analysis Instance Region
ibm_log_analysis_region = "us-east"

# List Apps for which Logs will be Exported (Empty means all apps)
apps = []

# List Sources for which Logs will be Exported (Empty means all sources)
hosts = []

# Service Key (API) for the IBM Log Analysis Instance
service_id = ""

# Log Export time Frame (Unix Timestamp - NUMERIC)
from_timestamp = 1697288400
to_timestamp = 1697293800


############### Usually below data should not be changed  ###############

# API path
api_path = "/v2/export"

# Construct the IBM Log Analysis API endpoint
endpoint = f"https://api.{ibm_log_analysis_region}.logging.cloud.ibm.com"