def caesar_encrpt(string,n):
	new_str = ""
	for ch in string:
	    if ord(ch) + n <= ord('Z'):	
	        new_str += chr (ord(ch) + n)
	    elif ord(ch) + n > ord('Z') and (ord(ch) + n < ord('a')):
	        new_str += chr(ord(ch) - 26 + n)
	    elif ord(ch) + n > ord('a') and (ord(ch) + n <= ord('z')):
	        new_str += chr(ord(ch) + n)
	    else:
	        new_str += chr (ord(ch) - 26 + n)
	print new_str
	return new_str

caesar_encrpt("abc",1)