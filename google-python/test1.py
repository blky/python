#!/usr/bin/python -tt
import sys

def hello(name):
	name = str(name) + '!'
	print 'hello', name


def main():
  	hello(sys.argv[1])

if __name__ == '__main__':
	main()
