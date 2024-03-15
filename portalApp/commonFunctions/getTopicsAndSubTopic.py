from portalApp.models import (
    course,
    subTopic,
    topic,
    selfCompletedLecture,
    lecture,
    classLectureCompleted,
)
from django.contrib.auth.models import User
from portalApp.queries.student import getUser


def getTopicsAndSubTopic(courseId, studentId):
    returnData = {"classLearning": [], "selfLearning": []}
    courseData = course.objects.get(courseId=courseId)
    for i in courseData.courseTopicIds:
        topicData = topic.objects.get(topicId=i)
        subTopicData = subTopic.objects.filter(topicId=i)
        topicDict = {"topicId": i}
        topicDict["title"] = topicData.topicName
        topicDict["subTopic"] = []
        for j in subTopicData:
            topicDict["subTopic"].append(j)
        if topicData.selfLearningTopic == False:
            returnData["classLearning"].append(topicDict)
        elif topicData.selfLearningTopic == True:
            returnData["selfLearning"].append(topicDict)
    return returnData


def getTopicData(id):
    topicData = topic.objects.get(topicId=id)
    return topicData.topicName


def getSubTopicData(topicId=None, subTopicId=None, studentId=None):
    studentData=getUser(studentId)
    returnData = []

    classLearningCompletionData = classLectureCompleted.objects.filter(
        batchId=studentData['batchId']
    )

    if classLearningCompletionData == None:
        classLearningCompletionData = []

    selfLearningCompletionData = selfCompletedLecture.objects.filter(
        studentId=studentId
    )

    if selfLearningCompletionData == None:
        selfLearningCompletionData = []

    if topicId != None and subTopicId == None:
        subTopicData = subTopic.objects.filter(topicId=topicId)

    elif topicId == None and subTopicId != None:
        subTopicData = subTopic.objects.filter(subTopicId=subTopicId)

    for subTopics in subTopicData:
        sampleSubTopicData = {}
        sampleSubTopicData["subTopicTitle"] = subTopics.subTopicName
        sampleSubTopicData["subTopicId"] = subTopics.subTopicId
        lectureData = lecture.objects.filter(subTopicId=subTopics.subTopicId)
        sampleSubTopicData["lectureList"] = []
        lectureList = []
        temporaryList = []

        for lectures in lectureData:
            temporaryData = {}
            temporaryData["lectureId"] = lectures.lectureId
            temporaryData["title"] = lectures.lectureName
            atLast = False

            for lect in classLearningCompletionData:
                if lect.lectureId.lectureId == lectures.lectureId:
                    temporaryData["classCompleted"] = True

            for lect in selfLearningCompletionData:
                if lect.lectureId.lectureId == lectures.lectureId:
                    temporaryData["selfCompleted"] = True
                    atLast = True

            if atLast:
                temporaryList.append(temporaryData)
            else:
                lectureList.append(temporaryData)

        sampleSubTopicData["lectureList"] = lectureList + temporaryList
        returnData.append(sampleSubTopicData)

    return returnData

def getTopicCount(id):
    subTopics=subTopic.objects.filter(topicId=id)
    count=0
    for subTop in subTopics:
        lectureCount=len(lecture.objects.filter(subTopicId=subTop.subTopicId))
        count+=lectureCount
    return count
