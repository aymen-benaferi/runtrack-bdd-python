import mysql.connector

# se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="azerty",
    database="LaPlateforme"
)

# créer un curseur pour exécuter des requêtes
cursor = conn.cursor()

# exécuter une requête pour récupérer tous les étudiants
query = "SELECT * FROM etudiants"
cursor.execute(query)

# afficher le résultat de la requête
for student in cursor.fetchall():
    print(student)

# fermer la connexion et le curseur
cursor.close()
conn.close()
