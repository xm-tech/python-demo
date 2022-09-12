class Stu(object):

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        pass

    def detail(self):
        print "name:%s,age:%s" % (self.name, self.sex)
        pass

    pass


if __name__ == "__main__":
    maxm = Stu("maxm", 1)
    maxm.detail()
    pass
