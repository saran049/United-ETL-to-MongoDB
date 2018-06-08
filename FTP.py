# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:46:08 2018

@author: Saran
"""

import ftplib
import pandas as pd


#ftp = FTP("ftp://192.168.0.32/", "FTP_user", "saran4993")

ftp = ftplib.FTP('192.168.0.32')
ftp.login('FTP_user', 'saran4993')

# grt file from FTP and store in local file
def getfile():
    filename = 'item_list.txt'
    localfile = open('C:/Users/saran/Desktop/abc/filename','wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()


# Load the local file

def load_file():
    dup_list = pd.read_csv('C:///Users///saran///Desktop///abc///filename',sep = '|',
                           header = None,encoding='latin1')
    col_names = ["UPC","Status","RootID","LongDes","ShortDes","ClassCode","ClassDes","CategoryCode","CategoryDes",
                 "FamilyCode","FamilyDes","DepartmentCode","DepartmentDes","StoreBrand","ExtraDes","ec"]
    dup_list.columns = col_names
    dup_list = dup_list.drop(['ec'],axis = 1)
    dup_list.dtypes
    

# comparing two columns

def compare_UPC():
    new_UPC = pd.DataFrame([])
    for item in dup_list['UPC']:
        if item not in item_list['UPC']:
            new_UPC.append(dup_list)

            
getfile()
load_file()
compare_UPC()
