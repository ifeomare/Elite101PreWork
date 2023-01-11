#This program is a starter chatbot program submitted by a fellow Elite 101 student.
# It's been modified to fit the purpose of the Elite 101 Pre-work Project.

import random

#NAME
userName = input("What is your name? ")
print("Hi there, " + userName  + ". You have a beautiful name!")

#FEELINGS
def userFeeling(feeling):
  #randresp1 = random.randint(1,2)
  #randresp2 = random.randint(1,2)
  good = ["happy","excited" , "great" , "ok" ,"good" , "well" , "nice"]
  bad = ["sad", "not good","unhappy" ,"bad"]
  
  if feeling in good:
    print("That's great to hear!")
  elif feeling in bad:
    print("I'm sorry you are feeling that way.")
  
# feeling = input("\nHow are you feeling? ").lower()
# userFeeling(feeling)


#AGE
def userAge(age):
  response3 = random.randint(1, 2)
  
  if age < 5:
    print("Oh my! You're so young! ")
  elif age < 10:
    input("What's the coolest things about your school? ")
  elif age <13:
    if response3 == 1:
      input("How is Middle School treating you?")
    elif response3 == 2:
      input("Are you interested in any sports?")
  elif age < 18:
    if response3 == 1:
      input("Is there anything you look forward to in High School?")
    elif response3 == 2:
      input("Do you have a job yet? If so, how's it going?")
  elif age < 23:
    input("Are you in college? How's the campus life treating you?")
  elif age < 120:
    if response3 == 1:
       print("Oh, an adult? That's cool!")
    else:
      input("Are you retired yet? What was your past/current job?")
  else:
      print("You can't be that old. Try again.")
      age2 = int(input("What is your age?"))
      if age2<120:
        print("Okay! This more like an age number.")

def userHobby():
  response3 = random.randint(1, 2)
  if response3 == 1:
    input("What are your hobbies?")
  else:
    input("Are you involved in any sports or clubs?")

# try:
#   age = int(input("\nWhat is your age? "))
# except:
#   age =5

# myAge(age)

questions = ["1", "2", "3"]
for x in range(3):
  randomQuestion = random.choice(questions)
  if randomQuestion == 0:
    feeling = input("How are you feeling today? ")
    userFeeling(feeling)
  elif randomQuestion == 1:
    age = int(input("How old are you? "))
    userAge(age)
  elif randomQuestion == 2:
    userHobby()