from django.db.models import Q
from portalApp.models import lecture, selfCompletedLecture, subTopic
from portalApp.queries.completedLecture import (
    getSelfCompletedLectureData,
    getClassCompletedLectureData,
)


def getSelfLearningPercentage(studentId):
    lectureData = getSelfCompletedLectureData(studentId)
    if lectureData == None:
        lectureData = 0
    lectureCount = lecture.objects.count()
    percentage = round((len(lectureData) / lectureCount) * 100)
    return percentage


def getClassLearningPercentage(courseId, lectureCount):
    lectureData = getClassCompletedLectureData(courseId)
    percentage = round((len(lectureData) / lectureCount) * 100)
    return percentage


def getClassLearningTopicPercentage(courseId, topicId, lectureCount):
    lectureData=getClassCompletedLectureData(courseId, topicId)
    percentage = round((len(lectureData) / lectureCount) * 100)
    return percentage
    
    
def getTopicCompletedPercentage(studentId, topicId):
    countOfLectures = 0
    q1 = Q(studentId=studentId)
    q2 = Q(topicId=topicId)
    subTopicData = subTopic.objects.filter(topicId=topicId)
    for topics in subTopicData:
        q3 = Q(subTopicId=topics.subTopicId)
        lectureData = lecture.objects.filter(q3)
        countOfLectures += len(lectureData)
    selfLectureCompleted = selfCompletedLecture.objects.filter(q1 & q2)
    percentage = round((len(selfLectureCompleted) / countOfLectures) * 100)
    return percentage
