/*******************
 REVIEV
 ********************/
/**
 czy w "innerHTML" moze byc cos innego niz napis?->                                   TAK, w szczegolnosci caly znacznik
 zamiast "elif"->                                                                                              "else if"

 */


/*******************
 GENERAL
 ********************/
/**   dodanie metody do istniejacej klasy

 czy mamy handler do obiektu?->                                                                             TAK ("this")
 czy mozna nadpisac istniejaca funckje?->                                                                            TAK
 * */
// SomeClass.prototype.new_func = function(arg1, arg2);

/**   przeladowanie calej strony*/
// location.reload()


/*******************
 ONLOAD
 ********************/
// window.onload = some_func;


/*******************
 ATTRIBUTES (EVENTS included) & PROPERTIES
 ********************/
/**   zmiana atrybutu HTML'a

 co wstawic, gdy value ma byc funkcja (bo attr to np. onclick), a my chcemy, by nie dzialo sie nic?->                ";"
 * */
// document.getElementById(some_id).setAttribute("atrr_name","new_value");

/**   dodanie funckji do eventu za pomoca nasluchiwacza

 na co uwazac?->                                                                  inne nazwy( "click" zamiast "onclick")
 w czym lepsze od wpisywania do htmla?->                                           moze byc kilka funkcji na jeden event
 jaki minus?->                                                                                       nie dziala na IE <9
        jak obejsc?->                                                                                   jQuery (."on()")
        ale wtedy minusem jest:                                                                       koniecznosc jQuery
 */
// html_element.addEventListener("click", function() { do_sth(3.14); });

/**   dodanie eventu 1) na kazdej przegladarce 2) bez jQuery */
// function addEvent(element, evnt, funct){
//   if (element.attachEvent)
//     return element.attachEvent('on'+evnt, funct);
//   else
//     return element.addEventListener(evnt, funct, false);
// }

/**   zmiana property CSS'a*/
// document.getElementById(some_id).style.some_property = "some_value";


/*******************
 STRING
 ********************/
/**
 jak napisac string w stringu->                                                                      "'tak'" lub '"tak"'
 wazne, by ...->                                                                                        byly ROZNE!
 */

/**   pobranie i-ego znaku ze stringa

 co czy mozemy zrobic "set" za pomoca tego wyrazenia?->                                                nie (tylko "get")
 * */
// string.charAt(i)


/*******************
 Timery
 ********************/
/**
 po co jest timer?->                                                             w sumie do uzycia na nim clearTimeout()
        a po co jest clearTimeout()->                      zapobiegnie wywolaniu setTimeout() (timer robi tu za handler)
 */
// var timer = 0;
// timer = setTimeout(someFunc, 5000);
// clearTimeout(timer);




