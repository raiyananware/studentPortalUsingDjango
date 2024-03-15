from portalApp.models import lecture, classLectureCompleted, selfCompletedLecture
from django.db.models import Q


def getSelfCompletedLecture(studentId, subTopicId):
    q1 = Q(studentId=studentId)
    q2 = Q(subTopicId=subTopicId)
    return selfCompletedLecture.objects.filter(q1 & q2)
    

def getClassLectureCompleted(batchId, subTopicId):
    q1 = Q(batchId=batchId)
    q2 = Q(subTopicId=subTopicId)
    return classLectureCompleted.objects.filter(q1 & q2)


def getLectureById(id):
    return lecture.objects.get(lectureId=id)