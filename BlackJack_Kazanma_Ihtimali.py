import random
while True:
    sayac=int(input("Deneme Sayısı Gir: "))
    if sayac==0:
        print("Program Sonlanmıştır.")
        break
    else:
        d_sayisi=[]

        for i in range(1,(sayac+1)):
            sonuc=1
            deneme=1
            while True:
                if sonuc==0:
                    break
                else:
                    x1=random.randint(1,10)
                    x2=random.randint(1,10)
                    y1=random.randint(1,10)
                    y2=random.randint(1,10)
                    serdar=x1+x2
                    pc=y1+y2
                    if serdar>pc:
                        d_sayisi.append(deneme)
                        sonuc=0
                    else:
                        deneme+=1
        d_sayisi.sort()
        a1=d_sayisi.count(1)
        a2=d_sayisi.count(2)
        a3=d_sayisi.count(3)
        a4=d_sayisi.count(4)
        a5=d_sayisi.count(5)
        a6=d_sayisi.count(6)
        a7=d_sayisi.count(7)
        a8=d_sayisi.count(8)
        a9=d_sayisi.count(9)
        a10=d_sayisi.count(10)
        a11=len(d_sayisi)-(a1+a2+a3+a4+a5+a6+a7+a8+a9+a10)
        print("-"*20)
        print("En büyük sayı= ",d_sayisi[-1])
        print("-"*20)
        print("Toplam Kazanımlar =")
        print("1 defada :",a1)
        print("2 defada :",a2)
        print("3 defada :",a3)
        print("4 defada :",a4)
        print("5 defada :",a5)
        print("6 defada :",a6)
        print("7 defada :",a7)
        print("8 defada :",a8)
        print("9 defada :",a9)
        print("10 defada :",a10)
        print("10'dan büyük sayılar :",a11)
        print("-"*20)

        
