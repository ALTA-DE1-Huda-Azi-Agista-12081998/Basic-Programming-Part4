def ubah_huruf(sentence):
    result = ""
    for char in sentence:
        if char.isalpha():
            new_char = chr((ord(char) - ord('A' if char.isupper() else 'a') + 10) % 26 + ord('A' if char.isupper() else 'a'))
            result += new_char
        else:
            result += char
    return result


if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB