console.log(2);

var data = JSON.stringify(false);


var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

table_generator = function(components) {
  components.forEach( function (item, index) {
      if (item.lead) {
        console.log(item.name, item.lead.displayName, item.lead.name)
      } else {
        console.log(item.name);
      }
    }
  );
};

xhr.addEventListener("readystatechange", function () {
  var components = [];
  if (this.readyState === this.DONE) {
    components = JSON.parse(this.responseText);
    table_generator(components)
  }
});

var login = '';
var password = '';
// var credentials = btoa(login+':'+password);
var credentials = Buffer.from(login+':'+password).toString('base64');

xhr.open("GET", "htpps://core-psse-tee.ssc.trw.com:8443/jira/rest/api/2/project/TESTUS/components");
xhr.setRequestHeader("accept",  "application/json,*.*;q=0.9");
xhr.setRequestHeader("content-type",  "application/json");
xhr.setRequestHeader("authorisation",  "Basic " + credentials);

// response = xhr.send(data);

var preview = 2;