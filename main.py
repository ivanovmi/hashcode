import argparse


class Vehicle(object):
    def __init__(self):
        self.coordinates = [0, 0]
        self.assigned_rides = []
        self.traveled_distance = 0

    def set_traveled_distance(self, new_distance):
        self.traveled_distance += new_distance

    def set_new_ride(self, new_ride):
        self.assigned_rides.append(new_ride)


class Ride(object):
    def __init__(self, *args):
        self.start_point = args[:2]
        self.finish_point = args[2:4]
        self.earliest_start = args[4]
        self.latest_finish = args[5]

    def __repr__(self):
        return "Start: {}, Finish: {}".format(self.start_point, self.finish_point)


class Info(object):
    def __init__(self, rows, columns, vehicles_num,
                 rides_num, bonus, steps):
        self.rows = rows
        self.columns = columns
        self.vehicles_num = vehicles_num
        self.rides_num = rides_num
        self.bonus = bonus
        self.steps = steps

    def __repr__(self):
        return "Rows: {}, Columns: {}".format(self.rows, self.columns)


class Utils(object):
    @staticmethod
    def parse_input(inp_file):
        with open(inp_file, 'r') as input_file:
            input_file_content = input_file.readlines()
            info = Info(*input_file_content[0].rstrip().split())
            rides = [Ride(*ride.rstrip().split()) for ride in input_file_content[1:]]

        return info, rides

    @staticmethod
    def generate_output():
        pass

    @staticmethod
    def simulate():
        Utils.simulate()

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument('--input', dest='input_file', default='a.in',
                            required=True, help='Input dataset')

        return parser


def main():
    utils = Utils()
    parser = utils.create_parser()
    args = parser.parse_args()
    info, rides = utils.parse_input(args.input_file)
    print(info, rides)


if __name__ == "__main__":
    main()
