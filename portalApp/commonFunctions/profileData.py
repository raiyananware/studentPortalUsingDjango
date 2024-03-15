from portalApp.queries.student import getUser
from portalApp.queries.jobLocationAvailable import jobLocationList
from portalApp.queries.qualificationAvailable import qualificationList
from portalApp.queries.qualification import getQualification
from portalApp.queries.workingDetails import getWorkingDetails


def createProfileData(userId):
    sampleData = {"allData": {"jobLocationSelected": []}}
    sampleData["allData"]["jobLocationAvailable"] = jobLocationList()
    sampleData["allData"]["qualificationList"] = qualificationList()

    tempData = {}
    userData = getUser(userId)
    tempData["firstName"] = userData["firstName"]
    tempData["middleName"] = userData["middleName"]
    tempData["lastName"] = userData["lastName"]
    tempData["dob"] = userData["dob"]
    tempData["gender"] = userData["gender"]
    tempData["email"] = userData["email"]
    tempData["mobileNumber"] = userData["mobileNumber"]
    tempData["address"] = userData["address"]
    sampleData["allData"]["personalDetails"] = tempData

    tempData = {}
    workingDetails = getWorkingDetails(userId)
    if len(workingDetails) != 0:
        tempData["fresher"] = workingDetails[0].fresher
        tempData["working"] = workingDetails[0].working
        tempData["companyName"] = workingDetails[0].companyName
        tempData["designation"] = workingDetails[0].designation
        tempData["startDate"] = workingDetails[0].startDate.strftime("%Y-%m-%d")
        tempData["lastDate"] = workingDetails[0].lastDate.strftime("%Y-%m-%d")
    sampleData["allData"]["workDetails"] = tempData

    tempData = {}
    qualificationData = getQualification(userId)
    if len(qualificationData) != 0:
        tempData["highestQualification"] = qualificationData[0].highestQualification
        tempData["university"] = qualificationData[0].university
        tempData["yearOfPassing"] = qualificationData[0].yearOfPassing
        tempData["score"] = float(qualificationData[0].score)
    sampleData["allData"]["qualification"] = tempData

    if userData["jobLocationSelected"] != None:
        sampleData["allData"]["jobLocationSelected"] = userData["jobLocationSelected"].split(", ")
    else:
        sampleData["allData"]["jobLocationSelected"] = [
            "Select",
            "Select",
            "Select",
            "Select",
        ]

    sampleData["allData"]["yearList"] = []
    for i in range(2024, 2004, -1):
        sampleData["allData"]["yearList"].append(i)

    return sampleData
