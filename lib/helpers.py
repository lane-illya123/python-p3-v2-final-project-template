# lib/helpers.py
from models.book import Book
from models.recipe import Recipes


def exit_program():
    print("Goodbye!")
    exit()

def view_all_cat():
    categorys = Book.get_all()
    for category in categorys:
        print(f"Name: {category.name}")    

def veiw_all_recipes():

    lists = Recipes.get_all()
    for list in lists:
        print(f"Name: {list.name}, Description: {list.description}, Prep Time: {list.prep_time}mins")

def recipes_by_category():
    name = input("Enter a category: ")
    print(f"Name entered: {name}")
    category = Book.find_by_name(name)

    if category:
        recipes = category.recipes()
        for recipe in recipes:
            print(f"Name: {recipe.name},Description: {recipe.description},Prep Time: {recipe.prep_time}mins")
    else:
        print(f"Category {name} not found.")

def new_recipe():
    
    name=input("Enter Name of Recipe:")
    description=input("Description of Recipe:")
    prep_time_input=input("Enter The Prep Time: ")
    prep_time=int(prep_time_input)
    print("Enter the number of the category the new recipe fall under:")
    categorys = Book.get_all()
    
    for i, cat in enumerate(categorys, start=1):
        print(f"{i}. {cat.name}")
     
    try:
        category_input = input()
        category = int(category_input)
    except ValueError:
        print("Invalid input. Please enter a numeric category number.")
        return

    try:
        new_item = Recipes.create(name, description, prep_time, category)
        print(f'Success: {new_item.name}, Description: {new_item.description}, Prep Time: {new_item.prep_time}mins')
    except Exception as exc:
        print("Error creating new recipe: ", exc)

def update_recipe():

    name = input("Enter the current recipe name: ")
    if edit_recipe := Recipes.find_by_name(name):
        try:
            name = input("Enter the Recipe new name: ")
            edit_recipe.name = name
            description = input("Enter the new description of recipe: ")
            edit_recipe.description = description
            edit_prep = input("Enter new prep time:")
            edit_recipe.prep_time = int(edit_prep)
            print("Enter the number of the new category:")
            categorys = Book.get_all()
            
            for i, cat in enumerate(categorys, start=1):
                print(f"{i}. {cat.name}")
            
            try:
                category_input = input()
                edit_recipe.category_id = int(category_input)
            except ValueError:
                print("Invalid input. Please enter a numeric category number.")
                return
            edit_recipe.update()
            print(f'Success: {edit_recipe.name}, Description: {edit_recipe.description}, Prep Time: {edit_recipe.prep_time}mins')
        except Exception as exc:
            print("Error updating recipe: ", exc)
    else:
        print((f'Recipe {name} not found \n'))
        recipes = Recipes.get_all()
        for recipe in recipes:

            print(f'Avalible Recipes: {recipe.name} \n')

def delete_recipe():
    name = input("Enter the recipe name: ")
    if bye_recipe := Recipes.find_by_name(name):
        bye_recipe.delete()
        print(f'Recipe {name} deleted')
    else:
        print(f'Recipe {name} not found')

def new_cat():
    new_name=input("Enter new category name:")

    try:
        new_item = Book.create(new_name)
        print(f'Success: {new_item.name}')
    except Exception as exc:
        print("Error creating new category: ", exc)

def edit_cat():
    name=input("Enter name of a category:")
    if edit_category := Book.find_by_name(name):
        try:
            name = input("Enter the category new name: ")
            edit_category.name = name

            edit_category.update()
            print(f'Success: {edit_category.name}')
        except Exception as exc:
            print("Error updating category: ", exc)
    else:
        print((f'Category {name} not found \n'))
        lists = Book.get_all()
        for list in lists:

            print(f'Avalible Categorys: {list} \n')

def delete_cat():
    name = input("Enter the recipe name: ")
    if bye_recipe := Book.find_by_name(name):
        bye_recipe.delete()
        print(f'Category {name} deleted')
    else:
        print(f'Category {name} not found')    

