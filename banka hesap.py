#ATM:hasap bakiye bilgisi verir

hesap=1000

islem=input('''Hangi islemi yapmak istediginizi seçiniz.
Bakiye kontrol için 1'e,
Para yatırmak için 2'ye,
Para çekmek için 3'e basınız.\n=''')

if islem=='1':
    print('Hesabinizda {} euro para bulunmaktadir.'.format(hesap))

elif islem=='2':
    yatırılan=int(input('Lütfen yatırmak istediğiniz miktarı giriniz\n='))
    hesap+=yatırılan
    print('''Hesabiniza {} euro para yatirildi.
Yeni bakiyeniz {} euro'''.format(yatırılan,hesap))

elif islem=='3':
    cekilen=int(input('Çekmek istediğiniz tutarı giriniz\n='))

    if cekilen>hesap:
        print('Yetersiz bakiye.')

    else:
        hesap-=cekilen
        print('''Hesabınızdan {} euro çekildi.
Kalan bakiyeniz {} euro.'''.format(cekilen,hesap))

else:
    print('Size belirten seçeneklerden birini seçmediniz!')
