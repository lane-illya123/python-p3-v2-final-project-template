from models.__init__ import CONN, CURSOR
from models.book import Book
from models.recipe import Recipes

def seed_database():
    Recipes.drop_table()
    Book.drop_table()
    Book.create_table()
    Recipes.create_table()

    #seed data
    app = Book.create("Appertizers")
    entree = Book.create("Entrees")
    dessert = Book.create("Desserts")

    Recipes.create("Buffalo Wings", "Wings tossed in buffalo sauce",30, app.id)
    Recipes.create("Cheese Burgar", "Fresh Burgar topped with Cheese",15, entree.id)
    Recipes.create("Strawberry Cheesecake", "Baked Cheesecake with strawberry puree",25, dessert.id)

seed_database()
print("Seeded database")