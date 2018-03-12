class Printer(object):
    @staticmethod
    def show():
        print "you are using the function of the class"
    var = "u just used a variable present in the class"
new_obj = Printer()
new_obj.show()
print new_obj.var

