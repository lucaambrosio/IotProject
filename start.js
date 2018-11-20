var spawn = require('child_process').spawn,
    py = spawn('python', ['code.py']),
    data = 7;

py.stdout.on('data', function (data) {

    console.log('LOOK', data.toString());
});
py.stdin.write(JSON.stringify(data));
py.stdin.end();










