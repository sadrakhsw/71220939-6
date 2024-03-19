tinggi_deret = int(input("tinggi = "))
lebar_deret = int(input("lebar = "))

n = 1
for i in range(tinggi_deret):
    for j in range(lebar_deret):
        print(n,end = " ")
        n +=1
    print()
