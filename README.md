# Phase 3 CLI+ORM Project Template

## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

---

## Introduction

This project represent a recipe book. The user is able to create, edit, delete, and
 view recipes. Its also give users the ability to create, edit, delete category the 
 recipes belog too.

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── book.py
    │   ├── recipe.py
    │   └── seed.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input. Below is the list of options the users can enter.

The project has a CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    view_all_cat,
    veiw_all_recipes,
    recipes_by_category,
    new_recipe,
    update_recipe,
    delete_recipe,
    new_cat,
    edit_cat,
    delete_cat
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_all_cat()
        elif choice == "2":
            veiw_all_recipes()
        elif choice == "3":
            recipes_by_category()
        elif choice == "4":
            new_recipe()
        elif choice == "5":
            update_recipe()
        elif choice == "6":
            delete_recipe()
        elif choice == "7":
            new_cat()
        elif choice == "8":
            edit_cat()
        elif choice == "9":
            delete_cat()
        else:
            print("Choice Avalable Options")





def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View All Categorys")
    print("2. View All Recipes")
    print("3. View Recipes From a Category")
    print("4. Create a New Recipe")
    print("5. Update a Recipe")
    print("6. Delete Recipe")
    print("7. Create a New Category")
    print("8. Edit a Category")
    print("9. Delete Category")

if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

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
        new_item = Recipes.create(name, description, prep_time)
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
            name = input("Enter the department's new name: ")
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
```

You can run the CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The CLI will ask for input, call one
of the functions, and update the database. Some options will let you view the
database.

---

### Recipe and Book classes

These two classes have a one to many relationship. It can be only one category
but that category can have many recipes. The two classes hold functions that 
interact with the database. The code below shows the recipes table being created
in the book class. You`ll see in the code that the foreign key is being establish
to the category_id.  

```py 
def create_table(cls):
        """ Create a new table to persist the attributes of Recipes instances """
        sql = """
            CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            prep_time INT,
            category_id INT,
            FOREIGN KEY (category_id) REFERENCES category(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
```

---

## Conclusion

This READMD.md goes over important classes in my phase-3 project. It
shows the structure of the classes. Then it goes into the `lib/cli.py`.
Which prompt the user with options that allow them to interact with the
database. The `lib/cli.py` class get help from the `lib/helpers.py` class.
The helpers class is full of funtions that the cli class uses so the user
can create, edit, delete, and view data from the database. The last things
talked about in the README.md is the two classes used to create tables in
the database which are the `lib/models/book.py` and `lib/models/recipe.py`

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
