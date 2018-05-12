const express = require('express')
const app = express()

app.get('/uniprot', function (req, res) {

    function myFunc(arg) {
        data = new Array();
        for (var i=0; i<100;i++){
            var i_str = i.toString();
            data.push("id" + i_str);
        }
        res.status(200).end(JSON.stringify(data));
    }
    setTimeout(myFunc, 2000, 'timeout');
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))