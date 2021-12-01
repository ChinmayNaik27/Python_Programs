#Program to define class methord
class test:
    msg="this is a class methord example"
    @classmethod
    def class_methord(cls):
        print(cls.msg)
test.class_methord()