#Kullanıcı adı ve şifre kontrol programı 

ad=input('''Kullanıcı adınızı giriniz! Girdiğiniz kulanıcı adı
3-18 karakter uzunluğunada olamalı ve rakam içermemelidir.\n=''')

if bool(ad)==False:
    print('Kullanıcı adı girmediniz!')

elif '0'in ad or'1'in ad or'2'in ad or'3'in ad or'4'in ad or'5'in ad or'6'in ad or'7'in ad or'8'in ad or'9'in ad:
     print('Kullanıcı adı için rakam kullanmayınız!')
    
else:
    if 2<len(ad)<19:
        password=input('''Şifrenizi giriniz! Gireceğiniz şifre
6-12 karakter uzunluğunda olamalıdır.\n=''')

        if 5<len(password)<13:
            dosya=open('Kullanıcı biligileri.txt.','w')
            print('Bilgileriniz kaydediliyor.')
            print('Kullanıcı adınız =', ad,'\n','Şifreniz =', password,sep='')            
            print('Kullanıcı adınız =', ad,'\n','Şifreniz =', password,file=dosya,sep='')
            dosya.close()

        else:
            print('Şifrenizi belirtilen şekilde giriniz!')
    
    else:
            print('Kullanıcı adınızın uzunluğunu belirtilen aralıkta giriniz!')


   
     
