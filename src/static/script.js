function updatePostureStatus(posture) {
    const postureMessage = document.getElementById('postureMessage');
    const postureContainer = document.getElementById('postureContainer');

    switch(posture) {
        case 'TRUE':
            postureMessage.textContent = "Good Posture!";
            postureContainer.className = 'green';
            break;
        case 'FALSE':
            postureMessage.textContent = "Bad Posture! Please adjust your position.";
            postureContainer.className = 'red';
            break;
        default:
            postureMessage.textContent = "Monitoring your posture...";
            postureContainer.className = ''; 
    }
}

document.getElementById('startButton').addEventListener('click', () => {
    var baseUrl = "http://127.0.0.1:5000";
    
    document.getElementById('startContainer').style.display = 'none';
    document.getElementById('postureContainer').style.display = 'flex';
    
    setInterval(() => {
        fetch(baseURL + "/api/getPosture") .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        }) .then(data => {
            console.log(data); // Process the data from the response
            if(data["status"] != 200) {
                    console.log("GET REQUEST FAILED");
            } else {
                    updatePosture(data["isGoodPosture"]);
            }
        }) .catch(error => {
            console.error('GET REQUEST ERROR:', error); 
        });

    }, 3000);
});
