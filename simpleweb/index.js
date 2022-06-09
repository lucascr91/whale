const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send("Hi there, welcome to my assignment");
});

app.listen(8080, ()=> {
    console.log("Server is listening on port 8080");
})