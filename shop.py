import tkinter as tk
import pandas as pd
from product_manager import Product_manager
from tkinter import messagebox


product_manager = Product_manager('root', 'azerty', 'boutique')
root = tk.Tk()
root.title("Gestion du stock")
root.geometry("500x440")
root.minsize(500,380)
root.config(background='#41B77F')


def get_data():
    data = product_manager.get_produit()
    data_nom = [data[i]['nom'] for i in range(len(data))]
    data_prix = [data[i]['prix'] for i in range(len(data))]
    data_quantite = [data[i]['quantite'] for i in range(len(data))]
    data_id = [data[i]['id_categorie'] for i in range(len(data))]
    data_syntax = {'Nom': data_nom, 'Prix': data_prix, 'Quantité': data_quantite, 'ID': data_id}
    df = pd.DataFrame(data_syntax)

    # Clear the variables before returning the DataFrame
    data.clear()
    data_nom.clear()
    data_prix.clear()
    data_quantite.clear()
    data_id.clear()
    del data_syntax

    return df

#function

def add_product():
    new_product_window = tk.Toplevel(root, bg='grey')
    new_product_window.title("Nouveau produit")
    new_product_window.geometry("300x300")
    # Créer des champs de saisie pour le nom, la description, le prix, la quantité et l'id de la catégorie du nouveau produit
    tk.Label(new_product_window, text="Nom :",bg='grey',fg="white").grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(new_product_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(new_product_window, text="Description :",bg='grey',fg="white").grid(row=1, column=0, padx=10, pady=10)
    description_entry = tk.Entry(new_product_window)
    description_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(new_product_window, text="Prix :",bg='grey',fg="white").grid(row=2, column=0, padx=10, pady=10)
    price_entry = tk.Entry(new_product_window)
    price_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(new_product_window, text="Quantité :",bg='grey',fg="white").grid(row=3, column=0, padx=10, pady=10)
    quantity_entry = tk.Entry(new_product_window)
    quantity_entry.grid(row=3, column=1, padx=10, pady=10)

    tk.Label(new_product_window, text="ID de catégorie :",bg='grey',fg="white").grid(row=4, column=0, padx=10, pady=10)
    category_id_entry = tk.Entry(new_product_window)
    category_id_entry.grid(row=4, column=1, padx=10, pady=10)

    tk.Button(new_product_window, text="Sauvegarder",bg='grey',fg="white",width=20,height=2,
              command=lambda: save_product()).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    def save_product():
        # Récupérer les valeurs des champs de saisie
        name = name_entry.get()
        description = description_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()
        category_id = category_id_entry.get()

        # Vérifier que tous les champs sont remplis
        if name == "" or description == "" or price == "" or quantity == "" or category_id == "":
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        else:
            product_manager.create_produit(name, description, price, quantity, category_id)
            reset_table(table)
            messagebox.showinfo("Succès", "Le produit a bien été ajouté.")
            new_product_window.destroy()

def remove_product():
    new_product_window = tk.Toplevel(root, bg='grey')
    new_product_window.title("Supprimer un produit")
    new_product_window.geometry("300x300")
    # Créer des champs de saisie pour le nom, la description, le prix, la quantité et l'id de la catégorie du nouveau produit
    tk.Label(new_product_window, text="Nom :", bg='grey', fg="white").grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(new_product_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Button(new_product_window, text="Suprimer", bg='grey', fg="white", width=20, height=2,
              command=lambda:remove())\
                .grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def remove():
        if name_entry.get() == "":
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        else:
            nom = name_entry.get()
            product_manager.delete_produit(nom)
            reset_table(table)
            messagebox.showinfo("Succès", "Le produit a bien été supprimé.")

def modify_product():
    new_product_window = tk.Toplevel(root, bg='grey')
    new_product_window.title("Modifier un produit")
    new_product_window.geometry("300x300")
    # Créer des champs de saisie pour le nom, la description, le prix, la quantité et l'id de la catégorie du nouveau produit
    tk.Label(new_product_window, text="Nom :", bg='grey', fg="white").grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(new_product_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Label(new_product_window, text="Description :", bg='grey', fg="white").grid(row=1, column=0, padx=10,
                                                                                   pady=10)
    description_entry = tk.Entry(new_product_window)
    description_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(new_product_window, text="Prix :", bg='grey', fg="white").grid(row=2, column=0, padx=10, pady=10)
    price_entry = tk.Entry(new_product_window)
    price_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(new_product_window, text="Quantité :", bg='grey', fg="white").grid(row=3, column=0, padx=10, pady=10)
    quantity_entry = tk.Entry(new_product_window)
    quantity_entry.grid(row=3, column=1, padx=10, pady=10)

    tk.Label(new_product_window, text="ID de catégorie :", bg='grey', fg="white").grid(row=4, column=0, padx=10,
                                                                                       pady=10)
    category_id_entry = tk.Entry(new_product_window)
    category_id_entry.grid(row=4, column=1, padx=10, pady=10)

    tk.Button(new_product_window, text="Sauvegarder", bg='grey', fg="white", width=20, height=2,
              command=lambda :valid_modification()).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def valid_modification():
        name = name_entry.get()
        description = description_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()
        category_id = category_id_entry.get()
        print(name, description, price, quantity, category_id)
        product_manager.update_produit(name, description, price, quantity, category_id)
        reset_table(table)
        messagebox.showinfo("Succès", "Le produit a bien été modifié.")
        new_product_window.destroy()

def reset_table(table):
    table.configure(text=get_data().to_string(index=False))


# Frame
frame = tk.Frame(root, bg='#41B77F')
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

canvas = tk.Canvas(root, width=800, height=300, bg='white')
canvas.pack()

table = tk.Label(canvas, text=get_data().to_string(index=False),font='Consolas 16', justify='left',fg='white', bg='grey',
                 width=800,height=500 , anchor='nw',pady=20)
table.pack(expand=True)


# Label

label_title = tk.Label(frame, text="Gestion du stock", font=("Courrier", 25), bg='#41B77F', fg='white')
label_title.pack()

# menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Produit", menu=file_menu)
file_menu.add_command(label="Ajouter un produit", command=add_product)
file_menu.add_command(label="Modifier un produit", command=modify_product)
file_menu.add_command(label="Supprimer un produit", command=remove_product)

# Tableau
root.mainloop()



