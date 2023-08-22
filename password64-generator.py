#! /usr/bin/python3.10.12

""" Generates a base64 string with special characters based on a given string """

import base64
from unidecode import unidecode

special_characters = [
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    58,
    59,
    63,
    61,
    64,
    92,
    94,
    95,
    96,
    126,
    199,  # Ç
    231,  # ç
]


def encoding(input_string: str) -> str:
    encoded: bytes = encode64(unidecode(input_string))
    new_password: str = insert_special_characters(encoded)
    return new_password


def encode64(input_string: str) -> bytes:
    """encode to base64"""
    encoded = base64.b64encode(input_string.encode("ascii"))
    return encoded


def insert_special_characters(encoded: bytes) -> str:
    """insert special characters into password"""
    EVERY_X_LETTERS: int = 4
    LENGTH_ENCODED: int = len(encoded)

    new_password: str = ""
    for i in range(LENGTH_ENCODED):
        new_password += str(chr(encoded[i]))
        if i % EVERY_X_LETTERS == 0 and i != 0:
            new_password += chr(special_characters[LENGTH_ENCODED + i])

    return new_password


def decoding(string_with_special_characters: str) -> str:
    string_without_special_characters = remove_special_characters(
        string_with_special_characters
    )
    decoded = decode64(string_without_special_characters)
    return decoded


def remove_special_characters(string_with_special_characters: str) -> str:
    """remove special characters from input string"""
    decoded: str = ""
    for i in range(0, len(string_with_special_characters)):
        if ord(string_with_special_characters[i]) in special_characters:
            continue
        decoded += string_with_special_characters[i]

    return decoded


def decode64(string_without_special_characters: str) -> str:
    """decode from base64"""
    string_without_special_characters += "=="
    decoded = base64.b64decode(string_without_special_characters)
    decoded = str(decoded).replace("'", "")
    decoded = decoded[1:].replace("\\n", "")
    return str(decoded)


def main():
    import sys, getopt

    usage = """
    usage: python3 password64-generator <-d|-e> <word>
    
    example: python3 password64-generator -d password
    output: cGFz@c3dv^cmQK
    
    example: python3 password64-generator -e cGFz@c3dv^cmQK
    output: password

    -e  --encode    encode word
    -d  --decode    decode word

    Generates a base64 string with special characters based on a given string,
    with password generation purposes.
    Input a selected word relative to a service to which you want to generate a
    random password.
    You'll receive a base64 encoded string with special characters.
    The same input, the same output.

    """

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ed", ["encode", "decode"])
    except getopt.error as msg:
        print(msg)
        print(usage)
        sys.exit(2)

    if opts:
        output: str = ""
        for o, a in opts:
            if o == "-e" or o == "--encode":
                output = encoding(args[0])
            if o == "-d" or o == "--decode":
                output = decoding(args[0])

            print(output)
    else:
        print(usage)
        sys.exit(2)

    # if len(args) == 1:
    #     print(usage, "\n")
    #     input_string: str = input("Enter your pass word: ")
    #     print()
    # elif args[1]:
    #     input_string: str = args[1]
    # else:
    #     func(sys.stdin, sys.stdout)


if __name__ == "__main__":
    main()
