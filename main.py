from re import A
from canvasapi import Canvas
import llist
from llist import sllist
import time
startTime=time.time()
#CANVAS API URL
API_URL="https://canvas.unf.edu"

#CANVAS API key
API_KEY="4502~fEGTycFhFVt7AJab3A0PhUnfo0L7cLv3W1uYWPbeb4LSlYqPe2tlyNoMdKGMRwb7"
# TODO:
# have program read from setup file 
# create function that prints all assignments

#New canvas object
canvas=Canvas(API_URL,API_KEY)
#SLL for holding assignments
AList=sllist()
user=canvas.get_current_user()
print("The current user is:")
print(user)
print("------------------------------")
print("Currently enrolled classes are")
print("------------------------------")
course=user.get_enrollments()
#load courses in SLL and print current courses
for Course in user.get_enrollments():
        active_courses=canvas.get_course(Course.course_id)
        AList.append(active_courses)
        print(active_courses)
print("--------------------------------")
print("Enter number to show assignments for class")
print("Enter A to show assignemnts for all classes")
print("---------------------------------")
for i in range(AList.size):
        print(AList[i],end=" #")
        print(i)
assignID=input("Enter number next to class\n")
if assignID.isnumeric():
        try:
                temp=AList[int(assignID)].get_assignments()
                temp[0]
        except:
                print("There are no assignements for this class")

        
        for assignment in temp:
         print(assignment)
else:
        print("TODO: Implmemnt all assignments")
exitTime=(time.time()-startTime)
print(exitTime)


