# Gérer une feuille d'appel/classe
# Dans une classe douze apprenants
# Gérer des absences/présences
# Ajouter/Supprimer des élèves
# Groupe d'élèves
# Tri par ordre alphabétique croissant, décroissant
# Ajouter des noms, prénoms, mail, age, sexe

# Listes : d'ID -> indice de la premiere liste
# Chaque ID renvoie à une liste comportant les informations des élèves
# [["Tramoy","Raphael","tramoy.raphael@hotmail.fr",18,"H"],["Yack", "Stephanie", "yack.stephanie@outlook.fr", 18, "F"],
# [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
# Ex : print list[0][1] -> les informations de raphael : Raphael


def ajouterEleve(nom, prenom, mail, age, sexe, list):
    list.append([nom, prenom, mail, age, sexe])
    afficherEleves(list)
    return list


def supprimerEleve(list):
    # ("Quel est le nom de l'élève à supprimer ?")
    # nom = input()

    for i in list[:]:
        if list[i][3] >= "34":
            del list[i]
            # i -= 1
    return list


def menuSuppEleve(list):
    print("De quelle manière souhaitez-vous supprimer l'élève ?")
    print("1 : Par nom")
    print("2 : Par preenom")
    print("3 : Par mail")
    print("4 : Par age")
    print("5 : Par sexe")
    choix = input()

    if choix != "4" and choix != "5":
        print("Quel est le nom/prenom/mail de l'élève à supprimer ?")
        nom = input()

        for i in range(len(list)):
            if list[i][int(choix) - 1] == nom:
                del list[i]
                return list
    elif choix == "4":
        print("Quel est l'age de l'élève à supprimer ?")
        age = input()

        listTmp = []

        for i in range(len(list)):
            if list[i][3] >= age:
                listTmp.insert(0, list[i])

        for j in range(len(listTmp)):
            list.remove(listTmp[j])

        return list

    elif choix == "5":
        print("Quel sexe voulez-vous radier de ce monde ?")
        sexe = input()

        listTmp = []

        for i in range(len(list)):
            if list[i][4] == sexe:
                listTmp.insert(0, list[i])

        for j in range(len(listTmp)):
            list.remove(listTmp[j])

        return list

    return list


def absence():
    print("hello")


def presence():
    print("hello")


def triCroissant():
    print("hello")


def triDecroissant():
    print("hello")


def afficherEleves(list):
    print(list)


def menuAjoutEleve(list):
    # A un moment un autre, cette fonction devra appeler ajouterEleve()
    # Cette fonction demande à l'utilisateur de renseigner les informations de l'élève
    # Après l'ajout de l'élève dans la liste, le menu retournera sur la page principale (menu())

    # return list

    print("Quel est votre nom ?")
    nom = input()
    print("Quel est votre prenom ?")
    prenom = input()
    print("Quel est votre age ?")
    age = input()
    print("Quel est votre sexe ?")
    sexe = input()
    mail = nom + "." + prenom + "@hotmail.fr"

    list = ajouterEleve(nom, prenom, mail, age, sexe, list)

    return list


def modifierEleve(list):
    # Dans liste il nous faudra repérer l'élève à modifier
    # Récupérer le champ à modifier
    # Modifier l'élève

    print("Veuillez renseigner le nom de l'élève à modifier")
    nom = input()

    for i in range(len(list)):
        if list[i][0] == nom:
            print(list[i])
            print("Quel champ (en nombre) souhaitez-vous modifier ? (1 : Nom, 2: Prenom, 3: Mail, 4: Age, 5: Sexe")
            champAMod = input()
            print("Quel valeur souhaitez vous mettre à la place ?")
            valAMettre = input()

            if champAMod == "1" or champAMod == "Nom":
                list[i][0] = valAMettre
                mail = list[i][0] + "." + list[i][1] + "@gmail.com"
                list[i][2] = mail
            elif champAMod == "2" or champAMod == "Prenom":
                list[i][1] = valAMettre
                mail = list[i][0] + "." + list[i][1] + "@gmail.com"
                list[i][2] = mail
            elif champAMod == "3" or champAMod == "Mail":
                list[i][2] = valAMettre
            elif champAMod == "4" or champAMod == "Age":
                list[i][3] = valAMettre
            elif champAMod == "5" or champAMod == "Sexe":
                list[i][4] = valAMettre
            else:
                print("T'es teuteu")
    return list


def remplacerEleve(list):
    # Le but de cette fonction est de remplacer tous les paramètres de l'élève

    print("Veuillez entrer le nom de l'élève")
    nom = input()
    print("Veuillez entrer le prenom de l'élève")
    prenom = input()
    mail = nom + "." + prenom + "@gmail.com"
    print("Veuillez entrer l'age de l'élève")
    age = input()
    flag1 = True
    while flag1:
        print("Veuillez entrer le sexe de l'élève")
        sexe = input()
        if sexe != "h" | sexe != "f":
            print("Sexe incorrecte : entre h ou f pour le sexe")
        else:
            return

    listEleveAMettre = [nom, prenom, mail, age, sexe]

    print("Quel le nom élève voulez-vous remplacer ?")
    nomEleveARemp = input()

    for i in range(len(list)):
        if list[i][0] == nomEleveARemp:
            list.pop(i)
            list.insert(i, listEleveAMettre)

    return list


def menu():
    list = [["Ye", "Alexis", "mail", "25", "H"], ["Mosca", "Corentin", "mail", "34", "H"],
            ["Denoun", "Medhi", "mail", "48", "N-B"]]
    flag = True

    print("Bonjour formateur, vous pouvez ici choisir une parmis les moultes options pour gérer votre classe :")

    while flag == True:
        print("1 : Ajouter un élève")
        print("2 : Supprimer un élève")
        print("3 : Rendre présent un élève")
        print("4 : Rendre absent un élève")
        print("5 : Afficher tous les élèves")
        print("6 : Afficher les élèves dans l'ordre croisssant-alphabétique des noms")
        print("7 : Afficher les élèves dans l'ordre décroisssant-alphabétique des noms")
        print("8 : Modifier un élève")  # Changer totalement l'élève
        print("9 : Remplacer un élève")  # Remplacer un seul paramètre de l'élève
        print("q : Sortir")

        choix = input()

        match choix:
            case "1":
                list = menuAjoutEleve(list)
            case "2":
                list = menuSuppEleve(list)
            case "3":
                presence()
            case "4":
                absence()
            case "5":
                afficherEleves(list)
            case "6":
                triCroissant()
            case "7":
                triDecroissant()
            case "8":
                modifierEleve(list)
            case "9":
                remplacerEleve(list)
            case "q":
                flag = False
                return
            case _:
                print("Erreur : Le choix demandé n'est pas attribué.")


def main():
    menu()


if __name__ == '__main__':
    main()
