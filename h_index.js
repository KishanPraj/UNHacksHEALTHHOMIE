const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();

app.use(bodyParser.json());
app.use(cors()); // Enable CORS for all routes

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));



app.listen(3000, () => console.log('Server running on http://localhost:3000'));
