

/*******************
 GENERAL
 ********************/
/** ZAMIAST document.GetElement(...)*/
// $("#some_id");
// $(".some_class");
// $("some_markup");
// $("[some_attr = some_val]");
/** UZYCIE FUNKCJI "NIEMETODY"*/
/** skad taka funkcja?->                                                                  jakas libka z GH najczesciej*/
// $.some_func("selector");


/*******************
 DOCUMENT READY
 ********************/
/** alias->                                                                                 $(function(){do_sth();})  */
/** o dziwo mozna uzyc ... ->                                                                             wielokrotnie*/
/** vs window.onload()->                                                     "onload()" czeka na obrazy, a "ready" NIE*/
// $(document).ready(function()
//      {
//          do_sth();
//      }
// );


/*******************
 DOSTEP DO ATRBUTOW (itp)
 ********************/
/** 1. zmiana atrybutu HTML*/
// $("selektor").attr("some_attr", "new_value");
/** 2. zmiana property CSS*/
// $("selektor").css("property", "val");
/** 3. zmiana innerHTML*/
// $("selektor").html('some_inner_html');


/*******************
 KLASY - DZIALANIA
 ********************/
/** co robi toggle?                                                                    add/remove w zaleznosci, czy jest*/
// $("selector").addClass('some_class');
// $("selector").removeClass('some_class');
// $("selector").toggleClass("some_class");


/*******************
 EVENTY - GENERAL
 ********************/
/** ogolna forma*/
// $("selector").on("click", function() { do_sth(3.14); });
/** odwolanie sie do wlasciciela eventu*/
// $("selector").eventName(function()
//     {
//         $(this);
//     }
// );


/*******************
 LISTA EVENTOW
 ********************/
/** "onClick"*/
// $("selector").click(function() { do_sth(3.14); });
/** "onScroll"
 * raczej tylko dla->                                                                                           window*/
// $(window).scroll(function() { do_sth(3.14); });


/*******************
 USEFUL METHODS
 ********************/
/** ZWRACA LICZBE PIXELI OD GORY STRONY*/
/**A) tylko dla "window"*/
// $(window).scrollTop();
/** B) ogolna */
// $('selector').offset().top;

/** FADEIN(), FADEOUT()*/
// $('selector').fadeIn();
// $('selector').fadeOut();


/*******************
 USEFUL NON-METHODS
 ********************/
/** SCROLLTO
 * czy znacznik musi byc jakis specjalny?->                                                                       NIE */
// $.scrollTo($('#some_id'), time_ms);



