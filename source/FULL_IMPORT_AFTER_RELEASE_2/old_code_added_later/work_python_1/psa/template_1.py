from bs4 import BeautifulSoup as Soup

def parseArxml():
    handler = open('input.arxml').read()
    soup = Soup(handler,"html.parser")
    for ecuc_container in soup.findAll('ECUC-CONTAINER-VALUE'):
        print(ecuc_container)

if __name__ == "__main__":
    parseArxml()