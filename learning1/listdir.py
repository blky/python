import sys
import os

def list(dir):
	filenames = os.listdir(dir)
	for fn in filenames:
		print 'path',os.path.join(dir,fn)

	for fn in filenames:
		print 'absolute path',os.path.abspath(dir)

	return filenames

 
def main():
	filelists = list(sys.argv[1]) 
 


 

if __name__ == "__main__":
    main()