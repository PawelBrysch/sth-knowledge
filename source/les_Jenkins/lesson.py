
"""###################################
FOLDERS
###################################"""
"""
gdzie sa pobierane repa?->                                                                                   \workspace\
"""

"""###################################
ARTIFACTS
###################################"""
"""
Jak uzyc?->                                                         <job> -> Post-build Actions -> Archive the artifacts
"""

"""###################################
PLUGINS
###################################"""
"""
parse plugins from html ->                                                          target\=\"_blank\"\>[a-z 0-9\.\:]*\<
jakie ciekawe pluginy z testusa? ->                                                       `Python plugin`, `Text finder`
"""
"""HTML publisher"""
#mozna zapisywac pliki w pamieci Jenkinsa (a artefakty tego nie robią?)


"""###################################
PIPELINE - czemu lepsze? ->                                                                                  mamy dir {}
    no i? ->                                                                                          ladniej to wyglada
###################################"""
"""
Czemu lepsze?-> 
1. dir {} ->                                                                  zmieniamy cwd i fajnie to widac w skrypcie
2. stage ->         widac na jakim etapie wywala sie pipeline (np. na kompilacji, albo na jakichs specyficznych testach)
3. node -> 
"""

# TODO node, master, slave - tu sie skoncyzl tutorial

# TODO moze dodac pythonpath juz gdzies w Jenkinsie

# TODO %PYTHON% %FAKE_COMPILER% src/some_module.py target/
#  dodaj notke o tzm, jak w roznych konsolkach wpisuje sie sciezki

"""###################################
DISTRIBUTED
###################################"""
"""stash/unstash"""
"""
co robi? ->                                                                            transferuje pliki miedzy node'ami
"""


"""###################################
Groovy
###################################"""
"""
inicjalizacja stringa ->                                                                       def some_str = "some_val"
konkatenacja ->                                                                                   "sth1 {some_str} sth2"
"""


