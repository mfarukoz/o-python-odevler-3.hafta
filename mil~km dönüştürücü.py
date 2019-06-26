# Kullanicadan 2 input alinacak:
#1-km-mil donusumu mu yapmak istiyor, mil-km donusumu mu yapmak istiyor.
#2-donusturmek istedigi birimin uzunlugu kactir?
#Donusum yapilacak birimler mil ve kilometre olacak.
    

km_mil=input('''Km\'yi Mil\'e dönüştürmek için 1\'e,
Mil\'i Km\'ye dönüştürmek için ise 2\'ye basınız!''')

if km_mil=='1':
    km=input('''km cinsinden meafeyi giriniz.
(Not:ondalıklı değerler için nokta kullanınız)
    = ''')
    mil=float(km)*0.6214
    print(km,'km',' ',mil,'mil\'dir.',sep='')
    print(type(mil))
elif km_mil=='2':
    mil=input('''mil cinsinden meafeyi giriniz.
(Not:ondalıklı değerler için nokta kullanınız)
    = ''')
    km=float(mil)/0.6214
    print(mil,'mil',' ',km,'km\'dir.',sep='')

else:
    print('Size belirtilen seçeneklerden birini girmediniz!')
    
    
    
    
    

