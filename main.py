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
# create function that gets and stores API key of user
#New canvas object
canvas=Canvas(API_URL,API_KEY)
#SLL for holding assignments
CList=sllist()
user=canvas.get_current_user()
#load courses in SLL and print current courses
print("Please wait while we load your classes")
for Course in user.get_enrollments():
        active_courses=canvas.get_course(Course.course_id)
        CList.append(active_courses)
print("The current user is:")
print(canvas.get_current_user())
print("------------------------------")        
print("Enter number to show assignments for class")
print("Enter A to show assignemnts for all classes")
print("---------------------------------")
for i in range(CList.size):
        print(CList[i],end=" #")
        print(i)
assignID=input("Enter number next to class\n")
if assignID.isnumeric():
        try:
                temp=CList[int(assignID)].get_assignments()
                temp[0]
        except:
                print("There are no assignements for this class")
                exit
        for assignment in temp:
                tempassignvar=assignment
                print(tempassignvar, end="---")
                print("Due at",end=": ")
                print(tempassignvar.due_at)
else:
        for i in range(CList.size):
                temp=CList[i].get_assignments()
                print("Assignments in class:")
                print(CList[i])
                print("---------------------")
                for assignment in temp:
                        tempassignvar=assignment
                        print(tempassignvar, end="---")
                        print("Due at",end=": ")
                        print(tempassignvar.due_at)
exitTime=(time.time()-startTime)
print(exitTime)








