<?php
class WapWeibaStrToolModel {
	/**
	 * 截取字符串
	 * 	本函数过滤掉了所有的空白字符
	 * 	长度按照汉字截取，比如截取长度为1，则截取1个汉字，1个汉字的长度=1个英文字母的长度
	 * 	
	 * @param $str     待截取的字符串
	 * @param $start   截取的开始位置
	 * @param $length  截取的长度
	 * @param $suffix  如果字符串的长度比需要截取的长度长，则添加的后缀字符，不需要的话需要设置为空
	 * @param $charset 待截取字符串的编码
	 */
	public static function msubstr( $str, $start=0, $length, $suffix="...", $charset="utf-8" ){
		$str    = str_replace( "　","",$str );//过滤数据库中特殊空字符
		$str    = trim( strip_tags( html_entity_decode( $str,ENT_COMPAT,$charset ) ) );
		$str    = str_replace( "\n","",$str );
		$str    = str_replace( "\r\n","",$str );
		$str    = str_replace( "\t","",$str );
		$str    = str_replace( "\r","",$str );
		$str    = str_replace( " ","",$str );
		$str    = str_replace( "&nbsp;","",$str );
		$strlen = mb_strlen( $str,$charset );
		$str    = mb_substr( $str,$start,$length,$charset );
		return ($length>=$strlen)?$str:$str.$suffix;
	}
	/**
	 * Summary:   解决去除标签时出现“？”的问题
	 * @return unknown
	 */
	
	public static function msubstr2( $str, $start=0, $length, $suffix="...", $charset="utf-8"){
		$str    = str_replace( "　","",$str );//过滤数据库中特殊空字符
		$str    = trim( strip_tags( html_entity_decode( $str,ENT_COMPAT,$charset ) ) );
		$str    = str_replace( "\n","",$str );
		$str    = str_replace( "\r\n","",$str );
		$str    = str_replace( "\t","",$str );
		$str    = str_replace( "\r","",$str );
		$str    = str_replace( " ","",$str );
		$str    = str_replace( "&nbsp;","",$str );
		$strlen = mb_strlen( $str,$charset );
		$str    = mb_strcut( $str,$start,$length,$charset );
		return ($length>=$strlen)?$str:$str.$suffix;
	}
	
	/**
	 * 按照字符串来截取utf-8文字的函数
	 * @param unknown_type $string 被截取的字符串
	 * @param unknown_type $length 要被截取的长度
	 * @param unknown_type $etc    如果字符串长度超过了截取的，后面的尾巴
	 * @return string|unknown
	 */
	public static function get_utf8_word($string, $length = 80, $etc = '...')
	{
		$strcut = '';
		$strLength = 0;
		$width  = 0;
		if(strlen($string) > $length) {
			//将$length换算成实际UTF8格式编码下字符串的长度
			for($i = 0; $i < $length; $i++) {
				if ( $strLength >= strlen($string) ){
					break;
				}
				if ( $width>=$length){
					break;
				}
				//当检测到一个中文字符时
				if( ord($string[$strLength]) > 127 ){
					$strLength += 3;
					$width     += 2;              //大概按一个汉字宽度相当于两个英文字符的宽度
				}else{
					$strLength += 1;
					$width     += 1;
				}
			}
			return substr($string, 0, $strLength).$etc;
		} else {
			return $string;
		}
	}	
}
