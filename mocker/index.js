const express = require('express')
const app = express()

app.get('/', function (req, res) {

    function myFunc(arg) {
        data = [];
        for (var i=0; i<100000;i++){
            var i_str = i.toString();
            data.push("id" + i_str);
        }

        res.status(200).end(JSON.stringify(data));
    }
    setTimeout(myFunc, 5000, 'timeout');
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))