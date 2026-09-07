import json


def to_dict(raw_data: bytes) -> dict:
    # 1. raw_data: This is your raw bytes literal

    # 2. Convert bytes to a standard string using UTF-8 decoding
    text_data = raw_data.decode("utf-8")

    # 3. Parse the string into a real Python dictionary
    data_dict = json.loads(text_data)

    return data_dict
