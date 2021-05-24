# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="hitesh",
  database="majorProject"
)

mycursor = mydb.cursor()

query = "Select * from TV where `Speaker`=%s AND `Size`=%s AND `HD`=%s AND `HDMI`=%s AND `USB`=%s ORDER BY `Cost`, `Ratings` LIMIT 3"
  
def output(speaker,size,hd,hdmi,usb):
  inputs=(speaker,size,hd,hdmi,usb)
  mycursor.execute(query,inputs)
  myresult = mycursor.fetchall()
  tv1 = {"Brand" :  myresult[0][0],
    "Ratings" : myresult[0][1] ,
    "Speaker" : myresult[0][2],
    "Size" : myresult[0][3] ,
    "Quality" : myresult[0][4] ,
    "HDMI" : myresult[0][5] ,
    "USB" : myresult[0][6] ,
    "Cost" : myresult[0][7]}

  tv2 = {"Brand" : myresult[1][0] ,
    "Ratings" : myresult[1][1] ,
    "Speaker" : myresult[1][2],
    "Size" : myresult[1][3] ,
    "Quality" : myresult[1][4] ,
    "HDMI" : myresult[1][5] ,
    "USB" : myresult[1][6] ,
    "Cost" : myresult[1][7]}

  tv3 = {"Brand" : myresult[2][0] ,
    "Ratings" : myresult[2][1] ,
    "Speaker" : myresult[2][2],
    "Size" : myresult[2][3] ,
    "Quality" : myresult[2][4] ,
    "HDMI" : myresult[2][5] ,
    "USB" : myresult[2][6] ,
    "Cost" : myresult[2][7]}

  return tv1, tv2, tv3
  
