# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import qrcode
from pyzbar import pyzbar
import cv2
import re
def pattern(s):
    url = s
    if re.match('^https?:/{2}\w.+\.baidu\.com.*$', url):
        print("是安全网站")
    else:
        print("不是安全网站")
        
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
def main():
    qr =qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )
    #输入网站
    s="https://www.baidu.com/?tn=98010089_dg&ch=7"
    # 设置密钥
    KEY1="mHAxsLYz"
    # 对网站进行加密
    s=des_encrypt(s,KEY1)
    # 生成二维码
    qr.add_data(s)
    qr.make(fit=True)
    img =qr.make_image()
    img.save("baidu.jpg")
    #img.show()
    
    image = cv2.imread('baidu.jpg')# 读取图片
    # 找到图像中的条形码并进行解码
    barcodes = pyzbar.decode(image)
    barcodeData = barcodes[0].data
    # 进行解密操作
    print("请输入密钥")
    # 输入密钥
    KEY2="mHAxsLYz"
    print(KEY2)
    barcodeData=des_descrypt(barcodeData,KEY2)
    if barcodeData!=None:
        print("该二维码包含的信息为："+barcodeData)
        pattern(barcodeData)

if __name__=='__main__':
    main()     


