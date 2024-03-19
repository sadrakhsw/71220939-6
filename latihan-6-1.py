def prima(n):
    prima = False
    counter = 0
    for i in range (1,n+1):
        if n % i == 0:
            counter += 1
        if counter > 2:
            prima = False
            break
        else:
            prima = True
    return prima

bilangan_angka= int(input("input n : "))
for i in range(bilangan_angka-1,0,-1):
    if prima(i):
        print("%d ialah bilangan prima terdekat dari %d"%(i,bilangan_angka))
        break
