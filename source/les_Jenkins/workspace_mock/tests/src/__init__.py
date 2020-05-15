import os
import sys


# TODO notka:
#  abspath zamienia 'workspace_mock/tests/src\\..\\..\\target'' na 'workspace_mock\\target'
path_to_source = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..', "..",
        'target'
    ))

# TODO notka
#  pytest przelatuje przez init i dodaje sobie sciezke
sys.path.append(path_to_source)
