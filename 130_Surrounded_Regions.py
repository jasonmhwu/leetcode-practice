from typing import List


def connectedComponent(start_x, start_y):
            """
            Returns all nodes connected to (start_x, start_y), and whether this region is surrounded.
            """
            direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            nodes_visited = set()
            is_surrounded = True
            stack = [(start_x, start_y)]
            while stack:
                curr_x, curr_y = stack.pop()
                nodes_visited.add((curr_x, curr_y))
                if curr_x in (0, m-1) or curr_y in (0, n-1):
                    is_surrounded = False
                for d_x, d_y in direc:
                    new_x, new_y = curr_x + d_x, curr_y + d_y
                    if 0 <= new_x < m\
                        and 0 <= new_y < n\
                        and board[new_x][new_y] == 'O'\
                        and (new_x, new_y) not in nodes_visited:
                        stack.append((new_x, new_y))
            return nodes_visited, is_surrounded
