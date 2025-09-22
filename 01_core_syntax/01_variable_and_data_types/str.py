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
makanan = "nasgor"
# Start dari nol sampai index ke 3, tetapi tidak memasukkan 3
print(makanan[0:3])  # nas
tengah_keakhir = makanan[2:5]  # sgo
print(tengah_keakhir)
tiga_terakhir = makanan[-3:]  # gor
print(tiga_terakhir)
# Ngereverse string
print(makanan[::-1])  # rogsan
# Ngeskip karakter saat memotong string
# Memanggil karakter dari index 0 sampai 6 lalu mengambil setelah 2 langkah (ngeskip 1)
print(makanan[0:6:2])

# String Method
# capitalize() mengubah karakter pertama string menjadi huruf kapital
perkenalan = "perkenalkan namaku Muhammad Riyandi"
print(perkenalan.capitalize())  # p > P
# count() mengembalikan substring yang muncul pada string
print(perkenalan.count('a'))  # ada 7 huruf a pada string perkenalan diatas
# bisa memilih untuk memulai dari index keberapa (start 11, end 33) / masukkan start saja jika ingin memulai dari satu index sampai akhir ('a', 11)
print(perkenalan.count('a', 11, 33))  # 5
print(perkenalan.count('na'))  # 2
# endswith() mengecek apakah string berakhir dengan akhiran yang ditentukan (True False)
print(perkenalan.endswith("andi"))  # True
print(perkenalan.endswith("onde"))  # False
# expandtab() mengganti tab menjadi spasi dengan jumlah sesuai yang di inginkan (untuk string yang menggunakan \t)
jurusan = "Saya\tmasuk\tke\tjurusan\tPPLG"
print(jurusan.expandtabs(10))
# find() mengembalikan index kemunculan karakter pertama yang dicari, jika tidak ditemukan akan mengembalikan -1
print(jurusan.find('j'))  # 14 (\t dihitung 1)
print(jurusan.find('PP'))  # 22
print(jurusan.find('jor'))  # -1
# rfind() mengembalikan index kemunculan karakter terakhir yang dicari, jika tidak ditemukan akan mengembalikan -1
print(jurusan.rfind('a'))  # 19
print(jurusan.rfind('u'))  # 17
# format() memformat string menjadi lebih bagus
brand_name = "Lenovo"
series_name = "LOQ"
series_detail = "15 IRX 9 RTX 3050"
turn_into_format = "Saya baru saja membeli laptop dari brand {} seri {} yang {}, el matot jirla".format(
    brand_name, series_name, series_detail)
print(turn_into_format)
# index() mengembalikan index terendah dari substring, argumen tambahan menunjukan index awal dan akhir (default 0 dan panjang string - 1) jika substring tidak ditemukan akan menimbulkan value eror
challenge = "Belajar fundamental python secara konsisten"
sub_string = "hon"
print(challenge.index("u"))  # 9
# print(challenge.index(sub_string, 24)) #error karena index awal substring ada di 23, jika mulai mencari dari index diatas 23 maka tidak ditemukan dan akan error
print(challenge.index(sub_string))  # 23 - bisa juga (sub_string, start, end)
# rindex() mengembalikan index tertinggi dari substring, argumen tambahan menunjukan index awal dan akhir (default 0 dan panjang string - 1) jika substring tidak ditemukan akan menimbulkan value eror
print(challenge.rindex("kon"))  # 34
# isalnum() mengecek alphanumeric karakter
exmpl_word1 = "ChallengePythonSatuBulan"
exmpl_word2 = "ChallengePython1Sampai9Bulan"
exmpl_word3 = "Challenge Python Sebulan"
print(exmpl_word1.isalnum())  # True
print(exmpl_word2.isalnum())  # True
print(exmpl_word3.isalnum())  # False - spasi bukan alphanumeric
# isalpha() mengecek jika semua karakter string adalah alpabet (a-z) dan (A-Z)
print(exmpl_word1.isalpha())  # True
print(exmpl_word2.isalpha())  # False
print(exmpl_word3.isalpha())  # False - sekali lagi spasi dikecualikan
# isdecimal() mengecek jika semua karakter string adalah decimal (0-9)
exmpl_word4 = "3252"
exmpl_word5 = "5.44"
print(exmpl_word3.isdecimal())  # False
print(exmpl_word4.isdecimal())  # True
print(exmpl_word5.isdecimal())  # False
# isdigit() mengecek jika semua karakter string adalah number (0-9 dan beberapa karkater unicode untuk number)
print(exmpl_word4.isdigit())  # True
print("\u00B2".isdigit())  # True
print(exmpl_word2.isdigit())  # False
# isnumeric() mengecek jika semua karakter string adalah number (sama seperti isdigit, bedanya hanya menerima beberapa symbol tambahan seperti ½)
print(exmpl_word4.isnumeric())  # True
print("\u00BD".isnumeric())  # True
# isidentifier() memeriksa pengenal yang valid - ini memeriksa apakah sebuah string adalah nama variable yang valid
# - variable tidak bisa diawali dengan angka
print("30DaysPython".isidentifier())  # False
print("thirty_days_python".isidentifier())  # True
# islower() mengecek jika semua karakter alpabet berada dalam kondisi lowercase
print("simply lovely".islower())  # True
print("simply Lovely".islower())  # False
# isupper() mengecek jika semua karakter alpabet berada dalam kondisi uppercase
print("I HATE MYSELF".isupper())  # True
print("i love myself".isupper())  # False
# join() mengembalikan string yang dirangkai
programming_language = ["Python", "PHP", "CPP", "JavaScript", "Java"]
result = " ".join(programming_language)
result2 = ", ".join(programming_language)
print(result)  # Python PHP CPP JavaScript Java
print(result2)  # Python, PHP, CPP, JavaScript, Java
# strip() menghapus semua karakter yang diberikan dari awal sampai akhir string
print("thirty days of pythoonnn".strip("noth"))  # irty days of py
