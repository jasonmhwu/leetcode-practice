from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # use a set to keep track of all available keys
        # use an array to keep track of all rooms visited
        # dfs approach
        # O(n) time, O(n) space
        visited_rooms = [False] * len(rooms)
        keys = [0]
        
        while keys:
            room_id = keys.pop()
            if not visited_rooms[room_id]:
                visited_rooms[room_id] = True
                keys.extend(rooms[room_id])
        if all(visited_rooms):
            return True
        else:
            return False

sol = Solution()
print(sol.canVisitAllRooms([[1], [2], [3], []]))
