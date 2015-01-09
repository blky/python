
# here is how to add thirdparty library in python
# sudo easy_install httplib2
# import httplib2

import urllib
import webbrowser  

url = "http://www.163.com"
# open web page like reading a file
content = urllib.urlopen(url).read()
# print content 
open('163.html','w').write(content)

webbrowser.get('firefox').open_new_tab(url)
 
 # webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("http://google.com")
# open local cached html file
webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("163.html")

print '---- the end ------'