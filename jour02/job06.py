import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="azerty",
    database="LaPlateforme"
)

# Exécution de la requête SQL
cursor = conn.cursor()
cursor.execute("SELECT SUM(capacite) FROM salles;")
result = cursor.fetchone()

# Affichage du résultat
capacite_totale = result[0]
print("La capacite de toute les salles est de : {}".format(capacite_totale))

# Fermeture de la connexion à la base de données
conn.close()