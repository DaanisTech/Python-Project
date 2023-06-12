print("welcome to my quiz game! ")

playing =input("Do you want play? ")

if playing .lower() != "yes":
##for turning upper case to lower case if user enters upper cases##
    quit()

print("okay! lets play :)")
score =0

print("Question-1")
answer = input("what is cpu stands for? ").lower()
if answer == "central processing unit":
    print("correct")
    score +=1
else:
    print("incorrect")


print("Question-2")
answer = input("what is psu stands for? ").lower()
if answer == "power supply unit":
    print("correct")
    score +=1
else:
    print("incorrect")


print("Question-3")
answer = input("what is gpu stands for? ").lower()
if answer == "graphics processing unit":
    print("correct")
    score +=1
else:
    print("incorrect")


print("Question-4")
answer = input("what is RAM stands for? ").lower()
if answer == "random access memory":
    print("correct")
    score +=1
else:
    print("incorrect")


more = input("Do you want continue? ")
if more.lower() != "yes":
    quit()

print("okay! lets continue")


print("Question-5")
answer = input("what is IC stands for? ").lower()
if answer == "Integrated chip":
    print("correct")
    score +=1
else:
    print("incorrect")

print("you got " + str(score) + "question corrected")
