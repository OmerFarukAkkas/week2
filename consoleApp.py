import random

student1 = {'isim':'Omer Faruk' , 'soyisim':'Akkas' , 'numara':1140110000+random.randint(0,1000) , 'sinif':random.randint(1,4)}
student2 = {'isim':'Adil' , 'soyisim':'Batur' , 'numara':1140110000+random.randint(0,1000) , 'sinif':random.randint(1,4)}
student3 = {'isim':'Batuhan' , 'soyisim':'Ak' , 'numara':1140110000+random.randint(0,1000) , 'sinif':random.randint(1,4)}
student4 = {'isim':'Kursat' , 'soyisim':'Akin' , 'numara':1140110000+random.randint(0,1000) , 'sinif':random.randint(1,4)}
student5 = {'isim':'Mustafa' , 'soyisim':'Sen' , 'numara':1140110000+random.randint(0,1000) , 'sinif':random.randint(1,4)}

print(student1)
print(student2)
print(student3)
print(student4)
print(student5)

numaralar = [student1['numara'] , student2['numara'] , student3['numara'] , student4['numara'] , student5['numara']]

cift=[]
tek=[]

for x in numaralar : 
    if x%2==0:
        cift.append(x)
    else:
        tek.append(x)

print(f"tek numaralar :{tek}" , f"cift numaralar: {cift}")