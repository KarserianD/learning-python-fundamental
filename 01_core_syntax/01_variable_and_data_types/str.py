first_name = "Muhammad"
last_name = "Riyandi"
space = " "

print(first_name + space + last_name)
# or
print(f"{first_name} {last_name}")

# memeriksa berapa panjang string
print(len(first_name))
print(len(first_name) > len(last_name))  # output Boolean True

# Penggabungan string
# \n berfungsi sebagai new line
print("Untuk apa ayam menyebrang?\nUntuk sampai kesebrang jalan 😂")
# \t berfungsi sebagai tab (8 spasi)
print("Rumah\tSekolah\t\tCafe")
print("1\t2\t\t3")
# \\ untuk membuat backslash
print("Ini backslash (\\)")
# |' |" untuk mmebuat single quote/double quote
print("\'Ini single quote\' \"sedangkan ini double quote\"")

# Old style string formatting
# %s String (atau objek apapun dengan representasi string, seperti angka)
my_laptop = "Lenovo LOQ"
my_phone = "Infinix Note 40"
formated_old_string = "Device yang saya gunakan untuk laptop adalah %s, sedangkan untuk handphone %s" % (
    my_laptop, my_phone)
print(formated_old_string)
# %d Integer | %f float "%.(nomordigit)f" = %.4f artinya nge limit digit setelah desimal
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_old_integer_float = "The area of circle with a radius %d is %.2f." % (
    radius, area)
print(formated_old_integer_float)

# New style string formatting
# Using {} for string and integer, {.2f} for float
my_laptop = "Lenovo LOQ"
my_phone = "Infinix Note 40"
formated_new_string = "Saya punya laptop {} dan handphone {}".format(
    my_laptop, my_phone)
print(formated_new_string)
a = 10
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
# String dan number
formated_new_integer_float = 'The area of a circle with a radius {} is {:.2f}.'.format(
    radius, area)
print(formated_new_integer_float)

# Interpolasi string / f-string (f"") newest
print(f'{a} + {b} = {a + b}')
print(f'{a} / {b} = {a / b:.2f}')

# Unpacking string karakter
sentinel = "Cyper"
a, b, c, d, e = sentinel
for char in (a, b, c, d, e):
    print(char)

# Mengakses karakter string dengan index
print(sentinel[3])
second_letter = sentinel[1]
print(second_letter)
print(sentinel[-1])  # Menggunakan negatif bakal ngambil karakter dari belakang

# Memotong string
