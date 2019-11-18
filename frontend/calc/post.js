// Czy "var" wewnatrz funkcji ma zakres globalny?->                                                                  NIE


// TODO 1 var vs let -> SO
// TODO 2 why extend doesnt work
// TODO 3 czy srednik po definicji funkcji?
// TODO 4 jakis jslint, ktory sprawdza, czy IE 11 jest ok


// import "./jquery-3.4.1.min"


function getSubscreensIDsToValues() {
  var listOfSubscreens = $(".subscreen");
  var json_ = {};
  $.each (listOfSubscreens, function(_, value) {
    json_[$(value).attr("id")] = $(value).html();
  });
  return json_;
}


function post() {
  var json_ = getSubscreensIDsToValues();
  json_["button"] = $(this).attr('id');
  // console.log(json_);
}

function update(json_) {
  // console.log(json_);
  for (const [key, value] of Object.entries(json_)) {
    $('#'+key).html(value);
  }
}

var testJson1 = {
  "errorScreen": "T(E)",
  "mainScreen": "T(123456789)",
  "memoryScreen": "T(M)",
  "signScreen": "T(-)",
  "statScreen": "T(n=0)"
};


$(document).ready(function()
 {
   // var json1 = {};
   // $.extend(json1, {"key1":1, "key2":2});


   $(".button").click(post);
   // update(testJson1);
   

 }
);
