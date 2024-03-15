from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class course(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=128)
    courseTopicIds = models.JSONField()


class batch(models.Model):
    batchId=models.AutoField(primary_key=True)
    batchName=models.CharField(max_length=128)
    courseId = models.ForeignKey(course, on_delete=models.CASCADE)


class extendedUser(models.Model):
    userId=models.ForeignKey(User,  on_delete=models.CASCADE, unique=True)
    middleName=models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    mobileNumber = models.BigIntegerField()
    address = models.CharField(max_length=256, null=True)
    gender = models.CharField(max_length=10, null=True)
    jobLocationSelected = models.CharField(max_length=256, null=True)
    batchId = models.ForeignKey(batch, on_delete=models.CASCADE, null=True)


class qualification(models.Model):
    studentID = models.ForeignKey(User,  on_delete=models.CASCADE, unique=True)
    highestQualification = models.CharField(max_length=20)
    university = models.CharField(max_length=50)
    yearOfPassing = models.IntegerField()
    score = models.DecimalField(max_digits=10, decimal_places=2)


class workingDetails(models.Model):
    studentID = models.ForeignKey(User,  on_delete=models.CASCADE, unique=True)
    fresher = models.BooleanField(default=True)
    working = models.BooleanField(default=False)
    companyName = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    startDate = models.DateField()
    lastDate = models.DateField()


class jobLocationAvailable(models.Model):
    location = models.CharField(max_length=20)


class qualificationAvailable(models.Model):
    qualificationName=models.CharField(max_length=100)


class topic(models.Model):
    topicId = models.AutoField(primary_key=True)
    topicName = models.CharField(max_length=256)
    selfLearningTopic = models.BooleanField(default=True)


class subTopic(models.Model):
    subTopicId = models.AutoField(primary_key=True)
    subTopicName = models.CharField(max_length=256)
    topicId = models.ForeignKey(topic, on_delete=models.CASCADE)


class lecture(models.Model):
    lectureId = models.AutoField(primary_key=True)
    lectureName = models.CharField(max_length=256)
    subTopicId = models.ForeignKey(subTopic, on_delete=models.CASCADE)


class selfCompletedLecture(models.Model):
    lectureId = models.ForeignKey(lecture, on_delete=models.CASCADE)
    subTopicId = models.ForeignKey(subTopic, on_delete=models.CASCADE)
    topicId = models.ForeignKey(topic, on_delete=models.CASCADE)
    studentId = models.ForeignKey(User,  on_delete=models.CASCADE)


class classLectureCompleted(models.Model):
    lectureId = models.ForeignKey(lecture, on_delete=models.CASCADE)
    subTopicId = models.ForeignKey(subTopic, on_delete=models.CASCADE)
    topicId = models.ForeignKey(topic, on_delete=models.CASCADE)
    batchId = models.ForeignKey(batch, on_delete=models.CASCADE)