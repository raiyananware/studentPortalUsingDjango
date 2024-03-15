from portalApp.models import qualificationAvailable

def qualificationList():
    qualifications=[]
    qualificationData=qualificationAvailable.objects.all()
    for qualification in qualificationData:
        qualifications.append(qualification.qualificationName)
    return qualifications
