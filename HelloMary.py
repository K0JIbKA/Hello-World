Python 2.7.13 (default, Sep 26 2018, 18:42:22) 
[GCC 6.3.0 20170516] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> name = 'Mary'
>>> password = 'swordfish'
>>> if name = 'Mary':
	
SyntaxError: invalid syntax
>>> name = 'Mary
password = 'swordfish'
if name == 'Mary':
	print('Hello Mary')
	if password == 'swordfish':
		
SyntaxError: EOL while scanning string literal
>>> name = 'Mary'
>>> password = 'swordfish'
>>> if name == 'Mary':
	print('Hello Mary')
	if password == 'swordfish':
		print('Access granted.')
		else:
			
SyntaxError: invalid syntax
>>> name = 'Mary'
>>> password = 'swordfish'
>>> if name == 'Mary':
	print('Hello Mary')
	if password == 'swordfish':
		print('Access granted.')
	else:
		print('Wrong password.') 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
=============================== RESTART: Shell ===============================
>>> name = 'Mary'
>>> password = 'swordfish'
>>> if name == 'Mary':
	print('Hello Mary')
	if password == 'swordfish':
		print('Access granted.')
	else:
		print('Wrong password.')
		
