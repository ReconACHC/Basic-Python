import random
import time


name = input ('What is your name?\n')
print ('Hi %s, Your IQ is...'%name)
time.sleep (1)

luc = random.randint(150,250)
if name=="Luca":
 print (luc)

iq=random.randint(2,180)
print (iq)
time.sleep(1)
if (iq)<127:
 print ("Your Dumb.... lol")

time.sleep(1)
if (iq)>127:
 print ("Your Clever....")

elif (iq)==127:
  print ("Thats not meant to happen")
