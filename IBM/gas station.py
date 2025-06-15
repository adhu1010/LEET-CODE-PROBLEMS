class Solution(object):
    
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        curr_tank = 0
        start_station = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_tank += gain
            curr_tank += gain

            if curr_tank < 0:
                # Can't start from current start_station to i
                start_station = i + 1
                curr_tank = 0

        return start_station if total_tank >= 0 else -1

#Time Complexity: O(n)
#Space Complexity: O(1)
# This code defines a class `Solution` with a method `canCompleteCircuit` that determines if there is a starting gas station from which a car can complete a circuit around a circular route.