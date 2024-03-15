from portalApp.models import qualification
from django.contrib.auth.models import User


def UpdateQualification(data, id):
    qualificationData = getQualification(id)
    if data["yearOfPassing"] == "---Select---":
        yearOfPassing = "0000-00-00"
    else:
        yearOfPassing = data["yearOfPassing"]
    if len(qualificationData) != 0:
        qualification.objects.filter(studentID=id).update(
            highestQualification=data.get("highestQualification"),
            university=data["university"],
            score=data["score"],
        )
        if data["yearOfPassing"] != "---Select---":
            qualification.objects.filter(studentID=id).update(
                yearOfPassing=data.get("yearOfPassing"),
            )

    else:
        studentData = User.objects.get(id=id)
        qualification.objects.create(
            studentID=studentData,
            highestQualification=data["highestQualification"],
            university=data["university"],
            yearOfPassing=yearOfPassing,
            score=data["score"],
        )
        if data["yearOfPassing"] != "---Select---":
            qualification.objects.filter(studentID=id).update(
                yearOfPassing=data.get("yearOfPassing"),
            )


def getQualification(id):
    return qualification.objects.filter(studentID=id)
