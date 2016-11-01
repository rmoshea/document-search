## Cerberus

- current version is v0.2.8
- source code written in python version 2.7.10

<br>
## Instructions for running program
The best and easiest way to download and interact with all cerberus files is to fork and clone this repo


#### [Option 1] Run the program in Terminal
This is the recommended option for Mac users that have cloned all files locally

1. In Finder navigate to the cerberus_0_2_8 unix executable file

  ```bash
  document-search / sourceCode / pythonApp / dist / cerberus_0_2_8 / cerberus_0_2_8
  ```
2. Control-click on the cerberus_0_2_8 executable and select open with Terminal


#### [Option 2] Run the program through python via command line
This option has been tested and will work for both Mac and Windows operating systems with Python installed

1. If you decided not to fork and clone this repo you will need to save the cerberus_0_2_8.py file locally
  - File is located directly in the sourceCode folder
  - Windows users should save this file directly in their Python folder
2. Via command line, install the **requests** python module
  ```bash
  #Mac
  $ sudo pip install requests

  #Windows
  > Scripts\easy_install.exe requests
  ```
3. From the command line, navigate to where the cerberus_0_2_8.py file is stored and execute the following commands to run the program
  ```bash
  #Mac
  $ python cerberus_0_2_8.py

  #Windows
  C:\Python27> python cerberus_0_2_8.py
  ```


#### [Option 3] Run the program as a standalone app
**WARNING:** This option is only compatible for those running on a Mac OS and is **not a recommended** at this time as it is still going through testing cycles.

1. Clone this repo
2. In Finder navigate to the **dist** directory where the bundled standalone application is stored

  ```bash
  / document-search / sourceCode / pythonApp / dist
  ```
3. Double-click on the cerberus_0_2_8.app program to open
