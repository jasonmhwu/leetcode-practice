class UndergroundSystem:
    # keeps a dictionary to store the checkin information
    # keeps another dictionary to store (startStation, endStation) pair
    # once a customer checks out, remove entry from id dict and add time to station pair list
    def __init__(self):
        # key: id, value: (stationName, t)
        self._checkin_info = dict()
        # key: (startStation, endStation), value: (num_customers, sum_travel_time)
        self._travel_time = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self._checkin_info[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_t = self._checkin_info.pop(id)
        if (start_station, stationName) in self._travel_time.keys():
            num_customers, sum_travel_time = self._travel_time[(start_station, stationName)]
        else:
            num_customers, sum_travel_time = 0, 0
        self._travel_time[(start_station, stationName)] =\
            (num_customers + 1, sum_travel_time + t - start_t)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        num_customers, sum_travel_time = self._travel_time[(startStation, endStation)]
        return sum_travel_time / num_customers


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
