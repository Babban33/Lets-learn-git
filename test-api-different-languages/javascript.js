fetch('http://127.0.0.1:8000/hello/Atharva', {
    method: 'GET',
    headers: {
        'Accept': 'application/json'
    }
})
.then(response => response.json())  // Convert response to JSON
.then(data => console.log(data))  // Log the response data
.catch(error => console.error('Error:', error));  // Handle errors
