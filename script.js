function updatePostureStatus(posture) {
    const postureMessage = document.getElementById('postureMessage');
    const postureContainer = document.getElementById('postureContainer');
    
    switch(posture) {
        case 'good':
            postureMessage.textContent = "Good Posture!";
            document.body.className = 'green';
            break;
        case 'bad':
            postureMessage.textContent = "Bad Posture! Please adjust your position.";
            document.body.className = 'red';
            break;
        case 'okay':
            postureMessage.textContent = "Okay Posture.";
            document.body.className = 'yellow';
            break;
        default:
            postureMessage.textContent = "Monitoring your posture...";
            document.body.className = ''; 
    }
}

setInterval(() => {
    const postures = ['good', 'bad', 'okay'];
    const randomPosture = postures[Math.floor(Math.random() * postures.length)];
    updatePostureStatus(randomPosture);
}, 3000);
