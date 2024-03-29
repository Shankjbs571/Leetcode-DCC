#📚 Problem Sources:
# Leetcode: https://leetcode.com/problems/meeting-rooms-iii/description/

# 2402. Meeting Rooms III


# S O L U T I O N
import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms, used_rooms = list(range(n)), []
        heapq.heapify(unused_rooms)
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(unused_rooms, room)
            if unused_rooms:
                room = heapq.heappop(unused_rooms)
                heapq.heappush(used_rooms, [end, room])
            else:
                room_availability_time, room = heapq.heappop(used_rooms)
                heapq.heappush(
                    used_rooms,
                    [room_availability_time + end - start, room]
                )
            meeting_count[room] += 1
        return meeting_count.index(max(meeting_count))
