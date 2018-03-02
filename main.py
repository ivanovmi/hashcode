class Vehicle(object):
    def __init__(self):
        self.coordinates = [0, 0]


class Ride(object):
    def __init__(self):
        self.start_point = [0, 0]
        self.finish_point = [0, 0]
        self.earliest_start = 0
        self.latest_finish = 0


class Utils(object):
    @staticmethod
    def parse_input():
        pass

    @staticmethod
    def generate_output():
        pass


def main():
    utils = Utils()

if __name__ == "__main__":
    main()