# Automate blocking Device access and specific apps in Microsoft Family 
## Background
Due to COVID-19, kids had to have their school online.  Online school meant kids having their own computing device that has continous internet / computer access.  With online access, parents had the need to regulate access to content on internet.  When you have a windows PC, you can make use of the Microsoft Family Safety website to do this.  Microsoft provides you features to Switch on / off and provide quotas or specify a time window for access.  Even though this is quite good; often kids don't stick to a speicific schedule or quota.  This creates the need to provide flexibble access to content and need to switch this access on / off on a regular basis.  

If you want to frequently make such manual access changes to the apps / content - Microsoft Family safety website is quite cumbersome.  The site lacks features like creation of groups / profiles or mass data changes.  All you get is a falt list of apps, and you have to block them one by one.  

Here is a Pytest that contains Selenium script that can automate this job for you.  You can target a specific family member and bunch of appliation that need to be blocked.  I personally use this script to block access to content from time to time.  

The same script can be also modified to create a script to unblock the required apps.  But, I have never had the need to do this - as kids themselves do this; what they don't do themselves is blocking the access back again.  And, this job falls on the parents.

## Pre-requisites
- Python 3 
  - Check if your PC has python 3 by entering command "python3 --version" 
  - if you do not have it already, download and install it from https://www.python.org/downloads/
- pytest
  - Check if your PC has pytest by entering command "pytest --version"
  - if you do not have it already, install it using instructions here: https://docs.pytest.org/en/6.2.x/getting-started.html
- Selenium
  - if you do not have it already, install selenium web driver and chrome driver using instructions here: https://pypi.org/project/selenium/

## Preparation
- Download the file blockcontent.py
- Modify Line 26: replace "user@live.com" with your own Microsoft Family account user id
- Delete Line 27: if you modify line 26, you don't need line 27.  You need this only if you want to provide user details at run time.
- Modify Line 38, 39: replace "Family member name" with your family member name as it appears in MS Family Safety website
- Modify Line 89, 90: replace the "discord" and "whatsapp" with the content name that you need to block.  Repeat the lines (copy and modify) as many apps you need to block

*Note*: The script assumes that you have configured 2nd factor authentication; and will wait for manual user input.  If you have not configured this, Delete line 31.
