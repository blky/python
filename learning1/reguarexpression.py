import re

def Find (pat, text):
	match = re.search(pat,text)
	if match:
		print match.group()
	else:	
		print 'not found'
	 
Find('x...g','called piiigi')
Find ('ja...g','calkfdajflkg asdfljads g')
Find ('c..\.', 'cal.kfdajflkg asdfljads g')
Find (':\w\w\w', 'cal.kfdajflkg :asdfl jads g')
Find (':\w\w\w', 'cal.kfdajflkg :a9sdfl jads g')
Find (':\w\w\w', 'cal.kfdajflkg :a9#dfl jads g')
Find ('a\d\d', 'cal.kfdajflkg :a909#dfl jads g')
Find ('a\d\s\d\s', 'cal.kfdajflkg :a9 0 9#dfl jads g')
Find('\d\d\d','1 2 3 ')
Find('\d\s\d\s\d\s','1 2 3 ')
Find('\d\s\d\s\d\s','1      2   3 ')
Find('\d\s+\d+\s+\d\s','1      22   3 ')
# w is for word.. including number and alph, but speical character does not include
Find(':\w+','balkdjf lkasdjf :ak55lsfj$kl ldkasfj;bl ')
# upper s is used for anhthing till space. 
Find(':\S+','balkdjf lkasdjf :ak55lsfj$kl ldkasfj;bl ')

Find('\w+@\w+','dsf dfsfads dsfbl@gmail.com  adsfasdf a%')
Find('\w+@\S+','dsf dfsfads dsfbl@gmail.com  adsfasdf a%')
Find('[\w.]+@[\w.]+','dsf dfsfads nikc.dsfbl@gmail.com  adsfasdf a%')
Find('[\w.]+@\S+','dsf dfsfads .nikc.dsfbl@gmail.com  adsfasdf a%')
Find('[\w][\w.]*@\S+','dsf dfsfads .nikc.dsfbl@gmail.com  adsfasdf a%')
Find('[\w][\w.]+@\S+','dsf dfsfads .nikc.dsfbl@gmail.com  adsfasdf a%')

m=re.search('([\w][\w.]+)@(\S+)','dsf dfsfads .nikc.dsfbl@gmail.com  adsfasdf a%')
print m.group()

print m.group(1)
print m.group(2)

m=re.findall('([\w][\w.]+)@(\S+)','dsf  .nikc.dsfbl@gmail.com  ad  a% a.com pzheng@gmail.com dklsfj ')
# return matched tuple 
print m
m=re.findall('([\w][\w.]+)@\S+','dsf  .nikc.dsfbl@gmail.com  ad  a% a.com pzheng@gmail.com dklsfj ')
# return matched tuple 
print m
# print m.group(1)
# print m.group(2)

# add third parameters at the end of re.findall
m=re.findall('(N[\w][\w.]+)@\S+','dsf  .nikc.dsfbl@gmail.com  ad  a% a.com pzheng@gmail.com dklsfj ',re.IGNORECASE)
print m




print '----------the end ------------'