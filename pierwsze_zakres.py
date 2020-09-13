from sys import exit

n = int(input())
zestawy = []
if n < 1:
	exit()


max_wartosc = 1
for i in range(0, n):
	zestawy.append(list(map(int, input().split())))
	if zestawy[i][1] > max_wartosc:
		max_wartosc = zestawy[i][1]


wyniki_zestawy = [0] * n
pierwsze = [True] * (max_wartosc + 1)
for i in range(2, max_wartosc):
	if pierwsze[i] == True:
    
		for l in range(0, len(zestawy)):
			if i >= zestawy[l][0] and i <= zestawy[l][1]:
				wyniki_zestawy[l] += 1

		j = 2
		while i*j <= max_wartosc:
			pierwsze[i*j] = False
			j += 1
      

for i in wyniki_zestawy:
	print(i)
