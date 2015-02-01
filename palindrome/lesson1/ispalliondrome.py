def is_pallindrome_v1(s): 
	""" 
	(str) -> bool
	return true if and only if s is  a palindrome

	>>> is_pallindrome_v1('noon') 
	True
	>>> is_pallindrome_v1('racecar')
	True
	>>> is_pallindrome_v1('dented')
	False	
	""" 
	return reverse(s) == s


def is_pallindrome_v2(s): 
	""" 
	(str) -> bool
	return true if and only if s is  a palindrome

	>>> is_pallindrome_v2('noon') 
	True
	>>> is_pallindrome_v2('racecar')
	True
	>is_pallindrome_v2('racecar')>> is_pallindrome_vl('dented')
	False	
	""" 
	n = len(s)
	#compare first half of characters with second half of characters
	#ignore middle character if string is odd length
	return s[:n//2] == reverse(s[n-n//2:])


def is_pallindrome_v3(s): 
	""" 
	(str) -> bool
	return true if and only if s is  a palindrome

	>>> is_pallindrome_v3('noon') 
	True
	>>> is_pallindrome_v3('racecar')
	True
 	>>> is_pallindrome_v3('dented')
	False
	"""
	i=0
	j=len(s) -1

	while i < j and s[i] == s[j]:
		i += 1
		j -= 1
	return  i >= j


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

	
