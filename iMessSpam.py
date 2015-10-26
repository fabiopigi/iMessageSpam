# -*- coding: utf-8 -*-
#import some dope
import sys
import os
import re
import time
from random import randrange
from itertools import repeat

numbers = {
	'adam'		:"+41111111111",
	'bob'		:"+41222222222",
	'chris'		:"+41333333333",
	'dave'		:"+41444444444",
	}
	

print "Gespeicherte Empfänger: "
for name in numbers:
	print "%10s - %s"%(name,numbers[name])
	

number = ""
while number == "":
	numberID = raw_input("\nEmpfänger eingeben: ")
	if numberID in numbers:
		number = numbers[numberID]
		

pause = int(raw_input("\nIntervall in Sekunden: "))	
	

print """
Verfügbare Optionen:
  [1]	Zeitansagen im Format 'Es ist 17:34:22'
  [2]	Zufällige 'Chuck Norris' Jokes
  [3]	Satz für Satz aus einem Buch (Twilight)
  [4]	Fifty Shades of HEX
  [5]	Fröhliches Flaggen raten
"""
option = int(raw_input("Option auswählen: "))	


if option == 1:
	anzahl = int(raw_input("\nAnzahl Nachrichten: "))
	start = 0
elif option == 2:
	anzahl = int(raw_input("\nAnzahl Nachrichten: "))
	start = 0
	replaceName = raw_input("\n'Chuck Norris' durch Namen ersetzen: ")
	if replaceName == "":
		replaceName = "Chuck Norris"
elif option == 3:
	p = open('content/twilight.txt')
	book = p.read()
	pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
	sentences = pat.findall(book)	
	anzahl = int(raw_input("\nAnzahl Nachrichten: "))
	start = int(raw_input("\nBei n. Satz anfangen: "))-1
	anzahl = anzahl + (start)
elif option == 4:
	anzahl = 50
	start = 0
elif option == 5:
	anzahl = 50
	start = 0
	import Countries
else:
	anzahl = 0
	start = 0	



print "\n\nSenden beginnt...\n\n"



#tunay bei 207
for i in range(start,anzahl,1):
	
	
	
	if option == 1:
		cmdCode = "date +'%H:%M:%S'"
		message = "Es ist jetzt " + os.popen(cmdCode).read()	
	elif option == 2:
		curlCode = "curl 'http://api.icndb.com/jokes/random' -s | sed -e 's/.*joke\\\": \\\"//'  -e 's/\\\", \\\".*//'  -e 's/Chuck Norris/" + replaceName + "/g' -e 's/&quot;/\"/g'"
		message = os.popen(curlCode).read()
	elif option == 3:
		message = sentences[i]
		
	elif option == 4:
		message = "#%s" % "".join(list(repeat(hex(randrange(16, 255))[2:],3))).upper()

	elif option == 5:
		flags = os.listdir("content/flags")
		country = Countries.iso[flags[randrange(1,len(flags))][:2]]
		
		message = "Dies ist die Flagge von '%s'."%(country["Name"])
		filePath = os.path.abspath("content/flags/%s.png"%country["ISO"])
		osaCode = "osascript sendImage.scpt \"%s\" \"%s\""%(number,filePath)
		osaReturn = os.popen(osaCode).read()
		print message
	
	message = message.replace('"', r'\"')
	osaCode = "osascript sendText.scpt \"%s\" \"%s\""%(number,message)
	print "%3d > %s"%((i+1),message)
	osaReturn = os.popen(osaCode).read()
	
	
	
	time.sleep(pause)



