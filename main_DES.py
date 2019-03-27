# -*- coding: utf-8 -*-
"""
？？？？？
Created on Tue Mar 26 22:44:12 2019

@author: Administrator
"""

from pyDes import des, CBC, PAD_PKCS5
import binascii
 


def des_encrypt(s,KEY):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    try:
        secret_key = KEY
        iv = secret_key
        k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        en = k.encrypt(s, padmode=PAD_PKCS5)
        return binascii.b2a_hex(en)
    except:
        print("非法的DES密钥长度，密钥必须是8bytes的长度！")
        return 
    
 
 
def des_descrypt(s,KEY):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    try:
        secret_key = KEY
        iv = secret_key
        k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
        print("密钥正确！")
        de=de.decode("utf-8")
        return de
    except:
        print("密钥错误！")
        return 

if __name__ == '__main__':
    # 秘钥
    KEY='mHAxsLYd'
    s="http://baidu.com/"
    s1=des_encrypt(s,KEY)
    KEY='mHAxsLYd'
    s2=des_descrypt(s1,KEY)
    print(s2)
