def encryption(text: str):
    result = ""
    for i in text:
        if ord(i) > 64 and ord(i) < 91:
            result += chr((ord(i) + 2) % 26 + 52)
        if ord(i) > 96 and ord(i) < 123:
            result += chr((ord(i) + 2) % 26 + 78)
    return result

def decryption(text: str):
    result = ""
    for i in text:
        if ord(i) > 64 and ord(i) < 91:
            result += chr((ord(i) - 2) % 26 + 78)
        if ord(i) > 96 and ord(i) < 123:
            result += chr((ord(i) - 2) % 26 + 104)
    return result