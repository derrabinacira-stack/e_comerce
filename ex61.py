import json

def afficher_produits(produits):
    f = open("produits.json", "r")

    produits = json.load(f)

    f.close()

    return produits

def lire_panier():
    f = open("cart.json", "r")

    panier = json.load(f)

    f.close()


    return panier



def sauvegarder_panier(panier):

    f = open("cart.json", "w")

    json.dump(panier, f, indent=4)

    f.close()


def sauvegarder_produits(produits):
    f = open("products.json", "w")

    json.dump(produits, f, indent=4)
    f.close()

 
   
produits = afficher_produits("produits.json") 
print(produits)
 
def ajouter_panier():
    for produit in produits:
        print(f"{produit['id']}: {produit['name']} - ${produit['price']}")
    choix = int(input("Entrez l'id du produit à ajouter au panier: "))

    for produit in produits:
        if produit['id'] == choix:
            panier.append(produit)
            break
    else:
        print("Produit non trouvé.")
