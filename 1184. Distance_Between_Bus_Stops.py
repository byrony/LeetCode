class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        if start > destination:
            start, destination = destination, start
        clock = sum(distance[start:destination])
        c_clock = sum(distance[0:start]+distance[destination:len(distance)])
        return min(clock, c_clock)