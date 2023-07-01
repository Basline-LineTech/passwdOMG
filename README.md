# passwdOMG
Linux Passwords Exposer

This script uses Hashes found on /etc/shadow against an wordlist to try to crack the password.
Since Linux hashes changed a little bit, I updated the script.

I also created a new script called ShadowPassOMG.py
This is the only script that will work on the future, because the library Crypt from the original file will be removed on newer versions of Python
Before you use it, make sure to install the new library: python - m pip install legacycrypt
