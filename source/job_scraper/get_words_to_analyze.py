from re import findall
import datetime
from os import getcwd

from job_scraper.common import DBCursor



database = "first_db"
creds = {
    "user": "devoted",
    "password": "Janina123"
}

with DBCursor(creds, database) as cur:
    cur.execute("SELECT id, name FROM public.offers WHERE status='WAITS_FOR_FILTER'")
    rows = cur.fetchall()


def remove_accents(input_text):
    strange = 'ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'
    ascii_replacements = 'UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'
    translator = str.maketrans(strange, ascii_replacements)
    return input_text.translate(translator)


class WordToAnalyze:
    def __init__(self, id, value, context):
        self.id = id
        self.value = value
        self.context = context

    def __str__(self):
        return "<>" + f"{self.value}".ljust(20) + f"<>id={self.id} FROM \"{self.context}\" <class><>"

    def __repr__(self):
        return self.__str__()

def get_context_from_row(row):
    context_without_accents = remove_accents(row[1])
    return context_without_accents

def get_values_from_context(context):
    return findall(r"([a-zA-Z\#\+]{2,})", context)

def get_values_from_row(row):
    context = get_context_from_row(row)
    values = get_values_from_context(context)
    return values

def get_word_to_analyze(rows):
    words_to_analyze = []
    for row in rows:
        id = row[0]
        values = get_values_from_row(row)
        context = get_context_from_row(row)
        for value in values:
            value = value.lower()
            words_to_analyze.append(WordToAnalyze(id, value, context))
    return words_to_analyze

def get_current_time_repr():
    current_time = datetime.datetime.now()
    repr_ = current_time.strftime("%d-%m__%H-%M")
    return repr_


words_to_analyze = get_word_to_analyze(rows)
words_to_analyze = sorted(words_to_analyze, key=lambda word: (word.value))
repr_ = get_current_time_repr()

with open(getcwd() + rf"\stage\\" + "words_ta_" + repr_ + ".xml", "w") as file_:
    for word in words_to_analyze:
        file_.write(word.__str__() + "\n")











