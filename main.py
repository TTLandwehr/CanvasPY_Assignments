from canvasapi import Canvas
#CANVAS API URL
API_URL="https://canvas.unf.edu"

#CANVAS API key
API_KEY="4502~fEGTycFhFVt7AJab3A0PhUnfo0L7cLv3W1uYWPbeb4LSlYqPe2tlyNoMdKGMRwb7"
# TODO:
# create LL that holds course object
# print assignments after storing objects in LL

#New canvas object
canvas=Canvas(API_URL,API_KEY)
user=canvas.get_current_user()
print("The current user is:")
print(user)
print("------------------------------")
print("Currently enrolled classes are")
print("------------------------------")
course=user.get_enrollments()
for Course in user.get_enrollments():
        course_id=Course.course_id
        active_courses=canvas.get_course(course_id)
        print(active_courses)
print("--------------------------------")


