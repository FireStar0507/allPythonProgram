"""
提供凯撒密码的加密和解密函数
由 FireStar0507 编写
Provides encryption and decryption functions for Caesar ciphers
Written by FireStar0507
"""


# 定义小写字母、大写字母、数字和符号的列表
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "[", "}", "]", ";", ":", "'", " "] 
# 将额外的符号添加到符号列表中，使用 r 前缀避免转义字符带来的问题
symbol += list(r"\|,./<>?")


# 定义加密函数，接受文本和位移值作为参数
def encrypt(text, values):
    """
    Args:
        text: (string)A string that needs to be encrypted
        values (integer): The value of the string offset when encrypting (cannot be a floating-point number!!! ）
    参数：
        text（字符串）：需要加密的字符串
        values （整数）：加密时字符串位移的值(不能为浮点数！！！）
    """
    newtext = []  # 用于存储加密后的字符
    for t in text:  # 遍历输入文本中的每个字符
        if t in abc:  # 如果字符是小写字母
            index = (abc.index(t) + values) % len(abc)  # 计算加密后的索引
            newtext.append(abc[index])  # 将加密后的字符添加到结果中
        elif t in ABC:  # 如果字符是大写字母
            index = (ABC.index(t) + values) % len(ABC)
            newtext.append(ABC[index]) 
        elif t in symbol:  # 如果字符是符号
            index = (symbol.index(t) + values) % len(symbol)  
            newtext.append(symbol[index]) 
        elif t in num:  # 如果字符是数字
            index = (num.index(t) + values) % len(num)  
            newtext.append(num[index])
        else:  # 处理不在列表中的字符，如其他特殊字符
            newtext.append(t)  # 直接将原字符添加到结果中
    return "".join(map(str, newtext))  # 将字符列表合并为字符串并返回


# 定义解密函数，接受文本和位移值作为参数
def decrypt(text, values):
    """
    Args:
        text:(string) The string that needs to be decrypted
        values (integer): The value of the string offset at the time of decryption (cannot be floating-point!! ）
    参数：
        text（字符串）：需要解密的字符串
        values （整数）：解密时字符串位移的值(不能为浮点数！！！）
    """
    newtext = []  # 用于存储解密后的字符
    for t in text:  # 遍历输入文本中的每个字符
        if t in abc:  # 如果字符是小写字母
            index = (abc.index(t) - values) % len(abc)  
            newtext.append(abc[index]) 
        elif t in ABC: 
            index = (ABC.index(t) - values) % len(ABC) 
            newtext.append(ABC[index])  
        elif t in symbol: 
            index = (symbol.index(t) - values) % len(symbol)  
            newtext.append(symbol[index]) 
        elif t in num: 
            index = (num.index(t) - values) % len(num)  
            newtext.append(num[index]) 
        else:  
            newtext.append(t)  
    return "".join(map(str, newtext))
