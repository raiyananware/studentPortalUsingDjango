let listOfElements = [
    "firstName",
    "middleName",
    "lastName",
    "address",
    "dob",
    "gender",
    "jobLocations1",
    "jobLocations2",
    "jobLocations3",
    "jobLocations4",
    "university",
    "highestQualification",
    "yearOfPassing",
    "score",
    "companyName",
    "designation",
    "startDate",
    "lastDate",
  ],
  userID,
  numbersOfJobLocationDropDown;

function toJson(data) {
  return JSON.parse(
    data
      .replace(/&#x27;/g, '"')
      .replace(/: True/g, ": true")
      .replace(/: False/g, ": false")
      .replace(/: None/g, ": null"),
  );
}

function changeToEdit(tagName) {
  tagName.removeAttribute("class");
  if (tagName.getAttribute("readonly") != null) {
    tagName.classList.add("editInput");
    tagName.removeAttribute("readonly");
  } else if (tagName.getAttribute("disabled") != null) {
    tagName.classList.add("dropDown");
    tagName.removeAttribute("disabled");
  }
}

function changeToReadOnly() {
  window.location.reload();
}

function getValueOfElement(elementID) {
  return document.getElementById(elementID).value;
}

function edit() {
  // var jsonData = toJson(dictionaryData);

  for (i = 0; i < listOfElements.length; i++) {
    changeToEdit(document.getElementById(listOfElements[i]));
  }
  document.getElementById("saveEdit").removeAttribute("hidden");
  document.getElementById("cancelEdit").removeAttribute("hidden");
  document.getElementById("editBtn").setAttribute("hidden", "hidden");
}

document.addEventListener("DOMContentLoaded", async () => {
  
  var jsonData = toJson(dictionaryData);
  var i,
    j,
    k,
    gender = document.getElementById("gender"),
    optionForGender = gender.children,
    qualification = document.getElementById("highestQualification"),
    optionsForQualification = qualification.children,
    yearOfPassing = document.getElementById("yearOfPassing"),
    optionForYearOfPassing = yearOfPassing.children,
    jobLocation = document.getElementsByClassName("jobLocations"),
    fresher = document.getElementById("fresher"),
    working = document.getElementById("working");


  fresher.checked = jsonData.workDetails.fresher;
  working.checked = jsonData.workDetails.working;

  for (i = 0; i < optionForGender.length; i++) {
    if (optionForGender[i].value == jsonData.personalDetails.gender) {
      gender.selectedIndex = i;
      break;
    }
  }

  for (i = 0; i < optionsForQualification.length; i++) {
    if (
      optionsForQualification[i].value ==
      jsonData.qualification.highestQualification
    ) {
      qualification.selectedIndex = i;
      break;
    }
  }

  for (i = 0; i < optionForYearOfPassing.length; i++) {
    if (
      optionForYearOfPassing[i].value == jsonData.qualification.yearOfPassing
    ) {
      yearOfPassing.selectedIndex = i;
      break;
    }
  }

  for (j = 0; j < jobLocation.length; j++) {
    for (k = 0; k < jobLocation[i].children.length; k++) {
      if (jobLocation[j].children[k].value == jsonData.jobLocationSelected[j]) {
        jobLocation[j].selectedIndex = k;
      }
    }
  }

  // userID = window.location.href.charAt(window.location.href.length - 1);
});
