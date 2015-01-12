import sys


def main():
	if len(sys.argv) == 1 or len(sys.argv) > 2:
		print 'Usage is ', __file__,'--filename [filename]'
		print 'Usage is ', __file__,'--operation [operation right]'
	if len(sys.argv) > 1 :
	 	if sys.argv[1] == '--filename':
	 		print 'filename is ',sys.argv[2]

	 	if sys.argv[1] == '--operation':
	 		print 'operation right is ', sys.argv[2]

if __name__ == '__main__':
	main()
