const express = require('express');
const connect = require('./config/database');
const app = express();
const PORT = 3000;

app.listen(PORT,  async()=>{
    console.log(`Server Started at ${PORT}`);
    await connect();
    console.log("MongoDB connected!");
});