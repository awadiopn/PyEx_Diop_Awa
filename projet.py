#importation fichier
from csv import DictReader
fichier=[]
file=open("file.csv",'r',encoding="utf8")
csv_reader=DictReader(file)
fichier_transform = list(csv_reader)
for row in fichier_transform:
    del row['CODE']
    fichier.append(row)
file.close()
# on supprime tout les espaces et stocker dans new_fichier
new_fichier=[]
for row in fichier:
    if row["Numero"]!=""or row["Date de naissance"]!=""or row["Nom"]!=""or row["Prénom"]!=""or row["Classe"]!=""or row["Note"]!="":
        new_fichier.append(row)
print(new_fichier)
#fonction numero valide

def numvalide(num):
    if len(num)==7 and num.isalnum() and num.isupper():
        return True
    else:
        return False

    #fonction prenom valide
    
def Prenomvalide(prenom):
    if len(prenom)>=3 and prenom[0].isalpha():
         return True
    else:
         return False
#fonction nom valide

def nomvalide(nom):
    if len(nom)>=2 and nom[0].isalpha():
        return True
    else:
        return False
    #fonction date valide

def dateval(m):
    m=m.lower()
    if m in ["janvier","janv"]:
        return '01'
    elif m in ["fevrier","février","fev","févr"]:
        return '02'
    elif m in "mars":
        return '03'
    elif m in "avril":
        return '04'
    elif m in "mai":
        return '05'
    elif m in "juin":
        return '06'
    elif m in "juillet":
        return '07'
    elif m in ["août","aout"]:
        return '08'
    elif m in "septembre":
        return '09'
    elif m in "octobre":
        return '10'
    elif m in "novembre":
        return '11'
    elif m in "decembre":
        return '12'
 from datetime import date
def datevalide(j,m,a):
    try:
        y=date(a,m,j)
        return True
    except ValueError:
        return False
j=int(3)
m=int(2)
a=int(2000)
print(datevalide(j,m,a))

import re
def transdate(x):
    x=(re.split("[. _/,;:-]", x))
    n=len(x)
    i=0
    while i<n:
        if x[i]=="":
            del x[i]
            n=n-1
            i=i-1
        i+=1
    if x[1].isalpha():
        x[1]=dateval(x[1])
        j=x[0]
        m=x[1]
        a=x[2]
        j=int(j)
        m=int(m)
        a=int(a)
    else:
        j=x[0]
        m=x[1]
        a=x[2]
        j=int(j)
        m=int(m)
        a=int(a)
            
    if datevalide(j,m,a):
        j=str(j)
        m=str(m)
        a=str(a)
        ndate=j+"/"+m+"/"+a
        return ndate
    else:
        return None
   #fonction classe valide
     
def classeval(chaine):
    chaine=chaine.strip()
    if chaine.isspace() == False and len(chaine) > 1:
        if (chaine[0] in ['6','5','4','3']) and (chaine[-1] in ['A','B']):
            return True
        else:
            return False

def moyennes(notes):
    valide = True
    moyDev = 0
    moyMatiere = 0
    moySemestre = 0
    try:
        notes=notes.split("#")
        note=notes[0]
        for i in range(len(notes)):
            a=str(notes[i])
            a=a.replace("]","")
            a=a.split("[")
            a1=a[1]
            devoirs=a1.split(":")
            if len(devoirs)!=2:
                valide=False
            else:
                exam=int(devoirs[1])
                if exam <0 or exam>20:
                    valide=False
                else :
                    devoir=str(devoirs[0])
                    devoir=devoir.split(";")
                    for i in range (len(devoir)):
                        dev = devoir[i]
                        dev = int(dev)
                        if dev<0 or dev>20:
                            valide=False
                        else:
                            moyDev = moyDev + dev
                    if valide == True:
                        moyDev = float(moyDev/len(devoir))
                        moyMatiere= (moyDev + (2 * exam))/3
                    moyDev = 0
                    moySemestre=moyMatiere+moySemestre
        if valide==True:
            moySemestre=float(moySemestre/len(notes))
        if valide == False:
            valide = "les notes ne sont pas valides"
        elif valide != False:
            valide = "les notes sont valides"
    except ValueError:
        return False
    return valide

listevalide=[]
listeinvalide=[]
for row in new_fichier:
    row["Date de naissance"]=transdate(row["Date de naissance"])
    row["Classe"]=classeval(row["Classe"])  
    if numvalide(row["Numero"]) and Prenomvalide(row["Prénom"]) and nomvalide(row["Nom"]) and row["Date de naissance"]!=None and row["Classe"]!=None:
        listevalide.append(row)
    else:
        listeinvalide.append(row)
def Menu():
    print("Entrer le numéro de l' élève pour voir ses informations")
    print("1:liste des élèves valides")
    print("2:liste des élèves invalides")
    print("3:voir les cinq premiers de la liste")
    print("4: modifier une information invalide")