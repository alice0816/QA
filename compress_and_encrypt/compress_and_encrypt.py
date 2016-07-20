# -*- coding:utf-8 -*-
'''
Created on 2016/7/20

@author: xinfeng.yang
'''

# coding:utf-8
import os
import zipfile

def zipdir(dirToZip,savePath):
    if not os.path.isdir(dirToZip):
        raise Exception,u"zipDir Error,not a dir‘%‘".format(dirToZip)

#     (saveDir,_)=os.path.split(savePath)
#     if not os.path.isdir(saveDir):
#         os.makedirs(saveDir)

    zipList = []

    for root,dirs,files in os.walk(dirToZip):
        for fileItem in files:
            zipList.append(os.path.join(root,fileItem))
        for dirItem in dirs:
            zipList.append(os.path.join(root,dirItem))

    zf = zipfile.ZipFile(savePath,'w',zipfile.ZIP_DEFLATED)

    for tar in zipList:
        zf.setpassword('hello')
        if tar != dirToZip:
            zf.write(tar,tar.replace(dirToZip,''))
        else:
            zf.write(tar)
    
    
    zf.close()
    
zipdir('D:\\logs\\log', 'D:\\logs.zip')  

    