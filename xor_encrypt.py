#!/usr/env/python3

# XOR Cipher - encryption/decryption
# Example script

import sys
import time
import os

# create Usage function, if something wrong with type/length or else of cli args
def usage():
    print(f"Usage: ./{sys.argv[0]} <plaintext> <key>")
    sys.exit(1)

def main():
    # check commandline args
    if len(sys.argv) != 3:
        usage()

    # assign commandline args
    plaintext = sys.argv[1]
    ciphertext = ''
    input_key = sys.argv[2]

    # adjust keylen to match plaintext
    if len(plaintext) > len(input_key):
        key = input_key[:len(plaintext)]
    elif len(plaintext) < len(input_key):
        key = input_key[:len(plaintext)]
    else:
        key = input_key

    print(f"""
    ********** XOR DECRYPTION - START **********
    plaintext: '{plaintext}'""")
    time.sleep(2)
    print(f"encrypt key: '{key}'")
    time.sleep(2)
    print(f"Now encrypting with 'XOR Cypher'...",
          f"plaintext:   '{plaintext}'",
          f"encrypt key: '{key}'")
    time.sleep(2)

    # encrypt plaintext with key
    for p, k in zip(plaintext, key):
        c = ord(p) ^ ord(k)
    ciphertext += chr(c)

    print(f"ciphertext: '{ciphertext}'\n",
          f"*********** XOR DECRYPTION - END ***********")
    answer = input("\nWould you like to reverse the encryption process? (y/n): ")

    if str(answer.lower()) == 'n':
        print(f"Exiting program on behalf of user {os.getlogin()}...")
    else:
        decoded = ''
        for c, k in zip(ciphertext, key):
            decoded += chr(ord(c) ^ ord(k))
        print(f"""
            ********** XOR DECRYPTION - START **********
            ciphertext:  '{ciphertext}'
            decrypt key: '{key}'
            plaintext:   '{decoded}'
            *********** XOR DECRYPTION - END ***********
            """)
    sys.exit(0)

# If run as script, not imported as module: start main() procedure
if __name__ == '__main__':
    main()
