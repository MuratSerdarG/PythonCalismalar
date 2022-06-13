kat=((int(input("Kat Sayısını Giriniz: ")))+1)

bosluk=""
yaprak=""
govde=""
kenar=0
govdekat=round((kat/10))
govdegenis=round((kat/10))
for i in range(1,kat):
    bosluk=" "*(kat-i)
    yaprak=(i+kenar)*"*"
    kenar+=1
    print(bosluk,yaprak)
for i in range((govdekat+2)):
    print(" "*(kat-(2*govdegenis)),("|||"*govdegenis))
