import mysql.connector
import csv
class Product_manager:

    def __init__(self, user, password, database, host='localhost'):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        self.products = []

    def create_produit(self, nom,description,prix, quantite,id_categorie):
        query = "INSERT INTO produit (nom, description,prix, quantité, id_catégorie) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, description,prix, quantite,id_categorie)
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def get_produit(self, categorie=None):
        query = "SELECT * FROM produit"
        if categorie:
            query += " WHERE id_catégorie = %s"
            self.cursor.execute(query, (categorie,))
        else:
            self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            for row in result:
                self.products.append({
                    'nom': row[1],
                    'description': row[2],
                    'quantite': row[4],
                    'prix': row[3],
                    'id_categorie': row[5]
                })
            return self.products

        else:
            return None

    def update_produit(self, id, nom=None, description=None,prix=None, quantite=None, id_categorie=None):
        query = "UPDATE produit SET "
        values = []
        if nom is not None:
            query += "nom = %s, "
            values.append(nom)
        if description is not None:
            query += "description = %s, "
            values.append(description)
        if prix is not None:
            query += "prix = %s, "
            values.append(prix)
        if quantite is not None:
            query += "quantite = %s, "
            values.append(quantite)
        if id_categorie is not None:
            query += "id_categorie = %s, "
            values.append(id_categorie)
        query = query[:-2] + " WHERE id = %s"
        values.append(id)
        self.cursor.execute(query, values)

    def delete_produit(self, nom):
        query = "DELETE FROM produit WHERE nom = %s"
        values = (nom,)
        self.cursor.execute(query, values)
        self.connection.commit()
        return True

    def get_all_categorie(self):
        query = "SELECT * FROM categorie"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return None

    def get_one_categorie(self, categorie):
        id_cat = self.get_categorie(categorie)
        if id_cat:
            return self.get_produit(id_cat)

    def delete_category(self, categorie):
        id_cat = self.get_categorie(categorie)
        if id_cat:
            query = "DELETE FROM categorie WHERE id = %s"
            values = (id_cat,)
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        else:
            return False

    def get_categorie(self, id):
        query = "SELECT id FROM categorie WHERE nom = %s"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def add_category(self, nom):
        query = "INSERT INTO categorie (nom) VALUES (%s)"
        values = (nom,)
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def CVS_export(self, categorie=None):
        query = "SELECT * FROM produit"
        if categorie:
            categorie_id = self.get_categorie(categorie)
            query += f" WHERE id_catégorie = {categorie_id}"
        self.cursor.execute(query)
        with open('produit.csv', 'w+',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'nom', 'description', 'prix', 'quantité', 'id_catégorie'])
            for row in self.cursor:
                writer.writerow(row)




product_manager = Product_manager('root', 'azerty', 'boutique')
