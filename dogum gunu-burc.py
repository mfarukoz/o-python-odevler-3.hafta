#Kullanıcıdan dogum tarihi girmesini isteyip
#bucunu bulan program

while True:
    ay_kontrol=input('Kaçıncı ayda doğduğunuzu sayı olarak giriniz = ')
    gun_kontrol=input('Doğum tarihinizin gününü sayı olarak giriniz = ')
    number1='123456789101112'
    number2='123456789010111213141516171819202122232425262728293031'
    if not ay_kontrol or not gun_kontrol:
        print('Doğum tarihi bilgilerinizi boş bırakmayınız!\n')
        continue 
    
    if ay_kontrol not in number1 or gun_kontrol not in number2:
        print('Doğum tarihi bilgilerinizi uygun sayılar olarak giriniz!\n')
        continue

    ay=int(ay_kontrol)
    gun=int(gun_kontrol)

    if ay==1:
        if 0<gun<22:
            print('Oğlak burcundansınız.')   #Oğlak Burcu : 22 Aralık - 21 Ocak
        elif 21<gun<32:
            print('Kova burcundansınız.')    #Kova Burcu : 22 Ocak - 19 Şubat
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')
        
    elif ay==2:
        if 0<gun<20:
            print('Kova burcundansınız.')    #Kova Burcu : 22 Ocak - 19 Şubat
        elif 19<gun<29:
            print('Balık burcundansınız.')   #Balık Burcu : 20 Şubat - 20 Mart
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')
        
    elif ay==3:
        if 0<gun<21:
            print('Oğlak burcundansınız.')   #Balık Burcu : 20 Şubat - 20 Mart
        elif 20<gun<32:
            print('Koç burcundansınız.')     #Koç Burcu : 21 Mart - 20 Nisan
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')

    elif ay==4:
        if 0<gun<21:
            print('Koç burcundansınız.')     #Koç Burcu : 21 Mart - 20 Nisan
        elif 20<gun<31:
            print('Boğa burcundansınız.')    #Boğa Burcu : 21 Nisan - 21 Mayıs
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')

    elif ay==5:
        if 0<gun<22:
            print('Boğa burcundansınız.')    #Boğa Burcu : 21 Nisan - 21 Mayıs  
        elif 21<gun<32:
            print('İkizler burcundansınız.') #İkizler Burcu : 22 Mayıs - 22 Haziran
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')

    elif ay==6:
        if 0<gun<23:
            print('İkizler burcundansınız.') #İkizler Burcu : 22 Mayıs - 22 Haziran
        elif 22<gun<31:
            print('Yengeç burcundansınız.')  #Yengeç Burcu : 23 Haziran - 22 Temmuz
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')
              
    elif ay==7:
        if 0<gun<23:
            print('Yengeç burcundansınız.')  #Yengeç Burcu : 23 Haziran - 22 Temmuz
        elif 22<gun<32:
            print('Aslan burcundansınız.')   #Aslan Burcu : 23 Temmuz - 22 Ağustos 
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')
    
              
    elif ay==8:
        if 0<gun<23:
            print('Aslan burcundansınız.')   #Aslan Burcu : 23 Temmuz - 22 Ağustos
        elif 22<gun<32:
            print('Başak burcundansınız.')   #Başak Burcu : 23 Ağustos - 22 Eylül
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')


    elif ay==9:
        if 0<gun<23:
            print('Başak burcundansınız.')   #Başak Burcu : 23 Ağustos - 22 Eylül
        elif 22<gun<31:
            print('Terazi burcundansınız.')  #Terazi Burcu : 23 Eylül - 22 Ekim
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')

    elif ay==10:
        if 0<gun<23:
            print('Terazi burcundasınız.')  #Terazi Burcu : 23 Eylül - 22 Ekim
        elif 22<gun<32:
            print('Akrep burcundasınız.')   #Akrep Burcu : 23 Ekim - 21 Kasım
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')
              
    elif ay==11:
        if 0<gun<22:
            print('Akrep burcundansınız.')   #Akrep Burcu : 23 Ekim - 21 Kasım
        elif 21<gun<31:
            print('Yay burcundansınız.')     #Yay Burcu : 22 Kasım - 21 Aralık
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')

    elif ay==12:
        if 0<gun<22:
            print('Terazi burcundansınız.')  #Yay Burcu : 22 Kasım - 21 Aralık
        elif 21<gun<32:
            print('Akrep burcundansınız.')   #Oğlak Burcu : 22 Aralık - 21 Ocak
        else:
            print('Lütfen doğum tarihinizin gününü doğru giriniz!')

    else:
        print('Doğum tarihinizin ayını doğru giriniz!')
              
    break          

        

