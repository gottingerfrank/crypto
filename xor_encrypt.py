#!/usr/env/python3

# XOR Cypher - encryption/decryption
# Example script

import sys
import time

plaintext = 'Python Rules!'
cyphertext = ''
key = 'Lorem ipsum d'

print(f"************ XOR ENCRYPTION - START ************\n")
print(f"The plaintext is: 'Python Rules!'")
time.sleep(3)
print(f"The key is: 'Lorem ipsum d'\n")
time.sleep(3)
print(f"Now encrypting plaintext *** {plaintext} *** with key *** {key} *** ...")
time.sleep(3)

for p, k in zip(plaintext, key):
    c = ord(p) ^ ord(k)
    cyphertext += chr(c)

print(f"RESULT: *** {cyphertext} ***")
answer = input("\nWould you like to reverse the encryption process? (y/n): ")

if str(answer.lower()) == 'y':
    decoded = ''
    for c, k in zip(cyphertext, key):
        decoded += chr(ord(c) ^ ord(k))
else:
    sys.exit(0)

print(
    f"Result: cyphertext '*** {cyphertext} ***' was decrypted with key '*** {key} ***', "
    f"resulting in the decoded text:\n"
    f"*** '{decoded}' ***")
print(f"\n********* XOR ENCRYPTION/DECRYPTION - END *********\n")

sys.exit(0)
