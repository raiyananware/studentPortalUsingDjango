from portalApp.models  import topic, subTopic


def getAllTopics():
    tempList=[]
    data=topic.objects.all()
    for eachData in data:
        tempDict={}
        tempDict['topicId']=eachData.topicId
        tempDict['topicName']=eachData.topicName
        tempList.append(tempDict)
    return tempList

def getTopicById(id):
    return topic.objects.get(topicId=id)


def getSubTopicById(id):
    return subTopic.objects.get(subTopicId=id)
