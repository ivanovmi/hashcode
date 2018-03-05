import argparse


class Vehicle(object):
    def __init__(self, car_num):
        self.num = car_num
        self.coordinates = [0, 0]
        self.assigned_rides = []
        self.traveled_distance = 0

    def __repr__(self):
        return "Number: {}".format(self.num)

    def set_traveled_distance(self, new_distance):
        self.traveled_distance += new_distance

    def set_new_ride(self, new_ride):
        self.assigned_rides.append(new_ride)


class Ride(object):
    def __init__(self, ride_num, *args):
        self.num = ride_num
        self.start_point = args[:2]
        self.finish_point = args[2:4]
        self.earliest_start = args[4]
        self.latest_finish = args[5]

    def __repr__(self):
        return "Number: {}, " \
               "Start: {}, " \
               "Finish: {}, " \
               "Earliest Start: {}, " \
               "Latest Finish: {}".format(self.num, self.start_point,
                                          self.finish_point,
                                          self.earliest_start,
                                          self.latest_finish)


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
        return "Rows: {}, " \
               "Columns: {}, " \
               "Number of vehicles: {}," \
               "Number of rides: {}, " \
               "Bonus: {}, " \
               "Steps: {}".format(self.rows, self.columns, self.vehicles_num,
                                  self.rides_num, self.bonus, self.steps)


class Utils(object):
    @staticmethod
    def parse_input(inp_file):
        with open(inp_file, 'r') as input_file:
            input_file_content = input_file.readlines()
            info = Info(*input_file_content[0].rstrip().split())
            rides = [Ride(input_file_content.index(ride) - 1,
                          *ride.rstrip().split())
                     for ride in input_file_content[1:]]
            cars = Utils.init_cars(info.vehicles_num)
        return info, cars, rides

    @staticmethod
    def generate_output():
        pass

    @staticmethod
    def simulate():
        Utils.simulate()

    @staticmethod
    def init_cars(vehicle_num):
        return [Vehicle(vehicle_n)
                for vehicle_n in range(1, int(vehicle_num)+1)]

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument('--input', dest='input_file',
                            required=True, help='Input dataset')

        return parser


def main():
    utils = Utils()
    parser = utils.create_parser()
    args = parser.parse_args()
    info, cars, rides = utils.parse_input(args.input_file)
    print(info, cars, rides)


if __name__ == "__main__":
    main()
