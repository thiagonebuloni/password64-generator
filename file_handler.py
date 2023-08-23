import sys
from unidecode import unidecode
from encoding import str_or_list, encode64, insert_special_characters, change_equal_sign
from decoding import remove_special_characters, decode64


def file_encode(input_file: str):
    """encode words from file"""
    new_lines: list[str] = []
    try:
        with open(input_file, "r") as file:
            for line in file:
                stripped: str = str_or_list(line)
                encoded: bytes = encode64(unidecode(stripped))
                with_special_characters: str = insert_special_characters(encoded)
                new_password: str = change_equal_sign(with_special_characters)
                new_lines.append(new_password)
    except FileNotFoundError:
        print("File not found")
        sys.exit(2)

    output_file = "encoded-" + input_file
    with open(output_file, "w") as file:
        for line in new_lines:
            file.write(line + "\n")


def file_decode(input_file: str):
    """decode words from file"""
    new_lines: list[str] = []
    try:
        with open(input_file, "r") as file:
            for line in file:
                string_without_special_characters = remove_special_characters(line)
                decoded = decode64(string_without_special_characters)
                new_lines.append(decoded)
    except FileNotFoundError:
        print("File not found")
        sys.exit(2)

    if "encoded-" in input_file:
        print("encode in file name")
        input_file = input_file.replace("encoded-", "")
        print(input_file)
    output_file = "decoded-" + input_file
    print(output_file)

    with open(output_file, "w") as file:
        for line in new_lines:
            file.write(line + "\n")
