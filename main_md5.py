# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:16:48 2019

@author: Administrator
"""

import hashlib
m = hashlib.md5()
m.update(b'hello, world!')
code=m.hexdigest()

from hashlib import md5, sha1, sha224, sha256, sha384, sha512

hash_md5 = md5()  # MD5 hash对象
hash_sha1 = sha1()  # SHA1 hash对象
hash_sha224 = sha224()  # SHA224 hash对象
hash_sha256 = sha256()  # SHA256 hash对象
hash_sha384 = sha384()  # SHA384 hash对象
hash_sha512 = sha512()  # SHA512 hash对象

def main():
    my_str = 'TengTengCai Is A Good Boy.'
    print('将要生成摘要的字符串:', my_str)

    # MD5 加密
    h_md5 = hash_md5.copy()  # 复制一个对象，避免频繁创建对象消耗性能
    h_md5.update(my_str.encode('utf-8'))  # 需要将字符串进行编码，编码成二进制数据
    md5_str = h_md5.hexdigest()  # 获取16进制的摘要
    print('MD5生成摘要结果:',md5_str)  # 输出结果

    # SHA1 摘要
    h_sha1 = hash_sha1.copy()
    h_sha1.update(my_str.encode('utf-8'))
    sha1_str = h_sha1.hexdigest()
    print('SHA1生成摘要结果:', sha1_str)

    # SHA224 摘要
    h_sha224 = hash_sha224.copy()
    h_sha224.update(my_str.encode('utf-8'))
    sha224_str = h_sha224.hexdigest()
    print('SHA224生成摘要结果:', sha224_str)

    # SHA256 摘要
    h_sha256 = hash_sha256.copy()
    h_sha256.update(my_str.encode('utf-8'))
    sha256_str = h_sha256.hexdigest()
    print('SHA256生成摘要结果:', sha256_str)

    # SHA384 摘要
    h_sha384 = hash_sha384.copy()
    h_sha384.update(my_str.encode('utf-8'))
    sha384_str = h_sha384.hexdigest()
    print('SHA384生成摘要结果:', sha384_str)

    # SHA512 摘要
    h_sha512 = hash_sha512.copy()
    h_sha512.update(my_str.encode('utf-8'))
    sha512_str = h_sha512.hexdigest()
    print('SHA512生成摘要结果:', sha512_str)


if __name__ == '__main__':
    main()
