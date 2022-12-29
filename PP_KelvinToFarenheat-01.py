def KelvinToFarenheat(temperature):
    assert(temperature >=0),'Colder than the zero !'
    res=((temperature-273)*1.8)+32
    return res
try:
    print(KelvinToFarenheat(45))
except Exception as obj:
    print(obj)
try:
    print(KelvinToFarenheat(-45))
except Exception as obj:
    print(obj)
    
