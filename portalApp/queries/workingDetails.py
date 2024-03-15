from portalApp.models import workingDetails
from django.contrib.auth.models import User


def updateWorkingDetails(data, id):
    workingData = getWorkingDetails(id)
    if data.get("working") == "on":
        working = True
    else:
        working = False
    if data.get("fresher") == "on":
        fresher = True
    else:
        fresher = False

    if len(workingData) != 0:
        workingData.update(
            fresher=fresher,
            working=working,
            companyName=data["companyName"],
            designation=data["designation"],
            startDate=data["startDate"],
            lastDate=data["lastDate"],
        )
    else:
        studentData = User.objects.get(id=id)
        workingDetails.objects.create(
            studentID=studentData,
            fresher=fresher,
            working=working,
            companyName=data["companyName"],
            designation=data["designation"],
            startDate=data["startDate"],
            lastDate=data["lastDate"],
        )


def getWorkingDetails(id):
    return workingDetails.objects.filter(studentID=id)
