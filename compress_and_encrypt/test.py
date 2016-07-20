#!/usr/bin/Python  
# Filename: backup_ver1.py  
# import os  
# import time  
# source =[r'D:\logs\log', r'E:\work']  
# target_dir = 'F:\\back up\\' # Remember to change this to what you will be using  
# target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'  
# zip_command = "zip -qr \"%s\" \"%s\"" % (target, ' '.join(source))  
# # Run the backup  
# if os.system(zip_command) == 0:  
#     print 'Successful backup to', target  
# else:  
#     print 'Backup FAILED' 

from subprocess import *  

zipcommand = r'"C:\Program Files (x86)\7-Zip\7z.exe" a -p D:\log.zip D:\logs\log' 
# call(zipcommand)
p =Popen(zipcommand ,stdin=PIPE,stdout=PIPE)
# if p.stdout.readline() ==''
p.stdin.write('123456') 
# p = sp.Popen(cmd, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.PIPE, shell=True)
# 
# Popen.communicate('123456')