# create a games class

class Games ():

    def __init__(self, game_name, user_name, phone_num, price, location, lat, long):
        self.game_name = game_name
        self.user_name =user_name
        self.phone_num = phone_num
        self.price = price
        self.location = location
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
