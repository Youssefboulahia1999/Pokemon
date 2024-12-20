# class Pokemon:
#     def __init__(self, nom, type_pokemon, points_vie, attaque):
#         self.nom = nom
#         self.type_pokemon = type_pokemon
#         self.points_vie = points_vie
#         self.attaque = attaque

#     def attaquer(self, cible):
#         print(f"{self.nom} ({self.type_pokemon}) attaque {cible.nom} !")
#         cible.points_vie -= self.attaque
#         print(f"{cible.nom} a maintenant {cible.points_vie} points de vie restants.\n")


# class PokemonPlante(Pokemon):
#     def __init__(self, nom, points_vie, attaque):
#         super().__init__(nom, type_pokemon="Plante", points_vie=points_vie, attaque=attaque)

#     def attaquer(self, cible):
#         print(f" {self.nom} utilise une attaque de type PLANTE !")
#         super().attaquer(cible)


# class PokemonEau(Pokemon):
#     def __init__(self, nom, points_vie, attaque):
#         super().__init__(nom, type_pokemon="Eau", points_vie=points_vie, attaque=attaque)

#     def attaquer(self, cible):
#         print(f" {self.nom} utilise une attaque de type EAU !")
#         super().attaquer(cible)


# class PokemonFeu(Pokemon):
#     def __init__(self, nom, points_vie, attaque):
#         super().__init__(nom, type_pokemon="Feu", points_vie=points_vie, attaque=attaque)

#     def attaquer(self, cible):
#         print(f" {self.nom} utilise une attaque de type FEU !")
#         super().attaquer(cible)


# # Exemple d'utilisation
# if __name__ == "__main__":
#     # Création des Pokémon avec des statistiques personnalisées
#     bulbizarre = PokemonPlante("Bulbizarre", points_vie=120, attaque=15)
#     carapuce = PokemonEau("Carapuce", points_vie=110, attaque=18)
#     salameche = PokemonFeu("Salamèche", points_vie=100, attaque=20)

#     # Combat entre les Pokémon
#     bulbizarre.attaquer(carapuce)
#     carapuce.attaquer(salameche)
#     salameche.attaquer(bulbizarre)



import mysql.connector
import random

# Fonction pour récupérer 5 Pokémon aléatoires depuis la base de données
def get_random_pokemons(cursor, nb_pokemons=5):
    query = f"SELECT * FROM pokemons ORDER BY RAND() LIMIT {nb_pokemons};"
    cursor.execute(query)
    return cursor.fetchall()

# Connexion à la base de données
try:
    conn = mysql.connector.connect(
        host="localhost",        
        user="root",             
        password="password",     
        database="pokedex"       
    )

    if conn.is_connected():
        print("Connexion réussie à la base de données!\n")

    # Création du curseur
    cursor = conn.cursor(dictionary=True)

    # Récupération des Pokémon pour les deux adversaires
    print(" Sélection des Pokémon pour les deux adversaires...\n")
    equipe_adversaire1 = get_random_pokemons(cursor)
    equipe_adversaire2 = get_random_pokemons(cursor)

    # Affichage des équipes
    print("⚔️ Équipe de l'Adversaire 1 :\n")
    for pokemon in equipe_adversaire1:
        print(f"Nom : {pokemon['nom']}, Type : {pokemon['type']}, "
              f"PV : {pokemon['points_vie']}, Attaque : {pokemon['attaque']}, "
              f"Défense : {pokemon['defense']}, Effet : {pokemon['effet']}")

    print("\n⚔️ Équipe de l'Adversaire 2 :\n")
    for pokemon in equipe_adversaire2:
        print(f"Nom : {pokemon['nom']}, Type : {pokemon['type']}, "
              f"PV : {pokemon['points_vie']}, Attaque : {pokemon['attaque']}, "
              f"Défense : {pokemon['defense']}, Effet : {pokemon['effet']}")

except mysql.connector.Error as e:
    print("Erreur lors de la connexion à la base de données :", e)

finally:
    # Fermeture de la connexion
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("\n Connexion fermée.")
