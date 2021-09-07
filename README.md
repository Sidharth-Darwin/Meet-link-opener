# Meet-link-opener

## *Introduction*
### This project is for accessing google meet link from whatsapp chats/groups and opening the  links.

### It uses [Selenium module](https://selenium-python.readthedocs.io/),[Webbrowser module](https://www.geeksforgeeks.org/python-launch-a-web-browser-using-webbrowser-module/),[Time module](https://www.programiz.com/python-programming/time) and [Re module](https://docs.python.org/3/library/re.html).
---

## *Brief Summary of the project*
### After specifying person/group chat and using [Selenium module](https://selenium-python.readthedocs.io/) to access whatsapp with driver. 
### It enters the [Whatsapp web page](https://web.whatsapp.com/) and accesses the last few messages. 
### The messages are filtered for [meet links](https://meet.google.com/) using [Regex module](https://www.w3schools.com/python/python_regex.asp).
### All the possible links are stored as a list.
### The last link is accessed and opened using [Webbrowser module](https://www.geeksforgeeks.org/python-launch-a-web-browser-using-webbrowser-module/).
---
