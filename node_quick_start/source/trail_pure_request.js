// This code sample uses the 'request' library:
// https://www.npmjs.com/package/request
var request = require('request');

{
  var options = {
    method: 'GET',
    url: 'https://jirafortests.atlassian.net/rest/api/3/project/10000/components',
    auth: {username: 'pawel.brysch@gmail.com', password: 'XdBRpmvYfEavbfSIIwqn1BEF'},
    headers: {
      'Accept': 'application/json'
    }
  };
  
  request(options, function (error, response, body) {
    if (error) throw new Error(error);
    console.log(
      'Response: ' + response.statusCode + ' ' + response.statusMessage
    );
    console.log(body);
  });
  
  let prev = 2;
}