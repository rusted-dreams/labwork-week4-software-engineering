class Flight:
    def __init__(self, flight_id, origin, destination, price):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self, flights):
        self.flights = flights

    def search_city(self, city):
        result = []
        for flight in self.flights:
            if flight.origin == city or flight.destination == city:
                result.append(flight)
        return result

    def search_from_city(self, city):
        result = []
        for flight in self.flights:
            if flight.origin == city:
                result.append(flight)
        return result

    def search_between_cities(self, origin, destination):
        result = []
        for flight in self.flights:
            if flight.origin == origin and flight.destination == destination:
                result.append(flight)
        return result

flights = [
    Flight("AI161E90", "BLR", "BOM", 5600),
    Flight("BR161F91", "BOM", "BBI", 6750),
    Flight("AI161F99", "BBI", "BLR", 8210),
    Flight("VS171E20", "JLR", "BBI", 5500),
    Flight("AS171G30", "HYD", "JLR", 4400),
    Flight("AI131F49", "HYD", "BOM", 3499)
]

flight_table = FlightTable(flights)

print("please choose the kind of search you want to perform")
print("1. search for Flights for a particular City")
print("2. search for Flights From a city")
print("3. search for Flights between two given cities")
print("4. exit")
user_ch = int(input("Enter your choice: "))
while user_ch != 4:
    if user_ch == 1:
        city = input("Enter the city: ")
        result = flight_table.search_city(city)
    elif user_ch == 2:
        city = input("Enter the city: ")
        result = flight_table.search_from_city(city)
    elif user_ch == 3:
        origin = input("Enter the origin city: ")
        destination = input("Enter the destination city: ")
        result = flight_table.search_between_cities(origin, destination)
    elif user_ch == 4:
        break
    else:
        print("Invalid user_ch")
        result = []

if user_ch != 4:
    for flight in result:
        print(flight.flight_id, flight.origin, flight.destination, flight.price)