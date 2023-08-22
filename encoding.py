import base64
from unidecode import unidecode

special_characters = [
    33,
    35,
    36,
    37,
    38,
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
    126,
    199,  # Ç
    231,  # ç
]


def encoding(input_string: str | list[str]) -> str:
    stripped: str = str_or_list(input_string)
    encoded: bytes = encode64(unidecode(stripped))
    with_special_characters: str = insert_special_characters(encoded)
    new_password: str = change_equal_sign(with_special_characters)
    return new_password


def str_or_list(raw_input: str | list[str]) -> str:
    if isinstance(raw_input, list):
        stripped: str = ""
        for word in raw_input:
            stripped += word
        return stripped
    return raw_input


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
            if LENGTH_ENCODED + i >= len(special_characters):
                index: int = LENGTH_ENCODED + i - len(special_characters)
                while index >= len(special_characters):
                    index -= len(special_characters)
            else:
                index: int = LENGTH_ENCODED + i
            new_password += chr(special_characters[index])

    return new_password


def change_equal_sign(with_special_characters: str) -> str:
    while with_special_characters[-1] == "=":
        with_special_characters = with_special_characters[:-1]
    return with_special_characters
