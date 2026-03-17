def caesar_encrypt(text):
    """
    凯撒密码加密函数：将每个字符的 ASCII 码 +3
    """
    result = ""
    for char in text:
        ascii_code = ord(char)
        new_ascii = ascii_code + 3
        result += chr(new_ascii)
    return result

def caesar_decrypt(text):
    """
    凯撒密码解密函数：将每个字符的 ASCII 码 -3
    """
    result = ""
    for char in text:
        ascii_code = ord(char)
        new_ascii = ascii_code - 3
        result += chr(new_ascii)
    return result

# 交互式主程序
if __name__ == "__main__":
    mode = input("请输入加密还是解密：")
    
    content = input("输入内容：")
    
    if mode == "加密":
        final = caesar_encrypt(content)
        print("加密结果：", final)
    elif mode == "解密":
        final = caesar_decrypt(content)
        print("解密结果：", final)
    else:
        print("输入错误！请输入：加密 或 解密")