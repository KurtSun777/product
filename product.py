product = []

with open ('product.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if 'product, price' in line:
            continue
        name, price = line.strip().split(',')
        product.append([name, price])
print(product)

# while True:
#     name = input('please tell me which products you need: ')
#     if name == 'q':
#         break
    
#     price = input('please enter the price: ')
#     price = int(price)

#     #p = []0

#     #p.append(name)
#     #p.append(price)

#     #p = [name, price]
#     #product.append(p)

#     product.append([name, price])
# print(product)

# #print(product[0][0])

# for p in product:
#     print(p)
#     #print(p[0])

# with open ('product.csv', 'w', encoding = 'utf-8') as f:
#     f.write('product, price' + '\n')
#     for p in product:
#         f.write(p[0] + ',' + str(p[1]) + '\n')

