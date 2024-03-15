from django.shortcuts import redirect, render


def validate(sqlData, userName, password, request):
    returnData={}
    if sqlData.mobileNumber == userName:
        if sqlData.password == password:
            return redirect("/profile/" + str(sqlData.id))
        else:
            returnData["passwordErrorMsg"] = "Incorrect Password"
            return render(request, "login.html", returnData)
    else:
        returnData["userErrorMsg"] = "Student Contact Number does Not exist"
        return render(request, "login.html", returnData)
