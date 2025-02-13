import heapq

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

        # print(self.arr, "heap")

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr) % 2 != 0:
            mid = len(self.arr) // 2
            return self.arr[mid]
        elif len(self.arr) % 2 == 0:
            mid = len(self.arr) // 2
            mid_prev = mid - 1
            return (self.arr[mid] + self.arr[mid_prev]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()