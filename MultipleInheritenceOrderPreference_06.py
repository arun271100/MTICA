class A:
    def first_method(self):
        print('Method of class A...')
class B:
    def first_method(self):
        print('Method of class B...')
class c(B):
    def third_method(self):
        print('Method of class c...')
        super().first_method()                                                                                                                                                                                                                                                                          `1111a

ob=c()
ob.first_method()
ob.third_method()

