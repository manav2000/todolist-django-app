fetch('send_json/')
    .then(response => response.json())
    .then(data => console.log(data))