from portalApp.models import selfCompletedLecture, classLectureCompleted
from django.db.models import Q


def addSelfCompletedLecture(lectureData, subtopicData, topicData, studentData):
    selfCompletedLecture.objects.create(
        lectureId=lectureData,
        subTopicId=subtopicData,
        topicId=topicData,
        studentId=studentData,
    )


def addClassCompletedLecture(lectureData, subtopicData, topicData, batchData):
    classLectureCompleted.objects.create(
        lectureId=lectureData,
        subTopicId=subtopicData,
        topicId=topicData,
        batchId=batchData,
    )


def getSelfCompletedLectureData(studentId, topicId=None, subTopicId=None):
    data = None
    q1 = Q(studentId=studentId)
    if (topicId == None) and (subTopicId == None):
        data = selfCompletedLecture.objects.filter(q1)
    elif (topicId != None) and (subTopicId == None):
        q2 = Q(topicId=topicId)
        data = selfCompletedLecture.objects.filter(q1 & q2)
    elif (topicId != None) and (subTopicId != None):
        q3 = Q(subTopicId=subTopicId)
        data = selfCompletedLecture.objects.filter(q1 & q2 & q3)
    return data


def getClassCompletedLectureData(batchId, topicId=None, subTopicId=None):
    data = None
    q1 = Q(batchId=batchId)
    q2 = Q(topicId=topicId)
    q3 = Q(subTopicId=subTopicId)
    if (topicId == None) and (subTopicId == None):
        data = classLectureCompleted.objects.filter(q1)
    elif (topicId != None) and (subTopicId == None):
        data = classLectureCompleted.objects.filter(q1 & q2)
    elif (topicId != None) and (subTopicId != None):
        data = classLectureCompleted.objects.filter(q1 & q2 & q3)
    return data
