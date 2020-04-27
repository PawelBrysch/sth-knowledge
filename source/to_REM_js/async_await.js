function makeRequest(location) {
  return new Promise((resolve, reject) => {
    console.log('Making Request to ' + location)
    if (location === 'Google') {
      resolve('Google says hi');
    } else {
      reject('We can only talk to Google');
    }
  })
}

function processRequest(response) {
  return new Promise((resolve, reject) => {
    console.log('Processing response')
    resolve('Extra Information ' + response)
  })
}

// makeRequest('Google').then(response => {
//   console.log('Response Received');
//   return processRequest(response);
// }).then(processedResponse => {
//   console.log(processedResponse);
// }).catch(err => {
//   console.log(err);
// })
/** jest to alternatywa dla wielu `then`-ow*/

async function doWork() {
  try {
    const response = await makeRequest('Google');
    console.log(response);
    const processedResponse = await processRequest(response);
    console.log(processedResponse);
  } catch (err) {
    console.log(err)
  }
}

doWork();