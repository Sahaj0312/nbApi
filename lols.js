fetch("http://127.0.0.1:5000/DAL")
    .then(res => res.json())
    .then(data => console.log(data))