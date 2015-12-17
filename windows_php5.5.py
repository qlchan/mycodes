#!/bin/evn python
#coding=gb18030
import subprocess
import types 
#import time
"""
适合习惯用mount挂载文件的广大同学
@cql 2014/8/4
"""
""" 
list = [
        'call_user_method', 
        'call_user_method_array',
        'define_syslog_variables',
        'dl',
        'ereg', 'ereg_replace',
        'eregi', 'eregi_replace',      
        'session_register', 'session_unregister',
        'session_is_registered', 'set_socket_blocking',
        'split', 'spliti',
        'sql_regcase', 'mysql_db_query',
        'mysql_escape_string',
        'set_magic_quotes_runtime'
       ]
   
dir = [
        'E:/www/ganji/ganji_online/mobile/mobile_base/apps/wap/*.php',
        'E:/www/ganji/ganji_online/mobile/mobile_base/apps/misc/*.php',
        'E:/www/ganji/ganji_online/mobile/mobile_base/apps/web_client/*.php'
        
     ]
"""
list = [
         'getDataFromXml'
       ]
def outPrint():
    OpenFile = open('list.txt','w+')
    for fuc in list:
        fucM = fuc+'('
        #print "find  '/home/mobile/mobile_base/apps/wap/' -name '*.php' -print | xargs grep '%s' "%fucM 
        print "findstr /s '%s' '/mobile/mobile_base/apps/*.php'"%fucM
        os = subprocess.Popen('findstr /s "%s" "E:/www/ganji/ganji_online/mobile/mobile_base/*.php"'%fucM,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out = os.communicate()[0]
        #time.sleep(3)
        print out
        print >> OpenFile,out
    OpenFile.close()

    
