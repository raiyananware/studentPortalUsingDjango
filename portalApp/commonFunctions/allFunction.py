from django.db.models import Q
from django.contrib.auth.models import User

print()
#--------------------------- Models
from portalApp.models import (
    topic,
    subTopic,
    lecture,
    selfCompletedLecture,
    extendedUser,
    batch,
    qualification,
    workingDetails,
    jobLocationAvailable,
    course,
    classLectureCompleted,
)

print()
#--------------------------- Topic and Sub Topic
from portalApp.commonFunctions.getTopicsAndSubTopic import (
    getTopicsAndSubTopic,
    getTopicData,
    getSubTopicData,
    getTopicCount,
)
print()
#--------------------------- lecture Details
from portalApp.commonFunctions.getLectureDetails import (
    getSelfLearningPercentage,
    getTopicCompletedPercentage,
    getClassLearningPercentage,
    getClassLearningTopicPercentage,
)
print()
#--------------------------- student
from portalApp.queries.student import (
    updateUser,
    getUser,
    getUserByEmail,
    getUserByMobileNumber,
    getUserById,
    getStudents,
    getTeachers,
    deleteUser,
    activateUser,
    deactivateUser,
    UpdateBatchID
)
print()
#--------------------------- batches
from portalApp.queries.batches import (
    getAllBatches,
    createBatch,
    getBatchByName,
    getBatchByID,
    getBatchesList
)
print()
#--------------------------- Topic and Sub Topic
from portalApp.queries.topicAndSubTopic import (
    getAllTopics,
    getSubTopicById,
    getTopicById,
)
print()
#--------------------------- Completed Lecture
from portalApp.queries.completedLecture import (
    addSelfCompletedLecture,
    addClassCompletedLecture,
)
print()
#--------------------------- Lectures
from portalApp.queries.lectures import (
    getLectureById
)
print()
#--------------------------- shortcuts
from django.shortcuts import (
    redirect, 
    render, 
    HttpResponse
)
print()
#--------------------------- Verify User
from portalApp.commonFunctions.verifyUser import (
    verifyUser
)
print()
#--------------------------- Qualification
from portalApp.queries.qualification import (
    UpdateQualification
)
print()
#--------------------------- workingDetails
from portalApp.queries.workingDetails import (
    updateWorkingDetails
)
print()
#--------------------------- Job Location
from portalApp.queries.jobLocationAvailable import (
    jobLocationList
)
print()
#--------------------------- Profile Data
from portalApp.commonFunctions.profileData import (
    createProfileData
)


#--------------------------- Qualification Available
from portalApp.queries.qualificationAvailable import (
    qualificationList
)


#--------------------------- Courses
from portalApp.queries.courses import (
    getAllCourses, 
    getCourseById, 
    createCourse
)


#--------------------------- Contrib Auth
from django.contrib.auth import (
    authenticate, 
    login as auth_login, 
    logout as auth_logout
)