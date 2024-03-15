from portalApp.models import jobLocationAvailable

def jobLocationList():
    locations=[]
    jobData=jobLocationAvailable.objects.all()
    for location in jobData:
        locations.append(location.location)
    return locations
