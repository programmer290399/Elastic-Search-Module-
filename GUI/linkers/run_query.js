function run_query() {
var python = require("python-shell")
var path = require("path")

var query = document.getElementById("query").value
document.getElementById("query").value = "wait...";

let options = {
    mode: 'text',
    pythonPath: 'C:/Users/SAAHIL/AppData/Local/Programs/Python/Python37/python.exe',
    //pythonOptions: ['-u'], // get print results in real-time
    scriptPath: 'H:/rps/python/GUI/Electron-JS/electron-quick-start/engine/',
    args: [query]
  };


python.PythonShell.run('run_query.py', options, function (err, results) {
    if (err) throw err;
    swal(results[0]);
  });
}

