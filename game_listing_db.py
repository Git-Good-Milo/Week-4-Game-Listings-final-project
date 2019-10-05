# Create and connect a game listing database on msS for game listing
import pyodbc
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

    def title_search(self, input_id_num):
        title = self.sql_query_fetchone(f"SELECT * FROM GameListings WHERE [Game ID] = '{input_id_num}'")
        return title

    # Add a game to the existing database
    def add_recipe_to_db(self, game_name, user_name, phone_num, price, location, lat_geo, long_geo):
            self.filter_query(f"INSERT INTO GameListings VALUES ('{game_name}', '{user_name}', '{phone_num}', '{price}', '{location}', '{lat_geo}', '{long_geo}')")
            self.conn_rep_db.commit()

    # Delete a game from the database
    def delete_recipe_from_db(self, game_id_to_remove):
        self.filter_query(f"DELETE FROM GameListings WHERE [Game ID] = '{game_id_to_remove}'")
        self.conn_rep_db.commit()

        # View all of the game details
        def read_all_recipes(self):
            query_rows = self.filter_query("SELECT * FROM GameListings")
            while True:
                record = query_rows.fetchone()
                if record is None:
                    break
                return record