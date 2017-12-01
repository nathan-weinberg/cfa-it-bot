# CFA IT BOT
#### Author: Nathan Weinberg
##### Written in Python 3.6

## Purpose
CFA IT Bot uses Selenium and chromedriver to open and login to web pages used at Boston University's CFA IT site automatically in Google's Chrome web browser.

## Usage
This file should be run from the command line. All existing Chrome instances must be closed before running.

Paths for the Chromedriver executable and User's Chrome options as well as login usernames and passwords must be written in a JSON file, which should be located in the same directory as the Python file unless otherwise specified. Chromedriver can be found here: https://sites.google.com/a/chromium.org/chromedriver/

The program will search for a file named "auth.json" by default. A custom JSON file can be used by specifying the filename as a command line argument.

Off-campus users wishing to connect to certain BU resources will need to be connected to the Boston Univeristy VPN. Information on how to do so can be found here: https://www.bu.edu/tech/services/cccs/remote/vpn/

### Packages
You must install the Selenium package and the jsonschema package. This can be done with

`pip install selenium`

`pip install jsonschema`

or they can be found here:

http://www.seleniumhq.org/

https://pypi.python.org/pypi/jsonschema

## Notes
This project is not officially supported by or associated with Boston University Information Services and Technology or any of its affiliates. Just something some DS student whipped up.
