let intervalId; // Declare a variable to hold the interval ID
let timerId; // Declare a variable for the timer interval
let seconds = 0; // Timer seconds
let timerStarted = false; // Flag to check if timer has started

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
    return `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`; // Format to 00:00
}

function startTimer() {
    if (!timerStarted) { // Start timer only if it hasn't been started yet
        seconds = 0; // Reset seconds
        document.getElementById('timer').textContent = `Time: ${formatTime(seconds)}`; // Reset timer display
        timerId = setInterval(() => {
            seconds++;
            document.getElementById('timer').textContent = `Time: ${formatTime(seconds)}`; // Update timer display
        }, 1000); // Update every second
        timerStarted = true; // Set the flag to true
    }
}

document.getElementById('startButton').addEventListener('click', () => {
    document.getElementById('startContainer').style.display = 'none';
    document.getElementById('postureContainer').style.display = 'flex';
    document.getElementById('stopContainer').style.display = 'none'; // Ensure stop button is hidden
    document.getElementById('timer').style.display = 'none'; // Hide timer initially

    intervalId = setInterval(() => {
        const postures = ['good', 'bad'];
        const randomPosture = postures[Math.floor(Math.random() * postures.length)];
        updatePostureStatus(randomPosture);
        startTimer(); // Start the timer only once
    }, 3000);
});

document.getElementById('stopButton').addEventListener('click', () => {
    clearInterval(intervalId); // Stop the posture monitoring interval
    clearInterval(timerId); // Stop the timer
    document.getElementById('postureContainer').style.display = 'none'; // Hide posture monitoring message
    document.getElementById('stopContainer').style.display = 'none'; // Hide stop button
    document.getElementById('startContainer').style.display = 'flex'; // Show start button again
    document.getElementById('timer').style.display = 'none'; // Hide timer on stop
    timerStarted = false; // Reset the flag when stopped
});
