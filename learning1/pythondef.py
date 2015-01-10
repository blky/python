sdef printEntry():
	print "entery 1"
	print "entery 2"

def printValue(var1, var2):
	print 'var 1 is:',var1,'var 2 is: ', var2
	 
def testReturn (n1, n2):
	n = n1 + n2
	m = n2 * n2
	p = n1 - n2
	e = n1 ** n2

	return n,m,p,e
 
# default avlue for parameter 

def testDefaultValue (n1, n2=6):
	n = n1 + n2
	m = n2 * n2
	p = n1 - n2
	e = n1 ** n2

	return n,m,p,e
 


print '--------entery program :'
printEntry()
printEntry()

printValue(12, 'today')

print 'test sum is : ', testReturn(2,18)

sum1, multi, diff,power = testReturn(12,3)

items = testReturn(5,2)

print sum1, multi, diff,power 

print items,'items[0] is:',items[0]
 

print testDefaultValue(6)
print testDefaultValue(6,2)

print '--------leave program .'

# if else 
ll = raw_input('please enter your sex:')

if ll == 'male' or ll =='boy' or ll == 'man':
	print 'hello, guy'
else:
	print 'hello, gal'

# while loop 
i=0
while i<10 :
	print i,"hello world"
	i +=1
	if i == 9:
		break
else:
	print 'else while'

print 'end of while'







print 'end of program'