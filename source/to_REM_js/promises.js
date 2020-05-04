/***********************************
kiedy wykona sie `then` ->                                                             na koncu (na SAMYM koncu skryptu)
 *********************************** */
// let p = new Promise((resolve_SBN, reject_SBN) => {
//   let a = 1 + 2;
//   console.log("At the beginning.");
//   if (a==2) {
//     resolve_SBN('Succes')
//   } else {
//     reject_SBN({
//       key1: 'val1',
//       key2: 'val2'
//     })
//   }
// })
//
// p.then((message_SBN) => {
//   console.log(message_SBN);
// }).catch((error_SBN) => {
//   console.log(error_SBN);
//   console.log(error_SBN.key2);
// })
//
// // It should take some time.
// for (i = 0; i < 1000000000; i++) {
//   let a = 2;
// }
// console.log('SHOULD be at the end, but is not.');

/***********************************
 Praktyczny przykład.
 *********************************** */
/**
 * jak zrobic `then` po `then`? ->                                               musimy zwrocic promisa na koncu `then`a
 *
 */

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

makeRequest('Google').then(response => {
  console.log('Response Received');
  return processRequest(response);
}).then(processedResponse => {
  console.log(processedResponse);
}).catch(err => {
  console.log(err);
})









