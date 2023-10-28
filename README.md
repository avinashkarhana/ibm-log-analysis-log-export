# IBM Log Analysis Log Export Tool

This project contains two tools to export logs from IBM Log Analysis.

1. [IBMLogAnalysisExportLogs.py](https://github.com/avinashkarhana/ibm-log-analysis-log-export/tree/main/python-based) - A Python-based Log Export Tool for IBM Log Analysis.

2. [IBMLogAnalysisExportLogs.user.js](https://github.com/avinashkarhana/ibm-log-analysis-log-export/tree/main/js-userscript) - A JavaScript-based Browser embedded Log Export Tool for IBM Log Analysis.

## Recommendation

Both tools have their own pros and cons, and it is recommended to use the tool which suits your needs.

> > Both the tools supports exporting logs in multiple formats Plain-Text, JSON, CSV, and EXCEL(XLSX).

### Python based tool

- It is more reliable than the JavaScript based tool as it do not rely on UI for configuration.

- But it requires Python to be installed on the machine, and it relies on the Service_ID/Key and configurations to be stored in the `config.py` file. Hence, changing the configuration requires manually editing the `config.py` file every time you need new logs

> Verdict: Recommended for advanced users, or if JavaScript based tool does not work for you

### JavaScript based tool

- It is more easy to use as it is embedded in the browser and can be used just as an extension to the IBM Log Analysis UI.

- This tools also do not require any manual editing of files.

- This tool does not store any sensitive information on disk, and asks for Service_ID/Key on every reload of the page.

- Log Export works with a single button click, after selecting appropriate options/filters/time-frame, as usual on UI.

- Easy to install (Few clicks install) and use.

- But it is less reliable than the Python based tool as it relies on the UI elements of IBM Log Analysis (Which might change in future).

- This tool also requires the user to install a browser extension (TamperMonkey) to work.

> Verdict: Recommended for most users due to ease of use and no manual editing of files, and almost no pre-setup required apart from tamper-monkey extension.

### Wanna help me to work more on Open-Source Projects like this?
<a href="https://www.buymeacoffee.com/avinashkarhana" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a> so that I can get one more sleepless night to work on this kind of stuff.

Or use other sponsoring methods if you like.
