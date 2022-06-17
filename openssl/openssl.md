# openssl

## 简介

OpenSSL 命令
https://blog.csdn.net/t990423909/article/details/120837032

## 向CA机构申请CA证书

1. 用户本地生成server私钥

2. 用户用server私钥生成CSR文件（包含server公钥以及用户身份信息等），并发送CSR请求给受信CA机构

3. CA机构对CSR中用户身份信息验证通过后，用根CA对CSR进行签名（盖上本CA机构的公章），生成SSL证书颁发给用户

   ps：SSL数字证书包含了你个人的server公钥、个人信息以及CA机构的信息。由于SSL证书将server公钥与个人信息匹配，并且该证书的真实性由颁发机构保证，因此SSL数字证书为如何找到用户的公钥并知道它是否有效这一问题提供了解决方案。

4. 用户将server私钥、SSL证书用于自己的web应用

## 使用openssl创建证书

1. **CA机构根证书的生成**

   1. 生成私钥，伴随导出的公钥相当于CA机构的根证书

      但是一般会签出二级（或多级）证书用于给用户提供签名

      ```bash
      openssl genrsa -out ca_organization.key 2048
      ```

   2. 生成CSR

      ```bash
      openssl req -new -key ca_organization.key -out ca_organization.csr
      ```

      CSR文件中需要注入CA机构的信息，可以用参数`-subj`指定，于是

      ```bash
      openssl req -new -key ca_organization.key -subj "/C=cn/ST=hubei/L=wuhan/O=Default" -out ca_organization.csr
      ```

      也可以参数`-config`指定下面配置文件ca_organization_csr.conf

      ```ini
      [ req ]
      default_bits = 2048
      prompt = no
      default_md = sha256
      req_extensions = req_ext
      distinguished_name = dn
       
      [ dn ]
      C = US
      ST = California
      L = San Fransisco
      O = MLopsHub
      OU = MlopsHub Dev
      CN = 127.0.0.1
       
      [ req_ext ]
      subjectAltName = @alt_names
       
      [ alt_names ]
      IP.1 = 127.0.0.1
      ```

      生成CSR文件命令为：

      ```bash
      openssl req -new -key ca_organization.key -config ca_organization_csr.conf -out ca_organization.csr
      ```

   3. 自签名得到证书rootCA

      这个证书对于用户来说是根CA证书，但是对于CA机构来说算是二级证书了

      ```bash
      openssl x509 -req -days 365 -in ca_organization.csr -signkey ca_organization.key -out ca_organization.crt
      ```

2. **用户证书的生成**

   1. 生成用户server私钥，伴随着server公钥

      ```bash
      openssl genrsa -out server.key 1024
      ```

   2. 生成证书请求csr文件

      ```bash
      openssl req -new -key server.key -subj "/C=cn/ST=hunan/L=shangsha" -out server.csr
      ```

   3. 请求CA机构，用根CA证书签名得到用户SSL证书

      ```bash
      openssl ca -in server.csr -out server.crt -cert ca_organization.crt -keyfile ca_organization.key
      ```

## 创建自签名证书

类似于向CA机构申请证书一样，仅将向CA机构发送CSR获取SSL证书的过程，变为用自己创建的根CA、私钥进行签名即可。

1. 创建我们自己的根 CA 证书和 根CA 私钥（自己充当 CA机构）
2. 本地生成server私钥，并用根CA及根私钥进行签名生成带有CSR的SSL证书
3. 将server私钥、SSL证书用于web应用服务器
4. 浏览器或操作系统安装SSL证书，手动使之受信

## 使用自签名证书有什么好处？

您无需依赖第三方来签署您的证书。
您可以创建和使用自己的证书颁发机构。
您不必为 CA 的证书付费。
您可以更好地控制您的证书。

## 使用自签名证书有什么缺点？

您的用户需要在他们的浏览器或应用程序中安装证书。
您的用户将需要手动信任您的证书颁发机构。
它们对于面向公众的应用程序不安全。
除非用户安装它们，否则所有浏览器或操作系统都不信任自签名证书。
容易受到中间人攻击。
