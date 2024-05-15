import pandas as pd
import os
from django import forms

class FileForm(forms.Form):
    file = forms.FileField(
        # 支持多文件上传
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        label='请选择文件',
    )


def fromFilePath(fileName):
  file_path = os.path.join('static/',fileName)
  return file_path

def loadTxt(fileName,isStrip=True):
    fileName = fromFilePath(fileName)
    data=[]
    with open(fileName, "r") as fileObj:
        for line in fileObj.readlines():
            if isStrip:
                data.append(line.strip())
            else:
                data.append(line)
    return data

def readFileByType(fileName, param,header):
    filepath = fileName.split('.')
    ext = filepath[len(filepath) - 1]
    if ext == "xlsx":
        return readExcel(fileName, param,header)

def getListFromExcel(fileName, sheetName,noHead=True):
    data=readExcel(fileName, sheetName,None)
    data_list=data.values.tolist()
    if noHead and len(data_list)>0:
        data_list.pop(0)
    return data_list

def readExcel(fileName, sheetName,header):
    file = pd.ExcelFile(fileName)
    if header!=-1:
        data = pd.read_excel(file, sheetName,header=header)
    else:
        data = pd.read_excel(file, sheetName)
    return data

def getFileName(subDirName=""):
    fileNames = []
    if subDirName == "":
        path = os.listdir('static/')
    else:
        path = os.listdir('static/' + subDirName)
    for p in path:
        if not os.path.isdir(p):
            if not '~$' in p and not 'DS_Store' in p:
                if subDirName == "":
                    fileNames.append(os.path.join('', p))
                else:
                    fileNames.append(os.path.join(subDirName + '/', p))
    return fileNames

def getFilePath(fileName,subDirName):
    return os.path.join(subDirName + '/', fileName)

class ExcelFile():
    def __init__(self, subDir,sheets):
        self.subDir = subDir
        self.sheets = sheets
        self.colomns = []

    def addColomn(self, colName):
        self.colomns.add(colName)

    def getAllData(self,header=-1):
        data_list = []
        fileNames = getFileName(self.subDir)
        for fileName in fileNames:
            for sheetName in self.sheets:
                #print(fileName, sheetName)
                temp_excel_data = readFileByType(fromFilePath(fileName), sheetName,header)
                #print()
                if len(temp_excel_data) > 0:
                    data_list.append(temp_excel_data)

        return pd.concat(data_list)
