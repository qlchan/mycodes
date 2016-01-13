<?php
/**
 RSA  公钥 私钥加密
生成rsa密钥
openssl genrsa -des3 -out prikey.pem
去除掉密钥文件保护密码
openssl rsa -in prikey.pem -out prikey.pem
分离出公钥
openssl rsa -in prikey.pem -pubout -out pubkey.pem
@author: cql 2016 1/1/
 eg: 如下
*/
$pri_file = '/home/www/work/prikey.pem';
function get_privkey($pri_file){
    $fp = fopen($pri_file, "rb");
    $priv_key = fread( $fp, 8192 );
    fclose($fp);
    $prikey = openssl_get_privatekey($priv_key,'abcde');
    $prikeyid=$prikey;
    openssl_free_key($prikey);
    return $prikeyid;
}

$pub_file = '/home/www/work/pubkey.pem';
function get_pubvkey($pub_file){ 
   $fp = fopen( $pub_file, "r" );
   $pub_key = fread( $fp, 8192 );
   fclose($fp);
   $pubkey = openssl_get_publickey($pub_key );
   $pubkeyid = $pubkey;
   openssl_free_key($pubkey);
   return $pubkeyid;
}
$pr_key = get_privkey($pri_file);
$pu_key = get_pubvkey($pub_file);

//中文加密需要加header
header ( "Content-Type: text/html; charset=utf-8" );

$data = '中国人民哈哈';

openssl_private_encrypt($data, $crypted, $pr_key);
////加密后的内容通常含有特殊字符，需要编码转换下，在网络间通过url传输时要注意base64编码是否是url安全的  
$encrypted = base64_encode($crypted);

openssl_public_decrypt(base64_decode($encrypted), $decrypted, $pu_key);
echo "DeCode:" . $decrypted;

?>
