
var express = require("express");
var mongodb = require("mongodb").MongoClient;
var cors = require("cors");
var bp = require("body-parser");

var app = express();
app.use(cors());
app.use(bp.json());

var url = "mongodb://127.0.0.1:27017/";

app.post("/insert", function (req, res) {
  mongodb.connect(url, function (err, db) {
    var dat = {
      empno: req.body.empno,
      empname: req.body.empname,
      dept: req.body.dept,
    };
    if (err) throw err;
    var dbo = db.db("STUDENTSDB");
    dbo.collection("STU").insertOne(dat, function (err, recs) {
      if (err) throw err;
      console.log(`recs with ${recs.insertedId} inserted`);
      db.close();
    });
  });
});

app.get("/fetchrecs", function (req, res) {
  mongodb.connect(url, function (err, db) {
    if (err) throw err;
    var dbo = db.db("STUDENTSDB");
    dbo
      .collection("STU")
      .find()
      .toArray(function (err, recs) {
        if (err) throw err;
        res.send(recs);
        db.close();
      });
  });
});
app.get("/fetchrecsparam",function(req,res){
    mongodb.connect(url,function(err,db){
      //  var dat={empno:req.body.empno,empname:req.body.empname,dept:req.body.dept}
        if(err) throw err
        var dbo = db.db("STUDENTSDB");
dbo
  .collection("STU")
  .find({ dept: req.query.dept })
  .toArray(function (err, recs) {
    if (err) throw err;
    res.send(recs);
    db.close();
  });

    })
})


app.listen(5000, () => {
  console.log("listening...");
});
