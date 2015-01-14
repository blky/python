import mylib.mymodule as mytest
import urllib
import re

upword =  mytest.hello('test')
print upword

uf = urllib.urlopen("http://www.google.com")
text = uf.read()
# print text
found = str(text).find('png')
print found
matches = re.findall('/images/[\/\w]+.png',text)

# matches = re.findall('/images/[\S/(\w)]+.png',text)
print matches

for f in matches:
	filename = 'http://www.google.com' + f
	print filename

	urllib.urlretrieve(filename, filename.split('/')[-1])