from collections import defaultdict, namedtuple


Coordinates = namedtuple('Coordinates', ['latitude', 'longitude'])


class StateManager:
    def __init__(self):
        #  Statuses
        self.START, self.REST_NAME, self.LOCATION, self.SAVE = range(4)
        self.USER_STATE = defaultdict(lambda: self.START)  # all new users will be created with START status

    def get_state(self, message):
        return self.USER_STATE[message.chat.id]

    def update_state(self, message, state):
        self.USER_STATE[message.chat.id] = state


class LocationManager:
    def __init__(self):
        self.LOCATIONS = defaultdict(lambda: {})  # all new locations will be created with empty dict

    def get_location(self, user_id):
        return self.LOCATIONS[user_id]

    def update_location(self, user_id, rest_name, latitude, longitude):
        coordinates = Coordinates(latitude, longitude)
        self.LOCATIONS[user_id][rest_name] = coordinates
