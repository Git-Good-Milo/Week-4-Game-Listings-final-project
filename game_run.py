from game_listing_db import *
from game_class import *

# Connect to the game DB
conn_to_gl_db = ConnectMsS('Passw0rd2018')
game1 = Games("Apex Legends", "Miles Eastwood", "07413065597", "10", "N16 9LN")
game2 = Games("Halo Reach", "Spartan 117", "01597896302", "30", "W4 5AB")
game3 = Games("Fifa 2020", "Vladimir Putin", "077-SOVIET-999", "50", "PA49 7UT")

# Add a game to the listing database
# conn_to_gl_db.add_game_to_db(game1.game_name, game1.user_name, game1.phone_num, game1.price, game1.post_code, game1.lat, game1.long)
# conn_to_gl_db.add_game_to_db(game2.game_name, game2.user_name, game2.phone_num, game2.price, game2.post_code, game2.lat, game2.long)
# conn_to_gl_db.add_game_to_db(game3.game_name, game3.user_name, game3.phone_num, game3.price, game3.post_code, game3.lat, game3.long)

# Delete a game from the listing
# conn_to_gl_db.delete_game_from_db(1)

# View All games in the Database
# print(conn_to_gl_db.read_all_games())

# View one specific game in the Database
# print(conn_to_gl_db.title_search(3))

# Update the latitude and longitude of a location
# conn_to_gl_db.get_lat_long("PA49 7UT")

# print(conn_to_gl_db.title_search(3))

# Atempting User interface

#game1.write_a_game_to_file()
#game2.append_a_game_to_file()
#game3.append_a_game_to_file()

welcome_statement = print("Good morning and welcome to the best game listing website in the Universe! Here are your options:")

while True:
    option_1 = print("Option 1: Would you like to add a game to our ilustrious database?")
    option_2 = print("Option 2: Would you like to view all games or just one?")
    option_3 = print("Option 3: Would you like to delete a shoddy game from our database?")
    option_4 = print("Option 4: Would you like to export a recipe to a .txt file?")
    user_input = input("Enter your choice:  ")

    if user_input == "1":
        get_game_name = input("'Please enter your game name: '")
        get_user_name = input("'Please enter your User name: '")
        get_phone_num = input("'Please enter you phone number: '")
        get_price = input("Please input the price of your game: ")
        get_postCode = input("'Please enter your postcode: '")
        user_game_list = conn_to_gl_db.add_game_to_db(get_game_name,get_user_name,get_phone_num, get_price, get_postCode)
        print(f"{get_game_name} has been added to the database :)")
        break

    elif user_input == "2":
        view_game_s = input("Would you like to view one game or all of them?")
        if view_game_s == "1":
            specific_id = input("Please enter the game ID you would like to view?")
            view_by_title = conn_to_gl_db.title_search(specific_id)
            print(view_by_title)
        elif view_game_s == "all":
            view_all = conn_to_gl_db.read_all_games()
            print(view_all)
        else:
            print("Sorry, I didnt quite get that")
            break

    elif user_input == "3":
        game_to_delete = input("Enter the game ID you would you like to delete: ")
        delete_recipe = conn_to_gl_db.delete_game_from_db(game_to_delete)
        print("That game has been deleted")

    # elif user_input == "4":
    #     input_recipe_for_txt = input("Which game would you like to export?")
    #
    #     if input_game_for_txt == user_recipe.recipe_name:
    #         recipe_to_export = user_recipe.append_a_recipe_to_file()
    #
    #     elif input_recipe_for_txt == "I'd like to choose a recipe":
    #         recipe_to_choose = input("Which recipe will it be then?")
    #
    #         if recipe_to_choose ==

    elif user_input == "exit":
        break

