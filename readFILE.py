#!/bin/evn python
#coding=gb18030
import subprocess  
import os 
import time

#by cql 2014/9/9
#起因，提交了多文件的时候，常常遗漏带上线。
#路径越小越好，不然很慢


def printPath(level, path ):
    OpenFile = open('list.txt','a+')
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''  
    # 所有文件夹，第一个字段是次目录的级别  
    dirList = []  
    # 所有文件  
    fileList = []  
    # 返回一个列表，其中包含在目录条目的名称(google翻译)  
    files = os.listdir(path)  
    # 先添加目录级别  
    dirList.append(str(level))  
    for f in files:  
        if(os.path.isdir(path + '/' + f)):  
            # 排除隐藏文件夹。因为隐藏文件夹过多  
            if(f[0] == '.'):  
                pass  
            else:  
                # 添加非隐藏文件夹  
                dirList.append(f)  
        if(os.path.isfile(path + '/' + f)):  
            # 添加文件  
            paths =  path + '/' + f
           # ospath = subprocess.Popen('svn log "%s"'%paths,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            #out = ospath.communicate()[0]
            #name = 'MSC-5567'
            #num = out.find( name )
            #if( num > 0):
            print paths
            print >> OpenFile,paths
            fileList.append(f)  
    # 当一个标志使用，文件夹列表第一个级别不打印  
    i_dl = 0  
    for dl in dirList:  
        if(i_dl == 0):  
            i_dl = i_dl + 1  
        else:  
            # 打印目录下的所有文件夹和文件，目录级别+1  
            printPath((int(dirList[0]) + 1), path + '/' + dl )  
    '''for fl in fileList:  
        # 打印文件  
        print '-' * (int(dirList[0])), fl  
        # 随便计算一下有多少个文件  
        allFileNum = allFileNum + 1  '''
        
        
        
def VisitDir(path ,name):
  for root,dirs,files in os.walk(path):
    for filespath in files:
        paths = os.path.join(root,filespath)
       # if filespath.endswith('.php'):
            #print fileLast
        ospath = subprocess.Popen('svn log "%s"'%paths,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out = ospath.communicate()[0]
        num = out.find( name )
        if( num > 0):
            print paths
            

def quick(path ,name):
    ospath = subprocess.Popen('svn log "%s"'%path,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    print ospath
    '''out = ospath.communicate()[0]
            num = out.find( name )
            if( num > 0):
                print paths'''
    
    


if __name__ == '__main__':  
    paths = raw_input("顶你，查找路径是：")
    #commit = raw_input("jira号是：")
    #printPath(1, paths , commit)  
    #path="E:/www/ganji/ganji_online/mobile/mobile_base/apps/sconsole/trunk"
    #quick(path,name)
    #printPath()
    #VisitDir(path,name)
    printPath(100, paths)