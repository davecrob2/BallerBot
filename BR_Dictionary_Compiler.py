# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 22:38:14 2017

@author: davecrob2
"""

import csv

#Variables assigned to the playerlist file stored on computer
PlayersCsv="C:\\Users\\davecrob2\\Documents\\GitHub\\BallerBot\\PlayerList_A-C.csv"
CommenterInput=str(input("Enter Player Name"))
#Opens PlayersCSV and reads .csv file
with open(PlayersCsv, mode='r') as infile:
    reader = csv.reader(infile)
    
    #iterates through rows to turn the list into an accesible python dictionary
    PlayerDict = {rows[0]:rows[1] for rows in reader}
    
    #print(PlayerDict)
    
print(PlayerDict[CommenterInput])

#Returns first letter of key for purposes of populating BR URL
character = PlayerDict[CommenterInput]
print(character[0])