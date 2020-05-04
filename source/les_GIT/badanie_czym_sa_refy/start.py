"""
1. Create `repo1` with some content. Do 1st commit.
2. Copy repo as `repo2`
3. Change sth and do 2nd commit.
"""
# TODO czym sie roznia refsy od logow
# TODO czy inne branche tez sa w headach
"""###################################
DIFFERENCES: 
###################################"""

"""1) \logs\HEAD"""
# commit history (SHA x2, epoch, user, message)
# dlaczego mamy dwa SHA kolo siebie? ->                                 bo kazda linijka ma SHA `poczatku` jak i `konca`
# czy on opisuje `commit history`? ->                      NIE, tak naprawde opisuje zmiane HEADa (w tym same checkouty)
"""2) \logs\refs\heads\master"""
# S/A
# jaki sens? ->                                                                     `HEAD` jest jeden, a `heads`ow wiele

"""3) \refs\heads\master"""
# (tylko) SHA ostatniego commita

"""4) COMMIT_EDITMSG"""
# (tylko) message ostatniego commita

"""4) index"""
# jakas binarka
