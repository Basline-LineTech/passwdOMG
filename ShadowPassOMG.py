#!/usr/bin/python

import legacycrypt, sys, time, os
def loading():
	os.system('clear')
	print ('Working...')
	print ('Trying password: '+senha)

os.system('clear')
print ("OMG! Linux Passwords Exposer")
print ("Created by Basline | LineTech")
print ("----------------------------- ")
print ("Salt = First '$' to last '$'")
print ("Hash = Full Hash until ':'")
print ("Hash Location = /etc/shadow")
arg=(len(sys.argv)-1)
if arg>0:
	f = open(sys.argv[1], "r")
	if f.mode == 'r':
		file = f.read()

		#salt = input("Salt: ")
		hash = input("Hash: ")
		salt = "$"+hash.split('$')[1]+"$"+hash.split('$')[2]+"$"+hash.split('$')[3]+"$"
		for senha in file.split('\n'):
			teste = legacycrypt.crypt(senha, salt)
			loading()
			if teste == hash:
				os.system('clear')
				print ("Password found: "+senha)
				break
else:
	print ("The password file coud not be read")
	print ("Use: ./passwdOMG.py your_wordlist.txt")
