# Create and connect a game listing database on msS for game listing
import pyodbc
from game_class import *
# Define a class as a recipe database
class ConnectMsS():

    # have the characteristcs to access the db
    def __init__(self, password, server = 'localhost,1433', database = 'GameListings', username = 'SA'):
        self.server = server
        self.database = database
        self.username =username
        self.password = password
        self.conn_rep_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_rep_db.cursor()

    # defining methods
    def filter_query(self, query):
        return self.cursor.execute(query)

    def sql_query(self, query):
        return self.filter_query(query)


    # def return_all_product_details(self):
    #     query_rows = self.filter_query()

    def sql_query_fetchone(self, query):
        return self.filter_query(query).fetchone()

    # Add a game to the existing database
    def add_game_to_db(self, game_name, user_name, phone_num, price, location, lat_geo, long_geo):
            self.filter_query(f"INSERT INTO Games_to_list VALUES ('{game_name}', '{user_name}', '{phone_num}', '{price}', '{location}', '{lat_geo}', '{long_geo}')")
            self.conn_rep_db.commit()

    # Delete a game from the database
    def delete_game_from_db(self, game_id_to_remove):
        self.filter_query(f"DELETE FROM Games_to_list WHERE [Game ID] = '{game_id_to_remove}'")
        self.conn_rep_db.commit()


    def title_search(self, input_id_num):
        title = self.sql_query_fetchone(f"SELECT * FROM Games_to_list WHERE [Game ID] = '{input_id_num}'")
        return title

        # View all of the game details
    def read_all_games(self):
        query_rows = self.filter_query("SELECT * FROM Games_to_list")
        while True:
            record = query_rows.fetchall()
            if record is None:
                break
            return record

        # Use methods to get latitude
    def get_lat_long(self, input_post_code):
        try:
            request_post_code = requests.get('https://api.postcodes.io/postcodes/' + input_post_code)
            return_latitude = request_post_code.json()["result"]["latitude"]
            return_longitude = request_post_code.json()["result"]["longitude"]
            self.filter_query(f"UPDATE Games_to_list SET longitude = '{return_longitude}', latitude = '{return_latitude}' WHERE location = '{input_post_code}'")
            self.conn_rep_db.commit()
        except ConnectionError:
            print("Not a valid URL")


    # def update_game_info(self, input_column_name, input_new_data, input_where):
    #     self.filter_query(f"UPDATE Games_to_list SET {input_column_name} = '{input_new_data}' WHERE location = '{input_where}'")