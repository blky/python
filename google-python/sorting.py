# key function , shadow list for sorting
# customer sorting

a = ['aaaaa','bb','ccc','dc']
b= sorted (a,key=len)
print b
def last(s):
	return s[-1]

a.append('aaaz')
print a
c=sorted(a,key=last)

d=':'.join(a)
print d

e = d.split(':')
print e

f=range(20)
print f

g=range(1,20,3)
print g

# for sorting on two function, return a tuple then sorteda = ['aaaaa','bb','ccc','dc']

a = ['aa','cbb','cccc','dc','aaad']

def firstthenlen(s):
	tup = (s[0],len(s))
	return tup

atwosort=sorted(a,key=firstthenlen)
print atwosort









