#! /usr/bin/python3.10.12

""" Generates a base64 string with special characters based on a given string """


from encoding import encoding
from decoding import decoding


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
        print(f"\033[1;31m    {msg}\033[0;0m")
        print(usage)
        sys.exit(2)

    if not args:
        print("\033[1;31m\n    Please input <word>\033[0;0m")
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
            sys.exit(0)
    else:
        print(usage)
        sys.exit(2)


if __name__ == "__main__":
    main()
