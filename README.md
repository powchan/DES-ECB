# DES-ECB
实现了DES加解密的ECB模式。文件结构如下：
##### main.c 
用C语言实现DES加密，仅支持**8**字节明文/密文/密钥加解密。

##### judge.py
测试加解密程序正确性的脚本，仅支持在Linux系统下运行。  
需要安装库：`pycryptodome`、`pwntools`

##### main.py
Python实现的版本，为 [https://www.cnblogs.com/luogi/p/15508933.html#python%E5%AE%9E%E7%8E%B0] 处的代码