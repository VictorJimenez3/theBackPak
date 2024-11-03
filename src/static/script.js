let intervalId; // Declare a variable to hold the interval ID
let timerId; // Declare a variable for the timer interval
let seconds = 0; // Timer seconds
let timerStarted = false; // Flag to check if the timer has started

function updatePostureStatus(posture) {
    const postureMessage = document.getElementById('postureMessage');
    const postureContainer = document.getElementById('postureContainer');
    const stopContainer = document.getElementById('stopContainer');
    const timer = document.getElementById('timer');

    switch (posture) {
        case 'good':
            postureMessage.textContent = "Good Posture!";
            postureContainer.className = 'green';
            postureMessage.style.color = 'white';
            stopContainer.style.display = 'block'; // Show stop button
            timer.style.display = 'block'; // Show timer when posture is good
            break;
        case 'bad':
            postureMessage.textContent = "Bad Posture! Please adjust your position.";
            postureContainer.className = 'red';
            postureMessage.style.color = 'white';
            stopContainer.style.display = 'block'; // Show stop button
            timer.style.display = 'block'; // Show timer when posture is bad
            break;
        default:
            postureMessage.textContent = "Monitoring your posture...";
            postureContainer.className = ''; 
            postureMessage.style.color = 'black';
            stopContainer.style.display = 'none'; // Hide stop button
            timer.style.display = 'none'; // Hide timer when monitoring posture
    }
}

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${String(minutes).padStart(2, '0')} min : ${String(secs).padStart(2, '0')} sec`; // Format to 00 min : 00 sec
}

function startTimer() {
    if (!timerStarted) { // Start timer only if it hasn't been started yet
        seconds = 0; // Reset seconds
        document.getElementById('timer').textContent = formatTime(seconds); // Reset timer display
        timerId = setInterval(() => {
            seconds++;
            document.getElementById('timer').textContent = formatTime(seconds); // Update timer display
        }, 1000); // Update every second
        timerStarted = true; // Set the flag to true
    }
}

document.getElementById('startButton').addEventListener('click', () => {
    document.getElementById('startContainer').style.display = 'none';
    document.getElementById('postureContainer').style.display = 'flex';
    document.getElementById('stopContainer').style.display = 'none'; // Ensure stop button is hidden
    document.getElementById('timer').style.display = 'none'; // Hide timer initially

    // Start timer when posture monitoring starts
    startTimer();
    
    // Simulate posture monitoring
    intervalId = setInterval(() => {
        const postures = ['good', 'bad'];
        const randomPosture = postures[Math.floor(Math.random() * postures.length)];
        updatePostureStatus(randomPosture);
    }, 3000); // Change posture every 3 seconds for demo purposes
});

document.getElementById('stopButton').addEventListener('click', () => {
    clearInterval(intervalId); // Stop posture monitoring
    clearInterval(timerId); // Stop the timer
    document.getElementById('postureContainer').style.display = 'none'; // Hide posture monitoring message
    document.getElementById('startContainer').style.display = 'flex'; // Show start button again
    document.getElementById('stopContainer').style.display = 'none'; // Hide stop button
    document.getElementById('timer').style.display = 'none'; // Hide timer
    seconds = 0; // Reset seconds
    timerStarted = false; // Reset timer flag
});
