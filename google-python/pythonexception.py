
import sys

def hello(filename):
	try:

		f = open(filename,'rU')
	except:
		print '================'
		print sys.exc_info()[1]
 		print '================'
		sys.exit(0)
	else:
		text = f.read()
		print '=====', filename
		print text
		f.close()

def main():
	if  not sys.argv: exit(0)
	for arg in sys.argv[1:]:
		hello(arg)

if __name__ == '__main__':
	main()