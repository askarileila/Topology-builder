# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:01:15 2019

@author: Leila Askari
"""

import xlrd
import os.path
wb = xlrd.open_workbook("big.xlsx")
wb.sheet_names()
sh = wb.sheet_by_index(0)
i = 0
n=0
Load=0
#for reading from text file
'''f = open("TimS.txt", "r")
content=f.readline()
currentline=content.split("<")'''
#file = open("Output2.txt", "w")
with open("TimS.txt", "r") as filestream:
    with open("answers.txt", "w") as filestreamtwo:
        for line in filestream:
            currentline = line.split(",")
            total="<link id=\""+str((currentline[0].replace("<","")))+"\""+" "+ "originNodeId=\""+str(currentline[1].lstrip())+"\""+" "+ "destinationNodeId=\""+str(currentline[2].lstrip())+"\""+" "+ "capacity=\"50.0\""+" "+"lengthInKm=\""+str(currentline[5].replace(">","").lstrip())+"\""+" "+ "propagationSpeedInKmPerSecond=\"200000.0\" isUp=\"true\">"+'\n'+"</link>"+'\n'
            #total = str((currentline[0].replace("<","")) + (currentline[1]) + (currentline [2])) + "\n"
            filestreamtwo.write(total)
print("file is opened")
#while sh.cell(i,0).value != 0:
'''for n in range(sh.nrows):  
 
 # Load = int((sh.cell(i,0).value))
   D1 = int((sh.cell(i,1).value))
   D2 = int(sh.cell(i,2).value)
   D3 = sh.cell(i,3).value

   DB1 = "<"+ str(Load) + ", " + str(D1) + ", " + str(D2) + ", " + "8, "+ "1, " + str(D3)+ ">" 
   Load=Load+1
   DB2 = "<"+ str(Load) + ", " + str(D2) + ", " + str(D1) + ", " + "8, "+ "1, " + str(D3)+ ">" 
   

   file.write(DB1 + ', '+ DB2 +', ')
   i = i + 1
   Load=Load+1
file.close'''