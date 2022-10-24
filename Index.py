import math


print("Ca marche")
print ( 1+2 )

#Chez python, les commentaires s'ouvrent avec le dièse, ou hashtag pour faire jeune

maVariable = input("Donnez un chiffre, ce que vous voulez")
monAutreVariable = 2
monEniemeVariable = 6

print(maVariable)

#C'est très simpliste pour l'écriture des if
#On se contente de dire direct la condition puis : pour dire voilà alors ce que tu fais
#Visiblement le else if s'appelle ici elif ET PAS AUTREMENT (j'ai testé), là ils ont voulu faire TROP simple
#Le résultat d'input est par défaut une string, 
#int convertit le résultat en integer(chiffres),
#mais float permet les décimales
if monEniemeVariable == float(maVariable)*3 :
    print("nickel chrome")

else : 
    print("ca cloche")

# les fonctions sont appelées def ici, pour define (comme pour définir nom de fonction)
# puis parenthèses des paramètres, et en fait, les {} sont remplacées par : en Python

def maFonction ():
    texte = "Fonctions en Python"
    print(texte)

def maFonctionAParametres (texte):
    
    print(texte)

maFonction()
maFonctionAParametres("salut")

#Parmis les bizarreries de Python, on note que && se voit grand remplacé par and
def calcul_age_ecole (age,nom) :
    if age < 5 :
        print("Tu est trop jeune petit", nom, "tu n'as encore que", age)
    elif age >= 5 and age < 20:
        print("J'espère que tu te feras plein de copains", nom)
    else:
        print("Tu est de l'élite du fofo ?")

calcul_age_ecole(25,"célestin") 

def calculAge(age):
    agePlus10 = age +10
    return agePlus10

#On peut print depuis la variable, je ne sait pas si ca se fait,
#et je n'en ai pas l'impression,
# mais c'est un gain de temps et de ligne
monAgeFutur = print(calculAge(17))

# boucle FOR
# Attention, range inclue le premier paramètres donné,  
# mais pas le second, 
# pour les arrays il comprends qu'il faut boucler
# pas besoin du paramétrage qu'on faisait en JS

for x in range(5,10):
    print(x)

jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

for j in jours:
    print(j)

fruits = ["banane", "pèche", "abricot", "pomme", "mure"]

#break rompt la boucle A PARTIR de l'élément que l'on précise
#On peut aussi skipper avec continue certains éléments de l'array
 
for f in fruits:
    if f==fruits[3] :break
    print(f)


#Plusieurs choses à noter

#math marche comme sur JS, mais c'est ici une librairie à importer
#Les bases de python sont vraiment archi simplistes
#L'écriture du code aussi est très voire trop simpliste
#Le cas le plus parlant : elif, qui sonne carrémment fainéant
#Python est encore très peu à l'assaut du web, par contre
#Recherche, finance, jeu vidéo, data, AI, il a trouvé sa voie !