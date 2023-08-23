import requests
Z = '\033[1;31m' #احمر
b ='\x1b[38;5;106m'#
p = '\x1b[38;5;85m'#اخضر فاتح
z ='\x1b[38;5;105m'#از
F = '\033[2;32m' #
W="\033[0;37m"#ابيض
Y = '\033[1;34m' #
os.system('cls'if os.name=='net'else'clear')
print (p+'''          
			     | |         | |
			  ___| |__   __ _| |_
			 / __| '_ \ / _` | __|
			| (__| | | | (_| | |_
			 \___|_| |_|\__,_|\__|''')
print('')
while True:
	text=input(W+'you : '+b)
	zz = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text
	print(Z+'he  :',f'{Y}',zz)
