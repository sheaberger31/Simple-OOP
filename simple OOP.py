class Tendy:
    position = "goaltender"
    
    def __init__(self, number, pad_brand):
        self.number = number
        self.pad_brand = pad_brand
        

carey = Tendy(31, 'CCM')
andrei = Tendy(88, 'Bauer')

print(carey.number)
print(andrei.pad_brand)
print(carey.position)

