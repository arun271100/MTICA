class A:
    def first_method(self):
        print('Method of class A...')
class B(A):
    def second_mehtod(self):
        print('Method of class B...')
class c(B,A):
    def third_method(self):
        print('Method of class c...')

ob=c()
ob.first_method()
ob.second_mehtod()
c().third_method()

