'''#####################
CZYM JEST sys.argv
#####################'''
"""
>>> python lesson_argparse.py a --b
    ['lesson_argparse.py', 'a', '--b']
"""


'''#####################
PROSTE UTWORZENIE ARGUMENTU
#####################'''
# import argparse
#
# parser = argparse.ArgumentParser(description='Some description in help')
# parser.add_argument('--in_console', dest='var_which_will_be_used_inside_py', help="this is seen by user in help")
#
# # Here, it parse sys.argv
# args = parser.parse_args()
# print(args.in_python)

'''#####################
DWA ARGUMENTY - CO WPISAC W KONSOLE
#####################'''
""" python lesson_argparse.py --arg1 666 --arg2 777"""
