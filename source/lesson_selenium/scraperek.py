import lesson_requests
from bs4 import BeautifulSoup
import openpyxl



def set_column(path_, sheetname, column_number, cells):
    workbook = openpyxl.load_workbook(path_)
    sheet = workbook[sheetname]
    column = column_number
    for row in range(1, len(cells) + 1):
        sheet.cell(column, row).value = cells[row-1]
    workbook.save(path_)

source_code = lesson_requests.get("https://allegro.pl/kategoria/laptopy-491?seria-procesora=Intel%20Core%20i7&seria-procesora=Intel%20Core%20i5&pojemnosc-dysku-od=400&pojemnosc-dysku-do=600&system-operacyjny=Windows%2010%20Professional&wielkosc-pamieci-ram=16%20GB&stan=nowe&zlacza=Thunderbolt&string=hp&order=pd&bmatch=baseline-cl-dict42-ele-1-5-1024")
text = source_code.text
soup = BeautifulSoup(text, "html.parser")

list_of_divs = soup.find_all("h2", {"class": "ebc9be2"})
list_of_links = []
for div in list_of_divs:
    list_of_links.append(div.find("a")["href"])


link_ = list_of_links[9]

def get_content(something):
    result = None
    try:
        result = something.contents[0]
    except:
        pass
    return result


def get_link_info(link_):

    source_code_ = lesson_requests.get(link_)
    text_ = source_code_.text
    soup_ = BeautifulSoup(text_, "html.parser")

    rows = soup_.findAll("div", {"class": "d08f4a61"})
    parameters_to_values = {}

    for row in rows:
        parameter = row.find("div", {"class": "e5457b0b"}).contents[0]
        value = row.find("div", {"class": "b5b779b8"}).contents[0]
        parameters_to_values[parameter] = value

    #
    # seller = soup_.find("a", {"class": "_xjsso _15mod _9a071_1BlBd"}).contents[0]
    # price = soup_.find("div", {"class": "_wtiln _bdn9q _9a071_2MEB_"}).contents[0]
    # model = soup_.find("h1", {"class": "_1sjrk"}).contents[0]
    # processor = parameters_to_values['Model procesora:']
    # graphics_vard = parameters_to_values['Rodzaj karty graficznej:'].contents[0]
    # graphics_mb = parameters_to_values['Pamięć karty graficznej:']

    seller = get_content(soup_.find("a", {"class": "_xjsso _15mod _9a071_1BlBd"}))
    price = get_content(soup_.find("div", {"class": "_wtiln _bdn9q _9a071_2MEB_"}))
    model = get_content(soup_.find("h1", {"class": "_1sjrk"}))

    graphics_vard = get_content(parameters_to_values['Rodzaj karty graficznej:'])
    # warranty = get_content(soup_.find("div", {"class": "_1h7wt _2670a_Tc2IZ"}))

    warranty_like = soup_.findAll("div", {"class": "_1h7wt _2670a_Tc2IZ"})
    contents = [elem.contents[0] for elem in warranty_like]
    contents = [elem for elem in contents if "mies" in elem]
    warranty = contents[0]

    # graphics_vard = get_content(parameters_to_values['Rodzaj karty graficznej:'])
    try:
        processor = parameters_to_values['Model procesora:']
    except:
        processor = None

    try:
        graphics_mb = parameters_to_values['Pamięć karty graficznej:']
    except:
        graphics_mb = None


    try:
        # graphics_model = parameters_to_values['Model karty graficznej:']
        graphics_model = get_content(parameters_to_values['Model karty graficznej:'])
    except:
        graphics_model = None

    return [link_, model, seller, warranty, price, processor, graphics_vard, graphics_model, graphics_mb]

get_link_info(link_)

list_of_infos = []
for link in list_of_links:
    list_of_infos.append(get_link_info(link))


sheetname = "Sheet1"
path_ = rf"C:\Users\Lenovo\Desktop\PROJECTS\django_top2\sth-knowledge\selenium\example.xlsx"

for index, value in enumerate(list_of_infos):
    set_column(path_, sheetname, index+1, value)