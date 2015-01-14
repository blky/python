import os.path
import time
import commands
import sys
 
import pprint

# print 'File         :', __file__
# print 'Access time  :', time.ctime(os.path.getatime(__file__))
# print 'Modified time:', time.ctime(os.path.getmtime(__file__))
# print 'Change time  :', time.ctime(os.path.getctime(__file__))
# print 'Size         :', os.path.getsize(__file__)

# for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
#     print 'File        :', file
#     print 'Absolute    :', os.path.isabs(file)
#     print 'Is File?    :', os.path.isfile(file)
#     print 'Is Dir?     :', os.path.isdir(file)
#     print 'Is Link?    :', os.path.islink(file)
#     print 'Mountpoint? :', os.path.ismount(file)
#     print 'Exists?     :', os.path.exists(file)
#     print 'Link Exists?:', os.path.lexists(file)
#     print



# def visit(arg, dirname, names):
#     print dirname, arg
#     for name in names:
#         subname = os.path.join(dirname, name)
#         if os.path.isdir(subname):
#             print '  %s/' % name
#         else:
#             print '  %s' % name
#     print

# os.mkdir('example')
# os.mkdir('example/one')
# f = open('example/one/file.txt', 'wt')
# f.write('contents')
# f.close()
# f = open('example/two.txt', 'wt')
# f.write('contents')
# f.close()
# os.path.walk('example', visit, '(User data)')

def list (dir):
	cmd = 'ls -latr ' + dir   
	print 'command is ',cmd
	# return

	(status,output) = commands.getstatusoutput(cmd)
	# check status for error 
	if status !=0:
		print 'status error',output
		sys.exit(1)
	print '====status====', status
	print '====output====',output

	# try:
	# 	(status,output) = commands.getstatusoutput(cmd)
	# 	print '====status====', status
	# 	print '====output====',output
	# except:
	# 	print 'status error, exit..'
	# 	exit(1)

	# print 'try correct output'


 

def main():
	list(sys.argv[1])

if __name__ == '__main__':
	main()



