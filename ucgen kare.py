#Kullanıcıya üçgen veya dikdörtgen seçimi yaptırıp
#girlen uzunluklarla ne tür şekil elde edilebileceğini belitir.

sekil=input('''Oluşturmak isediğiniz şekil üçgen
ise 1\'e, dörtgen ise 2\'ye basınız.\n''')
if sekil=='1':
    print('Üçgen için üç tane uzunluk giriniz!')
    u1=float(input('1.uzunluk = '))
    u2=float(input('2.uzunluk = '))
    u3=float(input('3.uzunluk = '))

    if abs(u1-u2)<u3<u1+u2 and abs(u1-u3)<u2<u1+u3 and abs(u3-u2)<u1<u3+u2:

        if u1==u2==u3:
            print('Girdiğiniz uzunluklar ile eşkenar üçgen oluşturulabilir.')

        elif u1==u2!=u3 or u1==u3!=u2 or u3==u2!=u1:
            print('Girdiğiniz uzunluklar ile ikizkenar üçgen oluşturulabilir.')

        else:
            print('Girdiğiniz uzunluklar ile çeşit kenar üçgen oluşturulabilir.')
            
    else:
        print('Girdiğiniz uzunluklar ile bir üçgen oluşturulamaz.')

elif sekil=='2':
    print('Dörtgen için dört tane uzunluk giriniz!')
    u1=float(input('1.uzunluk = '))
    u2=float(input('2.uzunluk = '))
    u3=float(input('3.uzunluk = '))
    u4=float(input('4.uzunluk = '))

    if u1==u2==u3==u4:
        print('Giridğiniz uzunluklar ile kare oluşturulabilir.')

    elif (u1==u2 and u3==u4) or (u1==u3 and u2==u4) or (u1==u4 and u2==u3):
        print('Giridğiniz uzunluklar ile dikdörtgen oluşturulabilir.')

    else:
        print('Girdiğiniz uzunluklar ile bir kare veya dikdöretgen oluşturulamaz.')
else:
    print('Lütfen sizden istenen seçeneklerden birini seçiniz!')
        

        
        
            
    
