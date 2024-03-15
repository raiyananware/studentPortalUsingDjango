from portalApp.models import  extendedUser
from django.contrib.auth.models import User

def updateUser(data, id, jobLocations):
    User.objects.filter(id=id).update(
        first_name=data["firstName"],
        last_name=data["lastName"],
        # email=data["email"],
    )
    extendedUser.objects.filter(userId=id).update(
        middleName=data["middleName"],
        dob=data["dob"],
        gender=data.get("gender"),
        # mobileNumber=data["mobileNumber"],
        address=data["address"],
        jobLocationSelected=jobLocations,
    )


def getUserByEmail(id):
    return student.objects.filter(email=id)


def UpdateBatchID(userId, batchId):
    extendedUser.objects.filter(userId=userId).update(batchId=batchId)


def getUserByMobileNumber(id):
    return student.objects.filter(mobileNumber=id)


def getUserById(id):
    return User.objects.get(id=id)


def getUser(id):
    tempData = {}
    userData = User.objects.filter(id=id)
    extendedUserData = extendedUser.objects.filter(userId=id)
    tempData["firstName"] = userData[0].first_name
    tempData["lastName"] = userData[0].last_name
    tempData["email"] = userData[0].email
    tempData["middleName"] = extendedUserData[0].middleName
    tempData["gender"] = extendedUserData[0].gender
    tempData["mobileNumber"] = extendedUserData[0].mobileNumber
    tempData["address"] = extendedUserData[0].address
    tempData["dob"] = extendedUserData[0].dob.strftime("%Y-%m-%d")
    tempData["jobLocationSelected"] = extendedUserData[0].jobLocationSelected
    tempData["batchId"] = extendedUserData[0].batchId.batchId
    return tempData


def deleteUser(id):
    extendedUser.objects.filter(userId=id).delete()
    User.objects.filter(id=id).delete()


def activateUser(id):
    User.objects.filter(id=id).update(is_active=True)


def deactivateUser(id):
    User.objects.filter(id=id).update(is_active=False)


def createUserData(UserList):
    tempUserList = []
    for eachUser in UserList:
        tempDict = {}
        eachUserData = extendedUser.objects.get(userId=eachUser.id)
        tempDict["id"] = eachUser.id
        tempDict["firstName"] = eachUser.first_name
        tempDict["lastName"] = eachUser.last_name
        tempDict["email"] = eachUser.email
        tempDict["isActive"] = eachUser.is_active
        tempDict["middleName"] = eachUserData.middleName
        tempDict["gender"] = eachUserData.gender
        tempDict["mobileNumber"] = eachUserData.mobileNumber
        tempDict["address"] = eachUserData.address
        tempDict["batchId"] = eachUserData.batchId.batchId
        tempUserList.append(tempDict)
    
    return tempUserList


def getStudents():
    tempUserList = []
    userData = User.objects.all()
    for eachUser in userData:
        if eachUser.is_superuser or eachUser.is_staff:
            continue
        else:
            tempUserList.append(eachUser)
    return createUserData(tempUserList)


def getTeachers():
    tempUserList = []
    userData = User.objects.all()
    for eachUser in userData:
        if eachUser.is_superuser or eachUser.is_staff != True:
            continue
        else:
            tempUserList.append(eachUser)
    return createUserData(tempUserList)


