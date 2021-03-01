class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # might need to perform instructions for maximum 4 times
        # need to go back to (0,0) at the end, regardless the orientation
        # takes O(n) time
        start = [0, 0]
        curr_direc = 0
        directions = (
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 0)
        )
        for num_loop in range(4):
            for c in instructions:
                if c == 'G':
                    start[0] += directions[curr_direc][0]
                    start[1] += directions[curr_direc][1]
                elif c == 'L':
                    curr_direc = (curr_direc + 1) % 4
                elif c == 'R':
                    curr_direc = (curr_direc + 3) % 4
                else:
                    pass
            if start == [0, 0]:
                return True
        return False

sol = Solution()
print(sol.isRobotBounded("GGLLGG"))
print(sol.isRobotBounded("GLGLGL"))
print(sol.isRobotBounded("GL"))
print(sol.isRobotBounded("GR"))
