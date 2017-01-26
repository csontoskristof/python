#F0002a: Melyik állat nevét nem írja ki a program? (Csak a válasz megadását követően ér lefuttatni a programot:))
cica = 'kutya'
kutya = 'egér'
egér = 'cica'
print(cica) #Ezt nem írja ki
print('kutya')
print(egér)
print('cica')

#F0002b: Mi lesz kiírva a program kimenetének utolsó sorában?
cica = 'kutya'
print(cica)
kutya = 'egér'
egér = 'cica'
print('kutya')
cica = 'tyúk'
print(egér)
kutya = cica
print('kutya')
print(kutya)
#kutya
#kutya
#cica
#kutya
#tyúk

#F0002c: Hány sornyi kiírás, azaz szöveg és üres sor kerül a képernyőre, ha majd egyszer lefuttatod ezt a programot?	
print('Első sor\n')
print('\nNos?')
print('Azaz?\n')
print('\nAkkor most mennyi?\n\n')
print('Utolsó sor')
#9

#F0002d: Rajzold ki egyetlen print() utasítással az alábbi ábrát! (Megoldás itt.) (Ennek a feladatnak – meg a következő kettőnek – az ötlete innen származik.)
print("     /\n    /\n   /\n  /\n /\n")

#F0002e: Ha visszapert (backslash, “\”) akarunk kiírni a print()-tel, akkor az utasításban két visszapert kell írnunk, mert az első arra jó, hogy levédje az utána álló karaktert, mint a \n esetén már láttad. Ennek fényében: Rajzold ki egyetlen print() utasítással az alábbi ábrát! (Megoldás itt.)
print("\\\n \\\n  \\\n   \\\n    \\\n     \\\n")

#F0002f: Rajzold ki egyetlen print() utasítással az alábbi ábrát! (Megoldás itt.)
print("\\    /\n \\  /\n  \\/\n")
