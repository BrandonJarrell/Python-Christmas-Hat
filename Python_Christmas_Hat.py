import os
import random

def main():
   
   print("\tCHRISTMAS NAME DRAWER\n\nNo more drawing from a hat, this is 21st Century!!\n")
   #Instructions
   print("\ttype a name and hit enter, hit enter again when done\n")
   names = assignNames(takeInput())
   userInput = input("Would you like to save this to a file? y/n: ")
   if (userInput == 'y' or userInput == 'Y'):
      saveNames(names)

   print("\nHave a pleasant day!")

#####################
# User Input
#####################
def takeInput():
   userInput = ""
   output = ""
   listOfPeople = {}
   i = 1
   while(True):
      userInput = input("Name %a: " % (i))
      if(userInput != ""):
         output += (userInput + ", ")
         listOfPeople[i] = Person(userInput)
         i += 1
      else: 
         output = output[:-2] #remoes the final ", "
         break
   print ("\n Creating a hat using %a" % (output))

   #Take Input for couples
   userInput = input("\nAre there any couples you dont want to draw each other? y/n:")
   if(userInput == 'y' or userInput == 'Y'):
      listOfPeople = seperateCouples(listOfPeople)
   else:
      print("Okay, they can draw each other (weird)\n")
   return listOfPeople

#####################
# Assigns each couple who they cant draw
#####################
def seperateCouples(peopleList):
   print("\tSeperating couples\n")
   print("Who are the couples? Please type their names as before")
   print("Leave both names empty when done")
   name1 = " "
   name2 = " "
   z = 1
   while (name1 != ""):
      print("\nCouple %a: "%(z))
      for i in range(1,2):
         name1 = input("Name 1: ")
         name2 = input("Name 2: ")
         z+=1
         for x in range(1,len(peopleList)+1):
            if(peopleList[x].name == name1):
               peopleList[x].cantDraw = name2
            if(peopleList[x].name == name2):
               peopleList[x].cantDraw = name1
   for i in range(1,len(peopleList)+1):
      if(peopleList[i].cantDraw != ""):
         print(peopleList[i].name + " Cant Draw " + peopleList[i].cantDraw)
   print("\n\n")
   return peopleList

#####################
# Assign the present giving!! (sadly with brute force)
#####################
def assignNames(peopleDrawing):
   i = 1
   while i <= len(peopleDrawing):
      randomPerson = random.randint(1,len(peopleDrawing))
      #check
      if((randomPerson == i) or (peopleDrawing[randomPerson].drawn == True) or (peopleDrawing[i].cantDraw == peopleDrawing[randomPerson].name)):
         continue
      print("\t" + peopleDrawing[i].name + " Has " + peopleDrawing[randomPerson].name)
      peopleDrawing[i].nameDrawn = peopleDrawing[randomPerson].name
      peopleDrawing[randomPerson].drawn = True
      i+=1
   return peopleDrawing

####################
# Writes to a file
####################
def saveNames(peopleLists):
   fileName = input("\nWhat would you like to name this file? This years date would be a good idea\n\t:")
   file = open(fileName + ".txt", 'w')
   for i in range(1,len(peopleLists)+1):
      file.write(peopleLists[i].name + " Has " + peopleLists[i].nameDrawn + "'s name\n\n" )
   print("\nDone\n")

####################
# PERSON CLASS
####################
class Person:
   def __init__(self, name):
      self.name = name
      self.drawn = False
   
   cantDraw = ""
   nameDrawn = ""

#clear system
os.system("cls")
main()
