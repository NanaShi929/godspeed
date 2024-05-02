var express = require("express");
var mong = require("mongodb").MongoClient;
var cors = require("cors");
var bp = require("body-parser");

var app = express();
app.use(cors());
app.use(bp.json());
var url = "mongodb://127.0.0.1:27017/";

app.post("/insert", function (req, res) {
    mong.connect(url, function (err, db) {
        var dat = {
            rollno: req.body.rollno,
            name: req.body.name,
            sub: req.body.sub,
        };
        if (err) throw err;
        var dbo = db.db("College22");
        dbo.collection("student").insertOne(dat, function (err, recs) {
            if (err) throw err;
            console.log(`rec with ${recs.insertedId} inserted`);
            db.close();
        });
    });
});

app.get("/fetchrecs", function (req, res) {
    mong.connect(url, function (err, db) {
        //  var dat={empno:req.body.empno,empname:req.body.empname,dept:req.body.dept}
        if (err) throw err;
        var dbo = db.db("College22");
        dbo
            .collection("student")
            .find()
            .toArray(function (err, recs) {
                if (err) throw err;
                res.send(recs);
                db.close();
            });
    });
});

// Route for deleting a document
app.delete("/delete", function (req, res) {
    mong.connect(url, function (err, db) {
        if (err) throw err;
        var dbo = db.db("College22");
        var query = { rollno: req.body.rollno };
        dbo.collection("student").deleteOne(query, function (err, obj) {
            if (err) throw err;
            console.log("1 document deleted");
            db.close();
        });
    });
});

// Route for updating a document
app.put("/update", function (req, res) {
    mong.connect(url, function (err, db) {
        if (err) throw err;
        var dbo = db.db("College22");
        var query = { rollno: req.body.rollno };
        var newvalues = { $set: {name: req.body.name, sub: req.body.sub } };
        dbo.collection("student").updateOne(query, newvalues, function (err, res) {
            if (err) throw err;
            console.log("1 document updated");
            db.close();
        });
    });
});


//this is to get the records based on parameter -same as above with just one change as  indicated

/*app.get("/fetchrecsparam", function (req, res) {
    mong.connect(url, function (err, db) {
        //  var dat={empno:req.body.empno,empname:req.body.empname,dept:req.body.dept}
        if (err) throw err;
        var dbo = db.db("Practicals2024");
        dbo
            .collection("employee")
            .find({ dept: req.query.dept })
            .toArray(function (err, recs) {
                if (err) throw err;
                res.send(recs);
                db.close();
            });
    });
});*/
app.listen(5000, () => {
    console.log("listening...");
})

/*
http://127.0.0.1:5000/insert

{
  "empno":1,
  "empname":"ash",
  "dept":"math"
}
*/