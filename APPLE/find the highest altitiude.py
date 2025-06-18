class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0
        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)
        return max_altitude

# Time Complexity: O(n) where n is the length of the input list gain, as we iterate through the list once.
# Space Complexity: O(1) since we only use a few variables to keep track of the current altitude and the maximum altitude.