class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        passenger_set = set(passengers)
        j = 0  

        for bus in buses:
            count = 0
            while j < len(passengers) and passengers[j] <= bus and count < capacity:
                j += 1
                count += 1
            
        if count < capacity:
            time = buses[-1]
        else:
            time = passengers[j - 1] - 1

        while time in passenger_set:
            time -= 1
        
        return time