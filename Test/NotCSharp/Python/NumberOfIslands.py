# https://leetcode.com/problems/number-of-islands/description/
# uses DFS, note the getnbors function - standardize on this function
class Solution(object):
    def __init__(self):
        self.count = 0
        self.visited = []

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.visited = [[False] * len(grid[0]) for x in range(len(grid))]

        m = len(grid)
        if m == 0:
            return self.count
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if self.visited[i][j]:
                    continue
                self.visited[i][j] = True
                if grid[i][j] == '1':
                    # print("reached here")
                    self.helper(grid, i, j)
                    self.count += 1

        print("count is", self.count)
        return self.count

    def helper(self, grid, i, j):
        nbors = self.getnbors(grid, i, j)
        # print("for i j", i, j)
        # print("nbors are", nbors)
        for i in nbors:
            if self.visited[i[0]][i[1]] is True:
                continue

            self.visited[i[0]][i[1]] = True
            if grid[i[0]][i[1]] == '1':
                self.helper(grid, i[0], i[1])

    def getnbors(self, grid, x, y):
        temp = []
        temp.append((x - 1, y))  # north
        temp.append((x + 1, y))  # south
        temp.append((x, y + 1))  # east
        temp.append((x, y - 1))  # west
        nbors = []
        for i in temp:
            if i[0] < 0 or i[1] < 0 or i[0] >= len(grid) or i[1] >= len(grid[0]):
                continue

            nbors.append(i)

        return nbors
