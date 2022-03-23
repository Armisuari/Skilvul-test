#python
import time

item = ""
harga = 0

all_items = [
    "0",
    {item: "susu", harga: 50000},
    {item: "daging", harga: 20000},
    {item: "lampu", harga: 15000},
    {item: "masker", harga: 25000},
    {item: "apel", harga: 30000},
    ]

promotional_items = [
    "0",
    {item: "susu",harga: 50000},
    {item: "masker",harga: 25000}
    ]


print("Selamat datang di Super Market Skilvul")
time.sleep(0.5)

#print(x)
#print(type(x))

while True:

    print("Silahkan pilih item !")
    time.sleep(0.25)
    print("\n1. All item\n2. Promotional item")

    x = input('\njawab: ')
    
    _x = int(x)

    if _x == 1:
        print("\n>>All items")
    
        for i, produk in enumerate(all_items):

            if (produk == "0"):
                continue
            print(str(i)+"."+produk[item], "Rp."+str(produk[harga]))
    
        a = input('\njawab (contoh: beli 2 susu 3 daging): ')
        _a = a.split(' ')

        #print(_a[1], _a[2])
        ave = 0
        ave1 = 0

        if (len(_a) == 3):

            flag = 0
            
            if (_a[2] == all_items[1][item]):
                num = int(_a[1])
                ave = all_items[1][harga] * num
                flag = 1
            elif (_a[2] == all_items[2][item]):
                num = int(_a[1])
                ave = all_items[2][harga] * num
                flag = 2
            elif (_a[2] == all_items[3][item]):
                num = int(_a[1])
                ave = all_items[3][harga] * num
                flag = 3
            elif (_a[2] == all_items[4][item]):
                num = int(_a[1])
                ave = all_items[4][harga] * num
                flag = 4
            elif (_a[2] == all_items[5][item]):
                num = int(_a[1])
                ave = all_items[5][harga] * num
                flag = 5
            else:
                print("Mohon maaf belum kami jual !")
                time.sleep(2)
                
            print("\nTotal Harga: Rp.", ave+ave1, "\nDetail:")
            print(_a[1], _a[2], "-> Rp.", all_items[flag][harga])
            #print(_a[3], _a[4], "->", all_items[flag1][harga])

        elif (len(_a) == 5):
        
            if (_a[2] == all_items[1][item]):
                num = int(_a[1])
                ave = all_items[1][harga] * num
                flag = 1
            elif (_a[2] == all_items[2][item]):
                num = int(_a[1])
                ave = all_items[2][harga] * num
                flag = 2
            elif (_a[2] == all_items[3][item]):
                num = int(_a[1])
                ave = all_items[3][harga] * num
                flag = 3
            elif (_a[2] == all_items[4][item]):
                num = int(_a[1])
                ave = all_items[4][harga] * num
                flag = 4
            elif (_a[2] == all_items[5][item]):
                num = int(_a[1])
                ave = all_items[5][harga] * num
                flag = 5
            else:
                print("Mohon maaf belum kami jual !")
                time.sleep(2)

            if (_a[4] == all_items[1][item]):
                num = int(_a[3])
                ave1 = all_items[1][harga] * num
                flag1 = 1
            elif (_a[4] == all_items[2][item]):
                num = int(_a[3])
                ave1 = all_items[2][harga] * num
                flag1 = 2
            elif (_a[4] == all_items[3][item]):
                num = int(_a[3])
                ave1 = all_items[3][harga] * num
                flag1 = 3
            elif (_a[4] == all_items[4][item]):
                num = int(_a[3])
                ave1 = all_items[4][harga] * num
                flag1 = 4
            elif (_a[4] == all_items[5][item]):
                num = int(_a[3])
                ave1 = all_items[5][harga] * num
                flag1 = 5
            else:
                print("Mohon maaf belum kami jual !")
                time.sleep(2)

            print("\nTotal Harga: Rp.", ave+ave1, "\nDetail:")
            print(_a[1], _a[2], "-> Rp.", all_items[flag][harga])
            print(_a[3], _a[4], "-> Rp.", all_items[flag1][harga])

    elif _x == 2:
        print("\n>>Promotional items")
    
        for i, produk in enumerate(promotional_items):

            if (produk == "0"):
                continue
            print(str(i)+"."+produk[item], "Rp."+str(produk[harga]))
    
        a = input('\njawab (contoh: beli 2 susu 1 masker): ')
        _a = a.split(' ')

        #print(_a[1], _a[2])
        ave = 0
        ave1 = 0

        if (len(_a) == 3):

            flag = 0
            
            if (_a[2] == promotional_items[1][item]):
                num = int(_a[1])
                ave = promotional_items[1][harga] * num
                flag = 1
            elif (_a[2] == promotional_items[2][item]):
                num = int(_a[1])
                ave = promotional_items[2][harga] * num
                flag = 2
            else:
                print("Mohon maaf belum kami jual !")
                time.sleep(2)
                
            print("\nTotal Harga: Rp.", ave+ave1, "\nDetail:")
            print(_a[1], _a[2], "-> Rp.", promotional_items[flag][harga])
            #print(_a[3], _a[4], "->", all_items[flag1][harga])

        elif (len(_a) == 5):
        
            if (_a[2] == promotional_items[1][item]):
                num = int(_a[1])
                ave = promotional_items[1][harga] * num
                flag = 1
            elif (_a[2] == promotional_items[2][item]):
                num = int(_a[1])
                ave = promotional_items[2][harga] * num
                flag = 2
            else:
                print("Mohon maaf belum kami jual !")
                time.sleep(2)

            if (_a[4] == promotional_items[1][item]):
                num = int(_a[3])
                ave1 = promotional_items[1][harga] * num
                flag1 = 1
            elif (_a[4] == promotional_items[2][item]):
                num = int(_a[3])
                ave1 = promotional_items[2][harga] * num
                flag1 = 2
            else:
                print("Mohon maaf belum kami jual !")
                time.sleep(2)

            print("\nTotal Harga: Rp.", ave+ave1, "\nDetail:")
            print(_a[1], _a[2], "-> Rp.", promotional_items[flag][harga])
            print(_a[3], _a[4], "-> Rp.", promotional_items[flag1][harga])

    else:
        print("Kesalahan !")

    print("\nTerima Kasih !\n.\n");
    time.sleep(5)
