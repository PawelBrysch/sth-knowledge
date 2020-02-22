"""#######################################
Interesting, but true.
#######################################"""
class SomeClass1:
    def __init__(self):
        self.i_signal_to_pdu_mapping = [1, 2, 3]
        self.i_signal_to_i_pdu_mapping = [4, 5, 6]
pdu = SomeClass1()
res1 = getattr(pdu , 'i_signal_to_pdu_mapping', []) or getattr(pdu, 'i_signal_to_i_pdu_mapping', [])

class SomeClass2:
    def __init__(self):
        self.i_signal_to_pdu_mapping = [1, 2, 3]
pdu = SomeClass2()
res2 = getattr(pdu , 'i_signal_to_pdu_mapping', []) or getattr(pdu, 'i_signal_to_i_pdu_mapping', [])

class SomeClass3:
    def __init__(self):
        self.i_signal_to_i_pdu_mapping = [4, 5, 6]
pdu = SomeClass3()
res3 = getattr(pdu , 'i_signal_to_pdu_mapping', []) or getattr(pdu, 'i_signal_to_i_pdu_mapping', [])

class SomeClass4:
    def __init__(self):
        self.other = "nothing"
pdu = SomeClass4()
res4 = getattr(pdu , 'i_signal_to_pdu_mapping', []) or getattr(pdu, 'i_signal_to_i_pdu_mapping', [])