import base64
from encoding import special_characters


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
