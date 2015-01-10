# string output raw vs. unicode
sr=r'aa\nbb'
print sr
su = u'aa\nbb'
print su

# string formating printout
s="name"
d=20
grade = 85.35

print "this is %s, age is %d, grade is %.2f"%(s,d,grade)

st = "www.google.com"
sub = st[-1::-1]
print sub

st = " kljthl aklsdfj lkfj  "
ststrip=st.strip()
print ststrip
print ststrip.strip('j') 
print ststrip.split(' ')

print ststrip
print ststrip.split('k')

# string and ascii code converstion 
cha = 'a'
print 'a ASII code is ',ord(cha)
cha = 'A'
print 'A ASII code is ',ord(cha)
print 'back to character from ascii value ',chr(65)

a1 = 'firstword'
a2 = 'second word'
a3= '56'
a4 = '5.6'
 
print a1 + a2
# alnum means all alpha and number

print a1.isdigit(), a3.isalnum(), a3.isdigit(),a1.isdigit()
print a3.isdigit(),a4.isdigit(), a1.isalpha(),a4.isalpha(),a3.isalpha()
print a4.isalnum(),a4.isdigit()

a5=''
a6  = '    '
print  a5.isspace(), a6.isspace(), a1.isspace()
print  a1.islower(), a1.isupper(), a6.islower(), a6.islower()
print a1.upper(),a2.upper(), a2.title()


st='www.google.com'
print st.startswith('www')
streplace = st.replace('www','WWW')
print streplace


# using split function to find all words

st='dafsds----dsafds----ads--f--asdf----adsfa-dsf-asdf---asdf--'

st1 = st.strip('-')
print st1
st2 = st1.split('-')
print st2
stFinal = ""
for ea in st2:
	if len(ea) <> 0:
		ea +='-'
		stFinal += ea
stFinal = stFinal.strip('-')
stFinal = stFinal.split('-')

print '===', stFinal,len(stFinal)

 
# using find to find all workds

st5 = st.replace('--','-').replace('--','-')
st6 = st5.strip('-').split('-')
print '===', st6, len(st6)
 
# regular expression
import re





print '-------- the end -----------'
