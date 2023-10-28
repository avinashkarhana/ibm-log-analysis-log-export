# IBM Log Analysis Log Export - JS Userscript

A JS Userscript based Log Export Tool for IBM Log Analysis.

## Note

- This tool uses IBM Log Analysis API to export logs.

- This tool tries to get logs in a format as close as it can to what is shown in the IBM Log Analysis UI.

- Due to security concerns, this tool does not store Service_ID/Key anywhere on disk, therefore on every reload of the page, it will ask for Service_ID/Key at time of backup.

## Prerequisite

 `TamperMonkey Extension`

> Or

 `TamperMonkey Beta Extension`

> > Click [here](https://chrome.google.com/webstore/detail/tampermonkey-beta/gcalenpjmijncebpfijmoaglllgpjagf?hl=en) to install extension for chromium based browsers.

> > Click [here](https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/) to install extension for Firefox.

## Install

Follow the step below:

- Visit this [here](https://raw.githubusercontent.com/avinashkarhana/ibm-log-analysis-log-export/main/js-userscript/IBMLogAnalysisExportLogs.user.js) once Tampermonkey is installed

- Click Install

Done !

## Usage

Once Installed, you can use this tool as follows:
    1. Open IBM Log Analysis UI
    2. Select appropriate options/filters/time-frame as usual on UI
    3. Select desired `Log Format` from `Export Format` dropdown
    4. Click on `Export Logs` button on top bar (This button might take 5secs to appear after page load)

## Note for users

If asked to allow connection to the API endpoint, click `Allow Always` as this tool needs to connect to API to export logs
