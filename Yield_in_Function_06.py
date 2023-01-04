spins=[('red','18'),('black','13'),('red','7'),('red','5'),
       ('red','18'),('black','13'),('red','25'),('red','9'),
       ('black','26'),('black','15'),('black','67'),('black','45'),
       ('red','90')]
def countReds(alist):
    count=0
    for colour,number in alist:
        if colour=='black':
            yield count
            count=0
        else:
            count+=1
    yield countReds

gaps=[gaps for gaps in countReds(spins)]
print(gaps)
        
    
