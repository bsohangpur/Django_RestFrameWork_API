
const res = fetch('http://127.0.0.1:8000/api/data/projects/3')           //api for the get request
    .then(response => response.json())
    .then(data => {return data});


console.log(res)
