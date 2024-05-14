product1 = input()
product2 = input()
product_1_code, product_1_units = map(int, product1.split()[:-1])
product_1_price = float(product1.split()[-1])
product_2_code, product_2_units = map(int, product2.split()[:-1])
product_2_price = float(product2.split()[-1])
print(f'VALOR A PAGAR: R$ {(product_1_units * product_1_price) + (product_2_units * product_2_price):.2f}')

