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
 Eventy
 ********************/
/** alternatywa dla addEventListener*/
// $(element).on("click", function() { do_sth(3.14); });
