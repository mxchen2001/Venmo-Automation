# Venmo Automation
This repository contains the code developed for Automating of Venmo Transactions. You will need Python versions 3.6+ because the Venmo Api is only compatible with those versions of python

```bash
# Use this to install the latest version of python with the latest version of pip

pip3 install venmo-api --upgrade

# Use the -V flag to check the version of pip, I recommend 20.2+

pip -V
```

## Installation
You can run this project directly from your terminal by cloning this repository and running it through your command line
```bash
# install 

pip install venmo-api
pip install xlrd

# or run

python -m pip install -r requirements.txt
```


## Running the CLI
Set up your Venmo Authentication Token by running:
```bash
python get_access_token.py
```
Then run the **Command Line Interface** by running:
```bash
python venmo_cli.py
```
Your access token will be stored in `access_token.txt`, **MAKE SURE TO RUN:**
```bash
python logout.py
```
Your access token never expires! Running `python logout.py` will revoke your token and delete it off your local machine

## Setting up the Spreadsheet
There are four inputs that you need to setup before running the script. Make sure to follow the guidelines listed below otherwise an **error** might occur.
- Username: Make sure it is the **unique** username that is associated with the target account
- Amount: Make sure that the value is a positive number
- Note: No restrictions
- Type: Either "R" or "r" for **Request** or "S" or "s" for **Send**

## Running the Spreadsheet Parser
Set up your Venmo Authentication Token by running:
```bash
python get_access_token.py
```
Then run the **Spreadsheet Parser** by running:
```bash
python venmo_read_spreadsheet.py
```
Your access token will be stored in `access_token.txt`, **MAKE SURE TO RUN:**
```bash
python logout.py
```
Your access token never expires! Running `python logout.py` will revoke your token and delete it off your local machine

## NPM installs

```bash
npm start
```