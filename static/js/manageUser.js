function toJson(data) {
  return JSON.parse(
    data
      .replace(/&#x27;/g, '"')
      .replace(/: True/g, ": true")
      .replace(/: False/g, ": false")
      .replace(/: None/g, ": null"),
  );
}

document.addEventListener("DOMContentLoaded", async () => {
  var i,
    j,
    userData = toJson(dictionaryData);
  for (i = 0; i < userData.length; i++) {
      var batch=document.getElementById('batchIdOfUser'+userData[i].id)
      for(j=0; j<batch.children.length;j++){
        if(batch.children[j].value==userData[i].batchId){
            batch.selectedIndex=j
        }
      }

  }
});
