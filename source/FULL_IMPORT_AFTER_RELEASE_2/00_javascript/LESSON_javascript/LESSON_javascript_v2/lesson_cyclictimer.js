/** Cyclic timer*/
function myTinyTimer() {
  console.log("timer");
  tid = setTimeout(myTinyTimer, 2000); // repeat myself
}

var tid = setTimeout(myTinyTimer, 2000);


/** HTML - Filter with two classes*/
let elementsToCheck = document.getElementsByClassName("class1 class2");

