#!/usr/bin/python

import crypt, sys, time
def loading():
	clear = "\n" * 100
	print clear
	print ("Working...")
	print "Trying password:"+senha

print "OMG! Linux Passwords Exposer"
print "Created by Basline | LineTech"
print "----------------------------- "
f = open(sys.argv[1], "r")
if f.mode == 'r':
	file = f.read()

#	salt = raw_input("Salt: ")
	hash = raw_input("Hash: ")
	salt = "$"+hash.split('$')[1]+"$"+hash.split('$')[2]
	for senha in file.split('\n'):
		teste = crypt.crypt(senha, salt)
		loading()
		if teste == hash:
			print "Password found:"+senha
			break
else:
	print "The password file coud not be read"
	print "Use: ./passwdOMG.py your_wordlist.txt"
