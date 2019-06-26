#ODEV:girilen 2 vize 1 final notunun yüzdelerini hesapalar
#ve ders notunu veerir.

vize1=float(input('1. vize notunuzu giriniz = '))
vize2=float(input('2. vize notunuzu giriniz = '))
final=float(input('Final notunuzu giriniz = '))

top_not=vize1*0.3+vize2*0.3+final*0.4

if 90<=top_not<=100:
    print('Ders notunuz {} = AA'.format(top_not))

elif 85<=top_not:
    print('Ders notunuz {} = BA'.format(top_not))

elif 80<=top_not:
    print('Ders notunuz {} = BB'.format(top_not))

elif 75<=top_not:
    print('Ders notunuz {} = CB'.format(top_not))

elif 70<=top_not:
    print('Ders notunuz {} = CC'.format(top_not))

elif 65<=top_not:
    print('Ders notunuz {} = DC'.format(top_not))

elif 60<=top_not:
    print('Ders notunuz {} = DD'.format(top_not))

elif 55<=top_not:
    print('Ders notunuz {} = FD'.format(top_not))

elif 0<=top_not:
    print('Ders notunuz {} = FF'.format(top_not))

else:
    print('Girdiğiniz notlar 0-100 aralığında olamalıdır!')
