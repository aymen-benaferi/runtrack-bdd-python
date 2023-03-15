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
cursor.execute("SELECT SUM(superficie) AS superficie_totale FROM etage;")
result = cursor.fetchone()

# Affichage du résultat
superficie_totale = result[0]
print("La superficie de La Plateforme est de {} m2".format(superficie_totale))

# Fermeture de la connexion à la base de données
conn.close()
