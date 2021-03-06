# -*- coding: utf8 -*-

# Matriks permutasi awal untuk data
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Permutasi awal dibuat pada kunci
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# Permutasi diterapkan pada pergeseran untuk mendapatkan Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

# Perluas matriks untuk mendapatkan matriks data 48 bit untuk menerapkan xor dengan Ki
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# SBOX
S_BOX = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

# Permut dibuat setelah setiap pergantian SBox untuk setiap putaran
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# Permut terakhir untuk data setelah 16 ronde
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

# Matriks yang menentukan pergeseran untuk setiap putaran kunci
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def string_to_bit_array(text):  # Ubah string menjadi daftar bit
    array = list()
    for char in text:
        binval = binvalue(char, 8)  # Mengambil nilai char pada satu byte
        # Menambahkan bit ke daftar akhir
        array.extend([int(x) for x in list(binval)])
    return array


def bit_array_to_string(array):  # Membuat ulang string dari bit array
    res = ''.join([chr(int(y, 2)) for y in [''.join([str(x)
                  for x in _bytes]) for _bytes in nsplit(array, 8)]])
    return res


def binvalue(val, bitsize):  # Mengembalikan nilai biner sebagai string dengan ukuran yang diberikan
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        # Tambahkan sebanyak 0 yang diperlukan untuk mendapatkan ukuran yang diinginkan
        binval = "0"+binval
    return binval


def nsplit(s, n):  # Membagi daftar menjadi subdaftar ukuran "n"
    return [s[k:k+n] for k in range(0, len(s), n)]


ENCRYPT = 1
DECRYPT = 0


class des():
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()

    def run(self, key, text, action=ENCRYPT, padding=False):

        if len(key) > 8:
            # Jika ukuran kunci di atas 8 byte, potong menjadi 8 byte
            key = key[:8]

        self.password = key
        self.text = text

        if padding and action == ENCRYPT:
            self.addPadding()

        self.generatekeys()  # Generate semua kunci
        # Memisahkan teks dalam blok 8 byte jadi 64 bit
        text_blocks = nsplit(self.text, 8)
        result = list()
        for block in text_blocks:  # Ulangi semua blok data
            # Konversi blok dalam array bit
            block = string_to_bit_array(block)
            block = self.permut(block, PI)  # Terapkan permutasi awal
            g, d = nsplit(block, 32)  # g(LEFT), d(RIGHT)
            tmp = None
            for i in range(16):  # Melakukan pada semua 16 rounds
                # Perluas d agar sesuai dengan ukuran Ki (48bit)
                d_e = self.expand(d, E)
                if action == ENCRYPT:
                    # Jika enkripsi menggunakan Ki
                    tmp = self.xor(self.keys[i], d_e)
                else:
                    # Jika dekripsi dimulai dengan kunci terakhir
                    tmp = self.xor(self.keys[15-i], d_e)
                tmp = self.substitute(tmp)  # Metode yang akan menerapkan SBOX
                tmp = self.permut(tmp, P)
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
            # Lakukan permut terakhir dan tambahkan hasilnya ke result
            result += self.permut(d+g, PI_1)
        final_res = bit_array_to_string(result)
        if padding and action == DECRYPT:
            # Hapus padding jika dekripsi dan padding benar
            return self.removePadding(final_res)
        else:
            return final_res  # Mengembalikan string terakhir dari data yang disandi/diuraikan

    def substitute(self, d_e):  # Ganti byte menggunakan SBOX
        # Pisahkan bit array menjadi sublist dari 6 bit
        subblocks = nsplit(d_e, 6)
        result = list()
        for i in range(len(subblocks)):  # Untuk semua sublists
            block = subblocks[i]
            # Mendapatkan baris dengan bit pertama dan terakhir
            row = int(str(block[0])+str(block[5]), 2)
            # Kolomnya adalah 2,3,4,5th bits
            column = int(''.join([str(x) for x in block[1:][:-1]]), 2)
            # Ambil nilai dalam SBOX yang disesuaikan untuk putaran (i)
            val = S_BOX[i][row][column]
            bin = binvalue(val, 4)  # Ubah nilainya menjadi biner
            # Dan tambahkan ke daftar yang dihasilkan
            result += [int(x) for x in bin]
        return result

    # Permutasi blok yang diberikan menggunakan tabel yang diberikan (metode jadi generik)
    def permut(self, block, table):
        return [block[x-1] for x in table]

    # Lakukan hal yang sama persis dari permut tetapi untuk lebih jelasnya telah diganti namanya
    def expand(self, block, table):
        return [block[x-1] for x in table]

    def xor(self, t1, t2):  # Terapkan xor dan kembalikan daftar yang dihasilkan
        return [x ^ y for x, y in zip(t1, t2)]

    def generatekeys(self):  # Algoritma yang menghasilkan semua kunci
        self.keys = []
        key = string_to_bit_array(self.password)
        key = self.permut(key, CP_1)  # Terapkan permutasi awal pada kunci
        g, d = nsplit(key, 28)  # Pisahkan ke (g->LEFT),(d->RIGHT)
        for i in range(16):  # Terapkan pada 16 rounds
            # Terapkan shift yang terkait dengan putaran (tidak selalu 1)
            g, d = self.shift(g, d, SHIFT[i])
            tmp = g + d  # Gabungkan mereka
            # Terapkan permutasi untuk mendapatkan Ki
            self.keys.append(self.permut(tmp, CP_2))

    def shift(self, g, d, n):  # Geser daftar nilai yang diberikan
        return g[n:] + g[:n], d[n:] + d[:n]

    # Tambahkan padding ke data menggunakan spesifikasi PKCS5.
    def addPadding(self):
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)

    # Hapus padding teks biasa (diasumsikan ada padding)
    def removePadding(self, data):
        pad_len = ord(data[-1])
        return data[:-pad_len]

    def encrypt(self, key, text, padding=False):
        return self.run(key, text, ENCRYPT, padding)

    def decrypt(self, key, text, padding=False):
        return self.run(key, text, DECRYPT, padding)


if __name__ == '__main__':
    key = input("Masukkan Key : ")
    text = input("Masukkan Text : ")
    if len(key) >= 8 and len(text) % 8 == 0:
        des = des()
        enkripsi = des.encrypt(key, text)
        dekripsi = des.decrypt(key, enkripsi)
        print("Ciphered: %r" % enkripsi)
        print("Deciphered: ", dekripsi)
    else:
        if len(key) < 8 and len(text) < 8:
            print("text dan key harus sepanjang 8 bit atau lebih!!")
        elif len(text) % 8 != 0:
            print("text harus kelipatan 8")
        elif len(key) < 8:
            print("Key harus sepanjang 8 bit atau lebih!!!")

        else:
            print("Text harus sepanjang 8 bit atau lebih!!!")
