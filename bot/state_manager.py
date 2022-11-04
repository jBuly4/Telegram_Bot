from collections import defaultdict


class StateManager:
    #  Statuses
    START, REST_NAME, LOCATION, SAVE = range(4)


    def __init__(self):
        self.USER_STATE = defaultdict(lambda: self.START)  # all new users will be created with START status

    @classmethod
    def get_state: