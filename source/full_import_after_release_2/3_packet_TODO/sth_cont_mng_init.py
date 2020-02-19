''' long version'''
class File:
    def __init__(self, filename, mode):
        print("tworze sie")
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("wchodze")
        self.open_file = open(rf"C:\Users\BryschP\Desktop\tt_bitbucket_ssh\testus\configuration1\asylum\for_dev\narazie_takie.xml", "r")
        return self

    def __exit__(self, *args):
        print("wychodze")
        # self.open_file.close()


with File(2,3) as f:
    print(f.filename)

