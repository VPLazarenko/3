
document.getElementById('save-button').addEventListener('click', () => {
    const assistantName = document.getElementById('assistant-name').value;
    const instructions = document.getElementById('instructions').value;
    const newFunction = document.getElementById('new-function').value;
    const codeChanges = document.getElementById('code-changes').value;

    fetch('/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            assistantName,
            instructions,
            newFunction,
            codeChanges,
        }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
