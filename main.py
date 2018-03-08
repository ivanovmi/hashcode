import argparse


class Vehicle(object):
    def __init__(self, car_num):
        self.num = car_num
        self.coordinates = [0, 0]
        self.assigned_rides = []
        self.traveled_distance = 0
        self.distance_to_nearest_ride = 0

    def __repr__(self):
        return str(self.num)

    def set_traveled_distance(self, new_distance):
        self.traveled_distance += new_distance

    def set_new_ride(self, new_ride):
        self.assigned_rides.append(new_ride)

    def set_coordinates(self, new_coordinates):
        self.coordinates = new_coordinates

    def set_distance_to_nearest_ride(self, new_distance):
        self.distance_to_nearest_ride = new_distance

    def show_info(self):
        return 'Assigned rides: {}'.format(self.assigned_rides)


class Ride(object):
    def __init__(self, ride_num, *args):
        self.num = ride_num
        self.start_point = args[:2]
        self.finish_point = args[2:4]
        self.earliest_start = args[4]
        self.latest_finish = args[5]
        self.priority = 0

    def __repr__(self):
        return str(self.num)

    def set_priority(self, new_priority):
        self.priority = new_priority

    def show_info(self):
        return ("Number: {}, "
                "Priority: {}"
                "Start: {}, "
                "Finish: {}, "
                "Earliest Start: {}, "
                "Latest Finish: {}".format(self.num, self.priority,
                                           self.start_point,
                                           self.finish_point,
                                           self.earliest_start,
                                           self.latest_finish))


class Info(object):
    def __init__(self, rows, columns, vehicles_num,
                 rides_num, bonus, steps, filename):
        self.rows = rows
        self.columns = columns
        self.vehicles_num = vehicles_num
        self.rides_num = rides_num
        self.bonus = bonus
        self.steps = steps
        self.file_name = filename

    def __repr__(self):
        return ("Rows: {}, "
                "Columns: {}, "
                "Number of vehicles: {},"
                "Number of rides: {}, "
                "Bonus: {}, "
                "Steps: {}".format(self.rows, self.columns, self.vehicles_num,
                                   self.rides_num, self.bonus, self.steps))


class Utils(object):
    @staticmethod
    def parse_input(inp_file):
        with open(inp_file, 'r') as input_file:
            filename = input_file.name.split('.')[0]
            input_file_content = input_file.readlines()
            info = Info(*input_file_content[0].rstrip().split(),
                        filename=filename)
            rides = [Ride(input_file_content.index(ride) - 1,
                          *ride.rstrip().split())
                     for ride in input_file_content[1:]]
            cars = Utils.init_cars(info.vehicles_num)

        return info, cars, rides

    @staticmethod
    def generate_output(info, result):
        with open(info.file_name+'.out', 'w') as output_file:
            for car in result:
                print(car.num, ' '.join([str(x.num)
                                         for x in car.assigned_rides]))
                output_file.write(str(car.num) + ' ' +
                                  ' '.join([str(x.num)
                                            for x in car.assigned_rides]) +
                                  '\n')
            pass

    @staticmethod
    def simulate(info, cars, rides):
        while len(rides) != 0:
            priorities = Utils.calculate_priority(cars, rides)
            print("Rides: ", rides)

            for car in cars:
                print("Car: ", car)
                ride = Utils.assign_by_bigger_property(car, rides, priorities)
                try:
                    rides.index(ride)
                except ValueError:
                    del priorities[car][ride]
                else:
                    car.set_new_ride(ride)
                    car.set_coordinates(ride.finish_point)
                    rides.remove(ride)
                    del priorities[car][ride]
                print("Priorities: ", priorities)
            Utils.simulate(info, cars, rides)

        return cars

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

    @staticmethod
    def assign_by_bigger_property(car, rides, priorities):
        s = [(k, priorities[car][k]) for k in sorted(priorities[car],
                                                     key=priorities[car].get,
                                                     reverse=True)]
        ride = s[0][0]

        return ride

    @staticmethod
    def calculate_priority(cars, rides):
        priorities = {}
        for car in cars:
            priorities[car] = {}
            for ride in rides:
                priorities[car][ride] = {}
                value = Utils.calculate_distance_from_vehicle_to_finish(car,
                                                                        ride)
                bonus = Utils.calculate_bonus(car, ride)
                priorities[car][ride] = value + bonus

        return priorities

    @staticmethod
    def calculate_distance(source_x, source_y, destination_x, destination_y):
        return (abs(int(destination_x) - int(source_x)) +
                abs(int(destination_y) - int(source_y)))

    @staticmethod
    def calculate_distance_from_vehicle_to_finish(vehicle, ride):
        return (Utils.calculate_distance(vehicle.coordinates[0],
                                         vehicle.coordinates[1],
                                         ride.start_point[0],
                                         ride.start_point[1]) +
                Utils.calculate_distance(ride.start_point[0],
                                         ride.start_point[1],
                                         ride.finish_point[0],
                                         ride.finish_point[1]))

    @staticmethod
    def calculate_full_distance(vehicle, ride):
        distance = (Utils.calculate_distance(vehicle.coordinates[0],
                                             vehicle.coordinates[1],
                                             ride.start_point[0],
                                             ride.start_point[1]) +
                    int(ride.earliest_start) +
                    Utils.calculate_distance(ride.start_point[0],
                                             ride.start_point[1],
                                             ride.finish_point[0],
                                             ride.finish_point[1]))

        return distance

    @staticmethod
    def calculate_bonus(car, ride):
        return (int(ride.earliest_start) -
                Utils.calculate_distance(car.coordinates[0],
                                         car.coordinates[1],
                                         ride.start_point[0],
                                         ride.start_point[1]))


def main():
    utils = Utils()
    parser = utils.create_parser()
    args = parser.parse_args()
    info, cars, rides = utils.parse_input(args.input_file)
    # import pdb; pdb.set_trace()
    result = utils.simulate(info, cars, rides)
    utils.generate_output(info, result)


if __name__ == "__main__":
    main()
