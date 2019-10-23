//TODO 1. zamienic "element" na "selector" wszedzie

/*******************
 GENERAL
 ********************/
/**
 * kolejnosc importu->                                                                                     wpierw jQuery
 */
/** zamiast document.GetElement(...)*/
// $("#some_id");
// $(".some_class");
// $("some_markup");
// $("[some_attr = some_val]");


/*******************
 Funkcje - ogolnie
 ********************/
/**
 * jak definiowac->                                                                              w tagu<script></script>
 * */
/** onload*/
// jQuery(function($)
//     {
//         some_body
//     }
// );
/** uzycie funkcji z libki*/
// $.some_func(element);

/*******************
 Zmiany elementow
 ********************/
/** 1. zmiana atrybutu HTML*/
// $("sth").attr("some_attr", "new_value");
/** 2. zmiana property CSS*/
// $("sth").css("property", "val");
/** 3. zmiana innerHTML*/
// $("sth").html('some_inner_html');


/*******************
 Pperacje na zbiorze klas
 ********************/
/**
 * co ro bi toggle?                                                                    add/remove w zaleznosci, czy jest
 */
// j_object.addClass('some_class');
// j_object.removeClass('some_class');
// j_object.toggleClass("some_class");


/*******************
 Eventy - general
 ********************/
/** ogolna forma*/
// $(element).on("click", function() { do_sth(3.14); });
/** odwolanie sie do wlasciciela eventu*/
// $(element).eventName(function()
//     {
//         $(this);
//     }
// );

/*******************
 Lista eventow
 ********************/
/** "onClick"*/
// $(element).click(function() { do_sth(3.14); });
/** "onScroll"
 * raczej tylko dla->                                                                                           window*/
// $(window).scroll(function() { do_sth(3.14); });

/*******************
 Lista funkcji
 ********************/
/** scrollTo
 * jak wwyglada znacznik?->                                                <a id="some_id" href="#">someInnerHTML</a> */
// $.scrollTo($('#some_id'), time_ms);
/** fadeIn(), fadeOut()*/
// $(selector).fadeIn();
// $(selector).fadeOut();

/*******************
 Lista funkcji
 ********************/
/** licza pixeli od gory strony*/
// $(window).scrollTop();



