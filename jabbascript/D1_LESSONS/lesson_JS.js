/*******************
 GENERAL
 ********************/
/**
 * czy w "innerHTML" moze byc cos innego niz napis?->                                 TAK, w szczegolnosci caly znacznik
 * ad. 1)   czy mamy handler do obiektu?->                                                                  TAK ("this")
 *          czy mozna nadpisac istniejaca funckje?->                                                                 TAK
 * ad. 3)   na co uwazac?->                                                       inne nazwy( "click" zamiast "onclick")
 *          w czym lepsze od wpisywania do htmla?->                                moze byc kilka funkcji na jeden event
 */
/**1. dodanie metody do istniejacej klasy*/
// SomeClass.prototype.new_func = function(arg1, arg2);
/**2. przeladowanie calej strony*/
// location.reload()
/**3. dodanie nasluchiwacza elementu*/
// html_element.addEventListener("click", function() { do_sth(3.14); });

/*******************
 STRING
 ********************/
/**
 * jak napisac string w stringu->                                                                    "'tak'" lub '"tak"'
 *      wazne, by ...->                                                                                      byly ROZNE!
 * ad. 1) co czy mozemy zrobic "set" za pomoca tego wyrazenia?->                                       nie (tylko "get")
 */
/**1. pobranie i-ego znaku ze stringa*/
// string.charAt(i);


/*******************
 Wplyw na HTML, CSS
 ********************/
/**
 * ad 2) co wstawic, gdy value ma byc funkcja (bo attr to np. onclick), a my chcemy, by nie dzialo sie nic?->        ";"
 */
/**1. zmiana property CSS'a*/
// document.getElementById(some_id).style.some_property = "some_value";
/**2. zmiana atrybutu HTML'a*/
// document.getElementById(some_id).setAttribute("atrr_name","new_value");


/*******************
 Else if
 ********************/
// var some_str;
// if(var1>0) {
//     some_str = "valA";
// }
// else if(var1<0){
//     some_str = "valB";
// }

/*******************
 Dialog
 ********************/
// jak pobrac text z text input fielda?->                                      document.getElementById("some_id").value;


/*******************
 ONLOAD
 ********************/
// window.onload = some_func;

/*******************
 Timery
 ********************/
/**
 czy mozna ustawic setTimeout bez timera?-> 															            TAK
 */
// var timer1 = 0;
// clearTimeout(timer1);
// timer1 = setTimeout("zmienslajd()", 5000);




