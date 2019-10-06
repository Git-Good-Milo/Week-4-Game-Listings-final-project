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
            with open('game_listings.txt', 'w') as opened_file:
                opened_file.write(
                    "Game Name: " + self.game_name + ", " + "User Name: "+ self.user_name + ", " + "Phone Number: " + self.phone_num + ", " + "Price (£): " + self.price + ", " + "Postcode:  " + self.post_code + ",  " + self.lat + " " + self.long + '\n')

        except FileNotFoundError:
            print("File not found")

    def append_a_game_to_file(self):
        try:
            with open('game_listings.txt', 'a') as opened_file:
                opened_file.write(
                    "Game Name: " + self.game_name + ", " + "User Name: " + self.user_name + ", " + "Phone Number: " + self.phone_num + ", " + "Price (£): " + self.price + ", " + "Postcode:  " + self.post_code + ",  " + self.lat + " " + self.long + '\n')

        except FileNotFoundError:
            print("File not found")

    def open_read_file_using_with(file):
        try:
            with open("game_listings.txt", 'r') as open_file:
                for line in open_file.readlines():
                    print(line.rstrip('\n'))
        except FileNotFoundError as errmsg:
            print("File can not be found. Please check your input")
            print(errmsg)
            # raise
        finally:
            print('\n Execution complete')

    def get_post_code(input_post_code):
        try:
            request_post_code = requests.get('https://api.postcodes.io/postcodes/' + input_post_code)
            return_postcode = request_post_code.json()["result"]  # ["postcode"]

            return return_postcode
        except ConnectionError:
            print("Not a valid URL")

