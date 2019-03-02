Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> name = 'Dracula'
>>> age = 4000
>>> if name == 'Alice':
	print('Hi, Alice.')
elif age < 12:
	print('You are not Alice, kiddo.')
elif age > 2000:
	print('Unlike you, Alice is not undead, immortal vampire.')
elif age > 100:
	print('You are not Alice, grannie.') 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> name = 'Dracula'
>>> age = 4000
>>> 
=============================== RESTART: Shell ===============================
>>> 
=============================== RESTART: Shell ===============================
>>> name = 'Bob'
>>> age = 30
>>> if name == 'Alice':
	print('Hi, Alice.')
elif age < 12:
	print('You are not Alice, kiddo.')
else:
	print('You are neither Alice not a little kid.')
	
