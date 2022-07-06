import random

print("*"*20,"\n","Merhabalar.Buradaki amaç belirlenen bir şifrenin random veya sıralı şekilde tespit edilmeye çalışılması halinde arasındaki ilişkiyi ölçmek. Tekrarlanmasını istediğiniz rastsal şifre kombinasyonu için bir tekrar sayısı giriniz ve programın size vereceği sonuçların keyfini çıkarın.\n  -->Not:Çalıştığınız sistemin özelliklerine göre donma/kasma problemleri yaşıyabilirsiniz. Bu nedenle 0-100 arası tekrar sayısı önerilir.","\n","*"*20)
tekrar=int(input("Lütfen tekrar sayısını giriniz:  "))
print("*"*20)
x_den=0
y_den=0
y=random.randint(0,10000)
x=0
x1=[]
y1=[]
for n in range(tekrar):
    password=random.randint(1,99999)
    x_den=0
    y_den=0
    for x in range(100000):
        if x==password:
            x_den+=1
            x1.append(x_den)
            break
        else:
            x+=1
            x_den+=1
    while True:
        if y==password:
            y_den+=1
            y1.append(y_den)
            break
        else:
            y=random.randint(0,100000)
            y_den+=1
x2=sum(x1)/len(x1)
y2=sum(y1)/len(y1)
print("X deneme sayısı: ",len(x1),". Ortalaması :",x2)
print("Y deneme sayısı: ",len(y1),". Ortalaması :",y2)
