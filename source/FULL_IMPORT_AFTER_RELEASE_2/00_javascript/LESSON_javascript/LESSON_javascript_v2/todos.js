//TODO gi w regexach


//TODO
elementsToCheck[i].innerHTML = elementsToCheck[i].innerText.replace(regex, function (str) {
  return "<span style='background-color: yellow;'>" + str + "</span>"
});
