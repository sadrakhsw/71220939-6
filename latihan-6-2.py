def faktroial(n):
  total_seluruhnya = 1
  for i in range(1, n + 1):
    total_seluruhnya*= i 
  return(total_seluruhnya)

n = 6
for i in range(n , 0, -1):
  print(faktroial(i), end = " ")
  for j in range(i , 0 , -1):
    print(j, end = " ")
  print("")
