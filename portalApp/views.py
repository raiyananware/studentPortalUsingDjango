from portalApp.commonFunctions import allFunction as functions


def logout(request):
    functions.auth_logout(request)
    return functions.redirect("/login/")


def dashboard(request):
    verified = functions.verifyUser(request)
    if verified:
        if request.user.is_staff == False:
            topicCount = 0
            dataFromSql = {}
            id = request.user.id
            studentData = functions.getUser(id)
            batchData = functions.getBatchByID(studentData["batchId"])
            selfLearningPercentage = functions.getSelfLearningPercentage(id)
            # classLearningPercentage = getClassLearningPercentage(batchData.batchId)
            courseData = functions.getTopicsAndSubTopic(batchData.courseId.courseId, id)

            for i in courseData["classLearning"]:
                topicCount += functions.getTopicCount(i["topicId"])
                i["percentage"] = functions.getTopicCompletedPercentage(id, i["topicId"])

            if request.user.is_staff == False:
                for i in courseData["selfLearning"]:
                    i["percentage"] = functions.getTopicCompletedPercentage(id, i["topicId"])
                dataFromSql["selfLearning"] = courseData["selfLearning"]

            classLearningPercentage = functions.getClassLearningPercentage(
                batchData.batchId, topicCount
            )

            dataFromSql["classLearning"] = courseData["classLearning"]
            dataFromSql["classLearningPercentage"] = classLearningPercentage
            dataFromSql["selfLearningPercentage"] = selfLearningPercentage
            dataFromSql["overallLearningPercentage"] = round(
                (classLearningPercentage + selfLearningPercentage) / 2
            )

        elif request.user.is_staff == True:
            topicCount = 0
            dataFromSql = {}
            id = request.user.id
            studentData = functions.getUser(id)
            batchData = functions.getBatchByID(studentData["batchId"])
            # selfLearningPercentage = getSelfLearningPercentage(id)
            # classLearningPercentage = getClassLearningPercentage(batchData.batchId, topicCount)
            courseData = functions.getTopicsAndSubTopic(batchData.courseId.courseId, id)

            for i in courseData["classLearning"]:
                tempTopicCount = functions.getTopicCount(i["topicId"])
                topicCount += tempTopicCount
                i["percentage"] = functions.getClassLearningTopicPercentage(
                    batchData.batchId, i["topicId"], tempTopicCount
                )

            classLearningPercentage = functions.getClassLearningPercentage(
                batchData.batchId, topicCount
            )

            dataFromSql["classLearning"] = courseData["classLearning"]
            dataFromSql["classLearningPercentage"] = classLearningPercentage
            dataFromSql["overallLearningPercentage"] = classLearningPercentage

        return functions.render(request, "dashboard.html", dataFromSql)
    else:
        return functions.redirect("/logout/")


def addUser(request):
    getVerificationOfUser = functions.verifyUser(request)
    context = {}
    if getVerificationOfUser and request.user.is_superuser:
        if request.method == "POST":
            isTeacher = False
            isAdmin = False
            isActive = True
            gender = request.POST.get("gender")
            firstName = request.POST["firstName"]
            lastName = request.POST["lastName"]
            email = request.POST["email"]
            password = request.POST["password"]
            role = request.POST.get("role")
            mobileNumber = request.POST["mobileNumber"]
            dob = request.POST["dob"]
            batchId = request.POST.get("batch")

            if batchId == "select":
                batchId = 1
            else:
                batchData = functions.getBatchByID(batchId)
            if role == "Teacher":
                isTeacher = True
            elif role == "Admin":
                isAdmin = True

            q1 = functions.Q(password=password)
            q2 = functions.Q(first_name=firstName)
            q3 = functions.Q(last_name=lastName)
            q4 = functions.Q(email=email)
            q5 = functions.Q(is_staff=isTeacher)
            q6 = functions.Q(is_active=isActive)
            q7 = functions.Q(is_superuser=isAdmin)
            data = functions.User.objects.filter(q2 & q3 & q4 & q5 & q6 & q7)

            if len(data) == 0:
                a = functions.User.objects.create(
                    password=password,
                    first_name=firstName,
                    last_name=lastName,
                    username=email,
                    email=email,
                    is_staff=isTeacher,
                    is_active=isActive,
                    is_superuser=isAdmin,
                )
                a.set_password(password)
                a.save()
                dataUser = functions.User.objects.filter(q2 & q3 & q4 & q5 & q6 & q7)
                userData = functions.User.objects.filter(id=dataUser[0].id)
                functions.extendedUser.objects.create(
                    userId=userData[0],
                    mobileNumber=mobileNumber,
                    dob=dob,
                    batchId=batchData,
                    gender=gender,
                )
                context["successMessage"] = "User Added Successfully"
                return functions.render(request, "addUser.html", context)
            else:
                getBatch = functions.batch.objects.all()
                context["batchData"] = getBatch
                context["errorMessage"] = "User already exist"
                return functions.render(request, "addUser.html", context)
        else:
            getBatch = functions.batch.objects.all()
            context["batchData"] = getBatch
            return functions.render(request, "addUser.html", context)
    else:
        return functions.redirect("/logout/")


def profile(request):
    getVerificationOfUser = functions.verifyUser(request)
    if getVerificationOfUser:
        if request.method == "POST":
            jobLocationSelected = [
                request.POST.get("jobLocation1"),
                request.POST.get("jobLocation2"),
                request.POST.get("jobLocation3"),
                request.POST.get("jobLocation4"),
            ]

            jobLocationSelectedString = ", ".join(jobLocationSelected)
            functions.updateUser(request.POST, request.user.id, jobLocationSelectedString)
            functions.UpdateQualification(request.POST, request.user.id)
            functions.updateWorkingDetails(request.POST, request.user.id)
            return functions.redirect("/profile/")
        else:
            returnData = functions.createProfileData(request.user.id)
            return functions.render(request, "profile.html", returnData)
    else:
        return functions.redirect("logout")


def login(request):
    context = {}
    if request.method == "POST":
        userName = request.POST["userName"]
        password = request.POST["password"]

        if userName.isdigit():
            userName = int(userName)

        if isinstance(userName, int) == True:
            getExtendedUserData = functions.extendedUser.objects.filter(mobileNumber=userName)
            userEmail = getExtendedUserData[0].userId.username
            userData = functions.User.objects.filter(username=userEmail)
            auth = functions.authenticate(username=userEmail, password=password)

        else:
            userData = functions.User.objects.filter(username=userName)
            auth = functions.authenticate(username=userName, password=password)
        

        if userData[0].is_active:
            if auth is not None:
                functions.auth_login(request, auth)
                if userData[0].is_superuser:
                    return functions.redirect("/addUser/")
                else:
                    return functions.redirect("/dashboard/")
            else:
                return functions.redirect("/login/")
        else:
            context={}
            context['errorMsg']="Your Account is Disabled"
            return functions.render(request, "login.html", context)

    else:
        return functions.render(request, "login.html")


def topics(request, topicId):
    getVerificationOfUser = functions.verifyUser(request)
    if getVerificationOfUser:
        studentId = request.user.id
        content = {}
        content["topicName"] = functions.getTopicData(topicId)
        content["topicId"] = topicId
        content["subTopics"] = functions.getSubTopicData(topicId, None, studentId)
        content["userId"] = studentId
        return functions.render(request, "topic.html", content)
    else:
        return functions.redirect("/logout/")


def subTopics(request, topicId, subTopicId):
    getVerificationOfUser = functions.verifyUser(request)
    if getVerificationOfUser:
        studentId = request.user.id
        id = request.user.id
        content = {}
        content["topicName"] = functions.getTopicData(topicId)
        content["topicId"] = topicId
        content["subTopics"] = functions.getSubTopicData(None, subTopicId, studentId)
        content["userId"] = studentId
        return functions.render(request, "topic.html", content)
    else:
        return functions.redirect("/logout/")


def markLectureCompleted(request, topicId, subTopicId, lectureId):
    getVerificationOfUser = functions.verifyUser(request)
    if getVerificationOfUser:
        if request.user.is_staff:
            data = functions.markClassLectureCompleted(request, topicId, subTopicId, lectureId)
        else:
            data = functions.markSelfLectureCompleted(request, topicId, subTopicId, lectureId)
        return data
    else:
        return functions.redirect("/logout/")


def markSelfLectureCompleted(request, topicId, subTopicId, lectureId):
    studentId = request.user.id
    q1 = functions.Q(studentId=studentId)
    q2 = functions.Q(lectureId=lectureId)
    getLectureData = functions.selfCompletedLecture.objects.filter(q1 & q2)
    if len(getLectureData) == 0:
        functions.addSelfCompletedLecture(
            functions.getLectureById(lectureId),
            functions.getSubTopicById(subTopicId),
            functions.getTopicById(topicId),
            functions.getUserById(studentId),
        )

    return functions.redirect("/topic/" + topicId + "/subTopic/" + subTopicId)


def markClassLectureCompleted(request, topicId, subTopicId, lectureId):
    userData = functions.getUser(request.user.id)
    q1 = functions.Q(batchId=userData["batchId"])
    q2 = functions.Q(lectureId=lectureId)
    getLectureData = functions.classLectureCompleted.objects.filter(q1 & q2)
    if len(getLectureData) == 0:
        functions.addClassCompletedLecture(
            functions.getLectureById(lectureId),
            functions.getSubTopicById(subTopicId),
            functions.getTopicById(topicId),
            functions.getBatchByID(userData["batchId"]),
        )
    return functions.redirect("/topic/" + topicId + "/subTopic/" + subTopicId)


def createBatchOrCourse(request):
    verified = functions.verifyUser(request)
    if verified and request.user.is_superuser:
        context = {}
        context["topics"] = functions.getAllTopics()
        context["courses"] = functions.getAllCourses()
        return functions.render(request, "createBatchOrCourse.html", context)

    else:
        return functions.redirect("/logout/")


def createCourses(request):
    verified = functions.verifyUser(request)
    if verified and request.user.is_superuser:
        element_values = []
        courseName = request.POST["courseName"]
        for key in request.POST.keys():
            if key.startswith("selectOption"):
                value = request.POST[key]
                element_values.append(value)

        functions.createCourse(courseName, element_values)
        return functions.redirect("/createBatchOrCourse/")
    else:
        return functions.redirect("/logout/")


def createBatch(request):
    verified = functions.verifyUser(request)
    if verified and request.user.is_superuser:
        batchName = request.POST["batchName"]
        courseId = request.POST.get("courseId")
        batches = functions.getBatchByName(batchName)
        if len  (batches) ==0:
            courses = functions.getCourseById(courseId)
            functions.createBatch(batchName, courses)
        else:
            return functions.HttpResponse("Batch with the Same name already exist")

        return functions.redirect("/createBatchOrCourse/")
    else:
        return functions.redirect("/logout/")


def manageStudent(request):
    verified = functions.verifyUser(request)
    if verified and request.user.is_superuser:
        context = {}
        context["users"] = functions.getStudents()
        context["batches"] = functions.getBatchesList()
        return functions.render(request, "manageUser.html", context)
    else:
        return functions.redirect("/logout/")


def manageTeachers(request):
    verified = functions.verifyUser(request)
    if verified and request.user.is_superuser:
        context = {}
        context["users"] = functions.getTeachers()
        context["batches"] = functions.getBatchesList()
        context["isTeacher"] = True
        return functions.render(request, "manageUser.html", context)
    else:
        return functions.redirect("/logout/")


def activateUsers(request, id, isTeacher):
    verified = functions.verifyUser(request)
    if verified and request.user.is_superuser:
        functions.activateUser(id)
        if isTeacher == "1":
            return functions.redirect("/manageTeachers/")
        else:
            return functions.redirect("/manageStudent/")
    else:
        return functions.render("/logout/")


def deactivateUsers(request, id, isTeacher):
    verified = functions.verifyUser(request)
    if verified and request.user.is_superuser:
        functions.deactivateUser(id)
        if isTeacher == "1":
            return functions.redirect("/manageTeachers/")
        else:
            return functions.redirect("/manageStudent/")
    else:
        return functions.render("/logout/")


def removeUser(request, id, isTeacher):
    verified = functions.verifyUser(request)
    if verified and request.user.is_superuser:
        functions.deleteUser(id)
        if isTeacher == "1":
            return functions.redirect("/manageTeachers/")
        else:
            return functions.redirect("/manageStudent/")
    else:
        return functions.render("/logout/")


def updateUsers(request, isTeacher):
    verified = functions.verifyUser(request)
    if verified and request.user.is_superuser:
        if isTeacher == "1":
            data = functions.getTeachers()
        else:
            data = functions.getStudents()
        for eachData in data:
            functions.UpdateBatchID(
                eachData["id"], request.POST["batchIdOfUser" + str(eachData["id"])]
            )
        if isTeacher == "1":
            return functions.redirect("/manageTeachers/")
        else:
            return functions.redirect("/manageStudent/")
    else:
        return functions.redirect("/logout/")


