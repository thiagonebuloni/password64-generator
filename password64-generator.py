#! /usr/bin/python3.10.12

""" Generates a base64 string with special characters based on a given string """


from encoding import encoding
from decoding import decoding
from file_handler import file_encode, file_decode


def main():
    import sys, getopt

    usage = """
    usage: python3 password64-generator [-d|-e|-h] ['word'|file]
    
    example: python3 password64-generator -d 'password'
    output: cGFz@c3dv^cmQK
    
    example: python3 password64-generator -e 'cGFz@c3dv^cmQK'
    output: password

    -e  --encode            encode words
    -d  --decode            decode words
        --file-encode       encode words from file
        --file-decode       decode words from file
    -h  --help              print this help message

    Generates a base64 string with special characters based on a given string,
    with password generation purposes.
    Input a selected word relative to a service to which you want to generate a
    random password.
    You'll receive a base64 encoded string with special characters.
    The same input, the same output.

    Use 'single quotes' with words and phrases to avoid misinterpretation from
    the cli, unless inside files.
    """

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "edh",
            ["encode", "decode", "help", "file-encode", "file-decode"],
        )
    except getopt.error as msg:
        print(f"\033[1;31m    {msg}\033[0;0m")
        print(usage)
        sys.exit(2)

    if opts and args:
        output: str = ""
        for o, _ in opts:
            if o == "-e" or o == "--encode":
                output = encoding(args)
            if o == "-d" or o == "--decode":
                output = decoding(args[0])
            if o == "--file-encode":
                file_encode(args[0])
            if o == "--file-decode":
                file_decode(args[0])
            if o == "-h" or o == "--help":
                print(usage)
                sys.exit(0)
            print(output)
            sys.exit(0)

    elif args:  # default
        output = encoding(args)
        print(output)
        sys.exit(0)
    else:
        print(usage)
        sys.exit(2)


if __name__ == "__main__":
    main()
