def encryption(text: str):
    result = ""
    odd = ""
    for index, i in enumerate(text):
        if i == " ":
            continue
        elif index % 2 == 0:
            result += i
        else:
            odd += i
    return result + odd

def decryption(text: str):
    double = list(text[:len(text) // 2])
    odd = list(text[len(text) // 2:])
    result = ""
    for i in range(len(odd)):
        result += double[i] + odd[i]
    return result