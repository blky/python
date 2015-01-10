# first line in this doc
forLine = 'www.google.com'
count = 0
for i in forLine:
	count +=1
	print format(count,'2d'), i
else:
	print('out of for loop')


# () is used for tuple , which is read-only - unlike list .. iwth []

tup = (1,2,3,4,5,6)
for ea in tup:
	print ea

# file can be thought as string.. therefore, for in to go through all lines in file
print 'read docment first line here .......'

# line = open('forloop.py','r').readline()
# print line

lines = open('forloop.py','r').readlines() 

i=0

for c in  lines:
	print i, ')' ,c 

	i +=1
else:
	print 'out readline', len(lines)



