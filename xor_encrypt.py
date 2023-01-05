#!/usr/env/python3

# XOR Cipher - encryption/decryption
# Example script

import sys
import time


# create Usage function, if something wrong with type/length or else of cli args
def usage:
    print(f"Usage: ./{sys.argv[0]} {sys.argv[1]} {sys.argv[2]}")
    sys.exit(1)


def main():
    # check commandline args
    if len(sys.argv) != 3:
        usage()

    # assign commandline arguments
    plaintext = sys.argv[1]
    ciphertext = ''
    key = sys.argv[2]

    # fix key to exact length of cipher
    nchars_plain = len(plaintext)
    key = key[:nchars_plain]

    print(f"************ XOR ENCRYPTION - START ************\n")
    print(f"The plaintext is: '{plaintext}'")
    time.sleep(2)
    print(f"The key is: '{key}'\n")
    time.sleep(2)
    print(f"Now encrypting with 'XOR Cypher':\n", f"*** {plaintext} *** with key {key} ***\n")
    time.sleep(2)

    for p, k in zip(plaintext, key):
        c = ord(p) ^ ord(k)
        ciphertext += chr(c)

    print(f"RESULT: *** {ciphertext} ***")
    answer = input("\nWould you like to reverse the encryption process? (y/n): ")

    if str(answer.lower()) == 'y':
        decoded = ''
        for c, k in zip(ciphertext, key):
            decoded += chr(ord(c) ^ ord(k))
    else:
        sys.exit(0)

    print(
        f"Result:\n", f"*** ciphertext '{ciphertext}' was decrypted with key '{key}',\n"
                      f"resulting in the decoded text:\n"
                      f"*** '{decoded}' ***")
    print(f"\n********* XOR ENCRYPTION/DECRYPTION - END *********\n")

    sys.exit(0)


# If script called regularly, not imported as module: start main() ...
if __name__ == '__main__':
    main()
