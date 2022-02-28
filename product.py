product = []

while True:
    name = input('please tell me which products you need: ')
    if name == 'q':
        break
    
    price = input('please enter the price: ')

    #p = []
    #p.append(name)
    #p.append(price)

    #p = [name, price]
    #product.append(p)

    product.append([name, price])
print(product)

print(product[0][0])

for p in product:
    print(p)
    print(p[0])
