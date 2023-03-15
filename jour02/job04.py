import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="azerty",
    database="LaPlateforme"
)

# Récupération des données de la table "salles"
mycursor = mydb.cursor()
mycursor.execute("SELECT nom, capacite FROM salles")
result = mycursor.fetchall()

# Affichage des résultats
for x in result:
    print(x)
