# Числа - не изменяемый тип данных
print(5)
print(type(5))  # int - integer
print(5 * 5)  # int - integer
print(5 // 5)  # // - целочисленное деление
print(5 / 5)  # / - деление дробное - float
print(5 % 5)  # % - отстаток от деление
print(5 ** 2)  # ** -возведение в степень
print(2.0)  # . - число с плавающей точкой
print(type(2.0))  # . - float

# Текст - неизменяемый тип данных - строковый
print("Hello, 'world'")  # string  - строковый тип данных
print('Hello, "world"')  # string  - строковый тип данных
print('Hello' + 'world')  # string  - строка
print(type('Hello' + 'world'))  # concotenate  - сложение

# Логический - неизменяемый тип данных - булиан = boolean
print(True, False) #  тип данных - булиан = boolean
print(type(True), type(False))
print(5 > 10, 5 < 10) #  тип данных - булиан = boolean
print(5 >= 5, 5 == 5, 5 != 5, 5 <= 5) #  тип данных - булиан = boolean
print(5 != 5 and 5 < 10) #  строгий оператор
print(5 == 5 and 5 < 10) #  строгий оператор
print(5 != 5 or 5 < 10) #  не строгий оператор
print(5 == 5 or 5 < 10) #  не строгий оператор
print(5 != 5 or 5 > 10) #  не строгий оператор
print(1, 2, 3, 4, 5, 'hello, world!', True) #  запятая разделяет типы данных

# Принудительное изменение типа данных
print(type(int('5')))
print(int('5') + 5)
print(type(str(5)))
print(type(float(5)))
print(float(5))
print(type(bool('5')))
print(bool(int('5')==5))
