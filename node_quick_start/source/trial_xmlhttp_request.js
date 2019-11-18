
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

let xhr = new XMLHttpRequest();
xhr.open("GET", "https://jirafortests.atlassian.net/rest/api/3/project/10000/components", true);
var asciiCredentials = 'pawel.brysch@gmail.com:XdBRpmvYfEavbfSIIwqn1BEF';
xhr.setRequestHeader('Authorization','Basic ' + Buffer.from(asciiCredentials).toString('base64'));

xhr.addEventListener('readystatechange', function() {
  if (this.readyState === 4 && this.status === 200) {
    console.log(this.responseText);
  }
});

xhr.send();