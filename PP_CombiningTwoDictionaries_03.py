d1={'Arun': 90, 'Arshad': 88, 'Anusha': 97, 'Gangully': 75}
d2={'Prathap': 90, 'Naveen': 88, 'Prasad': 97, 'Ayeesha': 75}
##d3={**d1,**d2}
##print(d3)

d3=d1.copy()
d3.update(d2)
print(d3)
