function postData(remainingUrl,data,token) {

    let url=`http://127.0.0.1:8000/${remainingUrl}`
//   fetch(url, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//       "X-CSRFToken":token
//     },
//     body: JSON.stringify(data),
//   })
    // .then((response) => {
    //   if (response.ok) {
    //     // location.reload(); // Refresh the page if response status is in the range 200-299
    //     // console.log("----Data Submitted")
    //     console.log(response)
    //   } else {
    //     console.error("Error:", response.status);
    //     console.log(response)
    //   }
    // })
    // .catch((error) => {
    //   console.error("Error:", error);
    // });


var xhr = new XMLHttpRequest();
// var url = `http://127.0.0.1:8000/${remainingUrl}`;
var data = JSON.stringify(data);

xhr.open('POST', url, true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.setRequestHeader('X-CSRFToken', token);

xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
        if (xhr.status === 200 || xhr.status === 201) {
            // console.log(xhr)
            location.reload(); // Refresh the page
        } else {
            console.error('Error:', xhr);
        }
    }
};

xhr.send(data);

}




