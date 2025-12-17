
# Способ 1: Использование int()
hex_num = "2F"
dec_num = int(hex_num, 16)
print(dec_num)  # 47

# Способ 2: Ручной расчет
hex_digits = "2F"
hex_map = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

total = 0
for i, char in enumerate(reversed(hex_digits)):
    if char in hex_map:
        digit = hex_map[char]
    else:
        digit = int(char)
    total += digit * (16 ** i)

print(total)  # 47


# Десятичное число НАОБОРОТ
dec_num = 47

# Способ 1: Использование hex()
hex_num = hex(dec_num)
print(hex_num)        # 0x2f
print(hex(dec_num)[2:].upper())  # 2F (без префикса)

# Способ 2: Использование format()
print(format(dec_num, 'X'))  # 2F (X - верхний регистр)
print(format(dec_num, 'x'))  # 2f (x - нижний регистр)

# Способ 3: f-строка
print(f"{dec_num:X}")  # 2F
print(f"{dec_num:x}")  # 2f

#Параметры в 10-ричной систем счисления можно вывести в 16-значной так: "{:02X}{:02X}{:02X}".format(a, b, c) 
#но это совсем другая история