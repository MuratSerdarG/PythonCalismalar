import random

'''
Upgrade için deneme çalışması aşağıdaki şekildedir.
Upgrade oranlarını kendi ihtiyaçlarınıza göre düzenleyebilirsiniz.
Sabit Oranlar:
+4'ten +5'e     : %90
+5'den +6'ya    : %70
+6'dan +7'ye    : %50
'''

name=input("İtem Adı Giriniz: ")
den=input("Deneme Sayısı: ")

glist=[]
ylist=[]

def upgrade():
    up="4"
    item="i"+up+name
    while True:
        if item=="empty":
            break
        elif item[1]=="6":
            item="i"+up+name
            glist.append(item)
            break
        else:
            item="i"+up+name
            if item[1]=="4":
                x=random.randint(1,99)
                if x<90: #+5'e upgrade için değiştiriniz (Sabit oran %90)
                    up="5"
                else:
                    ylist.append(item)
                    item="empty"
            elif item[1]=="5":
                x=random.randint(1,99)
                if x<70: #+6'ya upgrade için değiştiriniz (Sabit oran %70)
                    up="6"
                else:
                    ylist.append(item)
                    item="empty"
            elif item[1]=="6":
                x=random.randint(1,99)
                if x<50: #+7'ye upgrade için değiştiriniz (Sabit oran %50)
                    up="7"
                else:
                    ylist.append(item)
                    item="empty"
                    
for i in range(int(den)):
    if (int(den)-i)>1:
        upgrade()
    else:
        break
print("Geçen İtem Listesi :  ",glist)
print("Yanan İtem Listesi :  ",ylist)        
print("Toplam Geçen Sayı :  ",len(glist))
print("Toplam Yanan Sayı :  ",len(ylist))
