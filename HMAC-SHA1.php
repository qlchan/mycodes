<?php
/**
 * @brief 使用HMAC-SHA1算法生成oauth_signature签名值 
 *
 * @param $key  密钥
 * @param $str  源串
 *
 * @return 签名值
 */
 
function custom_hmac($algo, $data, $key, $raw_output = false)
{
    $algo = strtolower($algo);
    $pack = 'H'.strlen($algo('test'));
    $size = 64;
    $opad = str_repeat(chr(0x5C), $size);
    $ipad = str_repeat(chr(0x36), $size);
 
    if (strlen($key) > $size) {
        $key = str_pad(pack($pack, $algo($key)), $size, chr(0x00));
    } else {
        $key = str_pad($key, $size, chr(0x00));
    }
 
    for ($i = 0; $i < strlen($key) - 1; $i++) {
        $opad[$i] = $opad[$i] ^ $key[$i];
        $ipad[$i] = $ipad[$i] ^ $key[$i];
    }
 
    $output = $algo($opad.pack($pack, $algo($ipad.$data)));
 
    return ($raw_output) ? pack($pack, $output) : $output;
}
function get_signature($str, $key)
{
    $signature = "";
    if (function_exists('hash_hmac'))
    {
        $signature = hash_hmac("sha1", $str, $key);
    }
    else
    {
        $signature = custom_hmac("sha1", $str, $key);
        
    }
 
    return $signature;
} 
 
echo get_signature("img_url=http://s1.bdstatic.com/r/www/cache/xmas2012/images/car.png&nickname=anything&profile_url=http://3g.ganji.com&user_id=500011302", "bd9c83161441a1e68fa309455f09bf59");
 
?>

