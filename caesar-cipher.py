def caesar_encrypt(text):
    """
    凯撒密码加密函数：将每个字符的 ASCII 码 +3
    :param text: 原始明文字符串
    :return: 加密后的字符串
    """
    encrypted_result = ""
    for char in text:
        # 获取字符的ASCII码，加3后转回字符
        ascii_code = ord(char)
        new_ascii = ascii_code + 3
        encrypted_result += chr(new_ascii)
    return encrypted_result

def caesar_decrypt(text):
    """
    凯撒密码解密函数：将每个字符的 ASCII 码 -3
    :param text: 加密后的字符串
    :return: 解密后的原始字符串
    """
    decrypted_result = ""
    for char in text:
        # 获取字符的ASCII码，减3后转回字符
        ascii_code = ord(char)
        new_ascii = ascii_code - 3
        decrypted_result += chr(new_ascii)
    return decrypted_result

# 测试代码
if __name__ == "__main__":
    # 原始测试文本
    original_text = "hello,world"
    print(f"原始文本：{original_text}")
    
    # 加密
    encrypted_text = caesar_encrypt(original_text)
    print(f"加密后（ASCII+3）：{encrypted_text}")
    
    # 解密
    decrypted_text = caesar_decrypt(encrypted_text)
    print(f"解密后（ASCII-3）：{decrypted_text}")