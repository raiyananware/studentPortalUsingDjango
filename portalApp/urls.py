from django.urls import include, path
from portalApp import views
from portalApp.creatingData import creatingCourseTopicAndSubTopic

urlpatterns = [
    path("login/", views.login),
    path("profile/", views.profile),
    path("topic/<topicId>", views.topics),
    path("topic/<topicId>/subTopic/<subTopicId>", views.subTopics),
    path("dashboard/", views.dashboard),
    path('topicId/<topicId>/subTopicId/<subTopicId>/attendedLecture/<lectureId>', views.markLectureCompleted),
    path('addUser/', views.addUser),
    path('logout/', views.logout),
    path('createBatchOrCourse/', views.createBatchOrCourse),
    path('createCourse/',views.createCourses),
    path('createBatch/', views.createBatch),
    path('manageStudent/',views.manageStudent),
    path('manageTeachers/', views.manageTeachers),
    path('deactivateUser/<id>/<isTeacher>',views.deactivateUsers),
    path('activateUser/<id>/<isTeacher>',views.activateUsers),
    path('removeUser/<id>/<isTeacher>',views.removeUser),
    path('updateUser/<isTeacher>', views.updateUsers),
    path('createData',creatingCourseTopicAndSubTopic.uploadData)
]
