document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();
    var videoURL = document.querySelector('input[name="videoURL"]').value;

    fetch('/download', {
        method: 'POST',
        body: new URLSearchParams({ 'videoURL': videoURL }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        var resultDiv = document.getElementById('result');
        if (data.success) {
            resultDiv.innerHTML = data.message;
        } else {
            resultDiv.innerHTML = 'Error: ' + data.message;
        }
    });
});
