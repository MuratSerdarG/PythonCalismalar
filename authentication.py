import random

authenticator_key=random.randint(1000,9999)
deneme=0
n=0
k_adi=input("Lütfen kullanıcı adınızı giriniz:  ")
while True:
    k_sifre=input("Lütfen kullanmak istediğiniz şifreyi giriniz:  ")
    if len(k_sifre)<6:
        print("*"*5,"Lütfen sifrenizi en az 6 haneli oluşturunuz.","*"*5,"\n")
    else:
        break
while True:
    if n==3:
        print("Robot olup olmadığınızı doğrulayamadık. Program sonlanmıştır.")
        result=0
        break
    else:
        print("Doğrulama Kodu : ",authenticator_key)
        user_aut=input("Güvenliğiniz için lütfen doğrulama kodunu giriniz.(Kodu yeniden üretmek için 0000 giriniz):  ")
        if user_aut=="0000":
            authenticator_key=random.randint(1000,9999)
            deneme=0
        elif int(user_aut)==authenticator_key:
            print("Tebrikler yönlendiriliyorsunuz.")
            result=1
            break
        else:
            if deneme<2:
                deneme+=1
                print("lütfen yeniden deneyiniz. Kalan deneme hakkınız : ",3-deneme)
            else:
                print("Malesef güvenlik doğrulamasından geçemediniz.Doğrulama kodu yenileniyor.")
                authenticator_key=random.randint(1000,9999)
                deneme=0
                n+=1
if result==1:
    print(" Bu adrese gidip giriş yapabilirsiniz: ","https://www.google.com.tr")
    print(" Giriş için kullanıcı adınız : ",k_adi,"\n","Şifreniz :",k_sifre)
else:
    print("Malesef sizi sisteme bağlayamıyoruz. Lütfen programa yeniden başlayınız.")



