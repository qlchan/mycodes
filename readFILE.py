#!/bin/evn python
#coding=gb18030
import subprocess  
import os 
import time

#by cql 2014/9/9
#�����ύ�˶��ļ���ʱ�򣬳�����©�����ߡ�
#·��ԽСԽ�ã���Ȼ����


def printPath(level, path ):
    OpenFile = open('list.txt','a+')
    ''''' 
    ��ӡһ��Ŀ¼�µ������ļ��к��ļ� 
    '''  
    # �����ļ��У���һ���ֶ��Ǵ�Ŀ¼�ļ���  
    dirList = []  
    # �����ļ�  
    fileList = []  
    # ����һ���б����а�����Ŀ¼��Ŀ������(google����)  
    files = os.listdir(path)  
    # �����Ŀ¼����  
    dirList.append(str(level))  
    for f in files:  
        if(os.path.isdir(path + '/' + f)):  
            # �ų������ļ��С���Ϊ�����ļ��й���  
            if(f[0] == '.'):  
                pass  
            else:  
                # ��ӷ������ļ���  
                dirList.append(f)  
        if(os.path.isfile(path + '/' + f)):  
            # ����ļ�  
            paths =  path + '/' + f
           # ospath = subprocess.Popen('svn log "%s"'%paths,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            #out = ospath.communicate()[0]
            #name = 'MSC-5567'
            #num = out.find( name )
            #if( num > 0):
            print paths
            print >> OpenFile,paths
            fileList.append(f)  
    # ��һ����־ʹ�ã��ļ����б��һ�����𲻴�ӡ  
    i_dl = 0  
    for dl in dirList:  
        if(i_dl == 0):  
            i_dl = i_dl + 1  
        else:  
            # ��ӡĿ¼�µ������ļ��к��ļ���Ŀ¼����+1  
            printPath((int(dirList[0]) + 1), path + '/' + dl )  
    '''for fl in fileList:  
        # ��ӡ�ļ�  
        print '-' * (int(dirList[0])), fl  
        # ������һ���ж��ٸ��ļ�  
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
    paths = raw_input("���㣬����·���ǣ�")
    #commit = raw_input("jira���ǣ�")
    #printPath(1, paths , commit)  
    #path="E:/www/ganji/ganji_online/mobile/mobile_base/apps/sconsole/trunk"
    #quick(path,name)
    #printPath()
    #VisitDir(path,name)
    printPath(100, paths)