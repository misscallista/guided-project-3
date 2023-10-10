const express = require('express')
const pickle = require('pickle')
const { PythonShell } = require('python-shell')
const bodyParser = require('body-parser')

const app = express()
const port = 3001
app.listen(port, () => console.log(`Server is listening on ${port}`))


// let pyshell = new PythonShell('script.py');

// pyshell.send(run_model(data));

const spawn = require("child_process").spawn;
const pythonProcess = spawn('python',["path/to/script.py", 'troop_movements10m.csv']);