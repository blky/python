print("hello, world")

# function for str
# python variable specity 
x = 12
y = 16
z = 18
print 'x=',x,'y=',y,'z=',z
print 'address x=',id(x), 'address y=',id(y),'address z=',id(z) 

x = y
print 'x=',x,'y=',y,'z=',z
print 'address x=',id(x), 'address y=',id(y),'address z=',id(z) 
 
z=x

print 'x=',x,'y=',y,'z=',z
print 'address x=',id(x), 'address y=',id(y),'address z=',id(z) 
 


letters = "this Is world hello"
print letters
print str.islower(letters)
print '\n=====system str func======='

# replace function 
letters = letters.replace('l','LLL')
print(letters)
print '\n=====import math======='

# system function ,but need to be import
import math
sin = math.sin(3.14/6)
print sin
 
# constant defined in system 
pi = math.pi 
sin = math.sin(pi/6)
  
print 'sin is ',sin
print 'tang is ', math.tanh(pi/6)
print 'cos is ', math.cos(pi/6)

print '\n======import os======'
import os 
currentDir = os.getcwd()
print 'current dir is ',currentDir
ldir = os.listdir(currentDir)
print 'items at current dir' , ldir

print '\n======import socket======'
import socket
baiduIP = socket.gethostbyname('www.baidu.com')
print 'baidu ip address:' , baiduIP

print '\n=======the end========='




