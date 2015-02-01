def is_pallindrome_vl(s): 
	""" 
	(str) -> bool
	return true if and only if s is  a palindrome

	>>> is_pallindrome_vl('noon') 
	True
	>>> is_pallindrome_vl('racecar')
	True
	>>> is_pallindrome_vl('dented')
	False	
	""" 
	return reverse(s) == s

def reverse(s):
	"""
	(str) -> str 
	return string in reverse order 

	>>> reverse('hello')
	'olleh'
	>>> reverse('a')
	a
	"""

	rev = ''
	for char in s:
		rev = char  + rev

	return rev
