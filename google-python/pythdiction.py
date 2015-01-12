import sys

def dictExe():

	a = {}
	a['m'] = 'mary'
	a['z'] = 'zebra'
	a['a'] = 'amy'
	a['b'] = 'betty'

	print a.items()

	for ea in sorted(a.keys()):
		print 'key is :', ea , a[ea]

	for tup in a.items():
		print tup

# reading from a file
def printFunc():
	func_name = sys._getframe().f_code.co_name
	print '=====',func_name


def cat(filename):

	func_name = sys._getframe().f_code.co_name
	print '=====',func_name

	f=open(filename,'rU')
	for line in f:
		print line,

def cat2(filename):

	func_name = sys._getframe().f_code.co_name
	print '=====',func_name

	f = open (filename,'rU')
	lines = f.readlines()
	print lines

def cat3(filename):

 	print '=====',__file__,sys._getframe.f_code.co_name

	f = open (filename,'rU')
	text = f.read()
	print text


def main():
	cat(sys.argv[1])
	cat2(sys.argv[1])
	cat3(sys.argv[1])
if __name__ == '__main__':
	main()


