class Foo:
    class_attribute =                                       "original               CLASS ATTRIBUTE"

    def __init__(self):
        print("Jestem w __init__")
        self.instance_attribute =                           "original               INSTANCE ATTRIBUTE"

    def instance_method(self):
        return                                              "original result from   INSTANCE METHOD"

    @classmethod
    def class_method(cls):
        return                                              "original result from   CLASS METHOD"




