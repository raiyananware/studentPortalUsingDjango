from portalApp.models import course


def createCourse(courseName,courseTopicList):
    course.objects.create(courseName=courseName, courseTopicIds=courseTopicList)


def getCourseById(id):
    return course.objects.get(courseId=id)


def getAllCourses():
    tempList=[]
    data=course.objects.all()
    for eachData in data:
        tempDict={}
        tempDict['courseId']=eachData.courseId
        tempDict['courseName']=eachData.courseName
        tempList.append(tempDict)
    return tempList
