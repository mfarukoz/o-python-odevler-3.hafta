
sayı='3'
tahmin=input('1-10 arsında bir sayı tahmin ediniz.\n')
if sayı==tahmin:
    print('Tebrikler,ilk denemede bildiniz.')
    sus=len('Tebrikler,ilk denemede bildiniz.')
    print('-'*((sus-7)//2),'\u2604'*3,'-'*((sus-7)//2))

elif sayı!=tahmin:
    tahmin=input('Bilemediniz. 2. tahmiminizi nedir?\n')

    if sayı==tahmin:
        print('Tebrikler,ikinci denemede bildiniz.')
        sus=len('Tebrikler,ikinci denemede bildiniz.')
        print('-'*((sus-6)//2),'\u2605'*2,'-'*((sus-6)//2))

    elif sayı!=tahmin:
        tahmin=input('Bilemediniz. 3. tahmiminizi nedir?\n')

        if sayı==tahmin:
            print('Tebrikler,üçüncü denemede bildiniz.')
            sus=len('Tebrikler,üçüncü denemede bildiniz.')
            print('-'*((sus-3)//2),'\u2605','-'*((sus-4)//2))

        else:
            print('Üç denemede de bilemediniz.')
            
        
        
          


