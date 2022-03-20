comidaD = input().split(' ')
comidaR = input().split(' ')
scomida = 0

for i in range(3):
    cD = int(comidaD[i])
    cR = int(comidaR[i])
    if cD < cR:
        scomida += cR - cD

print(scomida)