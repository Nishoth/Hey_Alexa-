function sendCommand() {
    const command = document.getElementById('commandInput').value;

    fetch('/process_command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ command })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.response;
    });
}
