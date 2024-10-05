'''le sapin de noel'''
ht = int(input("quelle est la hauteur du sapin ? "))
def sapin(ht):
    num = ht+1
    for n in range(num):
        if n== 0:
            print(("_"*(num-1))+ ("*") + ("_"*(num-1)))
        else:
            print(("_"*(num-n-1))+(("*"))+("_"*(n))+(("_"*(n-1))+(("*"))+("_"*(num-n-1))))
sapin(ht)



"""1)  La TVA sur les produits est de 21%
Demandez à un utilisateur d'encoder le prix d'un article HTVA et afficher le résultat avec la TVA comprise.
Exemple: 100 € ==> 121€"""

HTVA = float(input("quelle est le prix htva ?  "))
print("le pris TVA comprise est de ", HTVA + (HTVA/100)*21)



"""2) Demandez à l'utilisateur d'encoder les 3 longueurs d'un triangle (valeurs entières)
Si la somme de 2 des côtés est supérieure ou égale au troisième côté, alors il faut afficher "c'est un triangle".  Si pas, vous devez afficher "Ce n'est pas un triangle"
Exemples:  
10, 20, 10 => C'est un triangle
10, 10, 10 => Ce n'est pas un triangle"""

list1 = []
ntlist = []
cotes = input("entre les trois valeur separe par une , :")
list1 = cotes.split(", ")
for i in list1:
    ntlist.append(int(i))
if (ntlist[0] <= (ntlist[1] + ntlist[2])) or (ntlist[1] <= (ntlist[0] + ntlist[2])) or (ntlist[2] <= (ntlist[0] + ntlist[1])):
    print("c'est un triangle")
else:
    print("ce n'est pas un triangle")



"""3) On demande à un utilisateur d'encoder une date: jour, mois année (3 valeurs entières)
- on doit vérifier si l'année est correcte (entre 0 et 2999)
- on doit vérifier si le mois encodé est correct (1 - 12)
- on doit vérifier si le jour est correct: 28, 29, 30 ou 31 jours suivant les conditions suivantes:
* Si le mois a 30 jours (avril, juin, septembre, novembre), le nombre de jours maximum est 30
* Si le mois a 31 jours (janvier, mars, mai, juillet, août, octobre, décembre), le nombre de jours maximum est 31
* Si le mois est février et l'année est bissextile, le nombre de jours maximum est 29.
* Si le mois est février et l'année n'est pas bissextile, le nombre de jours maximum est 28.
Si la date est correcte, afficher "date correcte".  Si pas, afficher 'date invalide".
Exemple: 
01/01/1980 => date correcte
28/02/2000 => date correcte
29/02/2023 => date incorrecte"""


while True:
    list = []
    intlist = []
    listmoispair = [4,6,9,11]
    try:
        cotes = input("quelle est la date a verifier ? : ")
        list = cotes.split("/")
        for num in list:
            intlist.append(int(num))

        #verifie le nbr de jour dans le mois.
        def test_moipair():
            listmoispair = [4,6,9,11]
            for i in listmoispair:
                if intlist[1] == i and intlist[0] > (30):
                    return True
                        
        def test_impairmoi():
            listmoisimpaire = [1, 3, 5, 7, 8, 10, 12]
            for z in listmoisimpaire:
                if intlist[1] == z and intlist[0] > (31):
                    return True
                        
        def febu_test():
            if intlist[2]%4 == 0 and intlist[0] <= (29):
                return True
            elif intlist[1] == 2 and intlist[0] > (28):
                return False

        if len(intlist) != 3:
            print("date incorrect")

        #verifie si jour/annees/mois mois ne sort pas des faits. 
        elif (intlist[2] > 2999 or intlist[2] < 0) or (intlist[1] > 12 or intlist[1] < 1) or (intlist[0] <= 0):  
            print("date incorrect") 

        elif test_impairmoi() == True:
            print("date incorrect")

        elif test_moipair() == True:
            print("date incorrect")

        elif febu_test() == False:
            print("date incorrect")
        else:
            print("date correct")

    except ValueError: 
        print("une date ce compose de valeur entiere note de la maniere suivante : j/m/a")
    
