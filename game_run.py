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

