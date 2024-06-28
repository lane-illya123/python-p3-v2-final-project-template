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
