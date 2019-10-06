# create a games class
import requests

class Games ():

    def __init__(self, game_name, user_name, phone_num, price, post_code, lat = " ", long = " "):
        self.game_name = game_name
        self.user_name =user_name
        self.phone_num = phone_num
        self.price = price
        self.post_code = post_code
        self.lat = lat
        self.long = long

    def write_a_game_to_file(self):
        try:
            with open('write_game_listings.txt', 'a') as opened_file:
                opened_file.write(
                    self.game_name + self.user_name + self.phone_num + self.price + self.location + self.lat + self.long + '\n')

        except FileNotFoundError:
            print("File not found")

    def append_a_game_to_file(self):
        try:
            with open('game_listings.txt', 'a') as opened_file:
                opened_file.write(self.game_name + self.user_name + self.phone_num + self.price + self.location + self.lat + self.long + '\n')

        except FileNotFoundError:
            print("File not found")

    def get_post_code(input_post_code):
        try:
            request_post_code = requests.get('https://api.postcodes.io/postcodes/' + input_post_code)
            return_postcode = request_post_code.json()["result"]  # ["postcode"]

            return return_postcode
        except ConnectionError:
            print("Not a valid URL")

