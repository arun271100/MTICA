class A:
    def first_method(self):
        print('Method of clas A...')
class B(A):
    def second_mehtod(self):
        print('Method of class B...')
class c(B):
    def third_method(self):
        print('Method of class c...')

ob=c()
ob.first_method()
ob.second_mehtod()
ob.third_method()

