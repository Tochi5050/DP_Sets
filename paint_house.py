from typing import List

class Solution:
    def path_house(costs: List[List[int]]) -> int:
        houses = len(costs)
        color_cost = len(costs[0])

        dp_array = [[0] * color_cost for _ in range(houses + 1)]
        dp_array_larger = [[0] * color_cost for _ in range(houses)]






        for house in range(houses - 1, -1, -1):
            for cost in range(color_cost - 1, -1, -1):
                if cost == 2:
                    dp_array_larger[house][cost] = costs[house][cost] + dp_array[house + 1][1]
                if cost == 1:
                    dp_array_larger[house][cost] = costs[house][cost] + dp_array[house + 1][0]
                if cost == 0:
                    dp_array_larger[house][cost] = costs[house][cost] + dp_array[house + 1][2]
                    dp_array[house][2] = min(dp_array_larger[house][2], dp_array_larger[house][1])
                    dp_array[house][1] = min(dp_array_larger[house][1], dp_array_larger[house][0])
                    dp_array[house][0] = min(dp_array_larger[house][0], dp_array_larger[house][2])

        return min(dp_array_larger[0])


print(Solution.path_house([[17,2,17],[16,16,5],[14,3,19]]))
print(Solution.path_house([[7,6,2]]))
print(Solution.path_house([[3,5,3],[6,17,6],[7,13,18],[9,10,18]]))
print(Solution.path_house([[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]]))
print(Solution.path_house([[17, 2, 17], [8, 4, 10], [6, 3, 19], [4, 8, 12]]))