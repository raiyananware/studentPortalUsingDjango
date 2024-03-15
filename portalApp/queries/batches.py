from portalApp.models import batch

def createBatch(batchName, courseId):
    batch.objects.create(batchName=batchName, courseId=courseId)


def getAllBatches():
    tempList=[]
    batchesData=batch.objects.all()
    for batches in batchesData:
        tempDict={}
        tempDict['batchId']=batches.batchId
        tempDict['batchName']=batches.batchName
        tempList.append(tempDict)
    return tempList


def getBatchByID(id):
    return batch.objects.get(batchId=id)


def getBatchesList():
    tempList=[]
    batchData=batch.objects.all()
    for eachBatch in batchData:
        tempList.append(eachBatch.batchId)
    
    return tempList



def getBatchByName(batchName):
    return batch.objects.filter(batchName=batchName)