let intervalId; // Declare a variable to hold the interval ID
let seconds = 0; // Timer seconds
let timerStarted = false; // Flag to check if the timer has started

// Move this function to the top
function updatePostureStatus(posture) {
    const postureMessage = document.getElementById('postureMessage');
    const postureContainer = document.getElementById('postureContainer');
    const stopContainer = document.getElementById('stopContainer');

    switch (posture) {
        case 'good':
            postureMessage.textContent = "Good Posture!";
            postureContainer.className = 'green';
            postureMessage.style.color = 'white';
            stopContainer.style.display = 'block'; // Show stop button
            break;
        case 'bad':
            postureMessage.textContent = "Bad Posture! Please adjust your position.";
            postureContainer.className = 'red';
            postureMessage.style.color = 'white';
            stopContainer.style.display = 'block'; // Show stop button
            break;
        default:
            postureMessage.textContent = "Monitoring your posture...";
            postureContainer.className = ''; 
            postureMessage.style.color = 'black';
            stopContainer.style.display = 'none'; // Hide stop button
    }
}

document.getElementById('startButton').addEventListener('click', () => {
    const baseURL = "http://127.0.0.1:5000";
    
    document.getElementById('startContainer').style.display = 'none';
    document.getElementById('postureContainer').style.display = 'flex';
    document.getElementById('stopContainer').style.display = 'none'; // Ensure stop button is hidden

    // Simulate posture monitoring
    intervalId = setInterval(() => {
        fetch(baseURL + "/api/getPosture")
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log("Data received:", data); // Log the data for debugging
                if (data["status"] !== 200) {
                    console.log("Request unsuccessful, status not 200");
                } else {
                    updatePostureStatus(data["isGoodPosture"] === "TRUE" ? "good" : "bad");
                }
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }, 1000); // Change posture every 1.0 seconds
});

document.getElementById('stopButton').addEventListener('click', () => {
    clearInterval(intervalId); // Stop posture monitoring
    document.getElementById('postureContainer').style.display = 'none'; // Hide posture monitoring message
    document.getElementById('startContainer').style.display = 'flex'; // Show start button again
    document.getElementById('stopContainer').style.display = 'none'; // Hide stop button
});

document.getElementById("startButton").addEventListener("click", function() {
    fetch('/api/startMeasure')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
