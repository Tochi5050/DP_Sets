from typing import List
from collections import deque

class Solution:
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        queue = deque([0])

        seen = set()
        # print(seen)

        while queue:
            start = queue.popleft()
            print(start)
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)

        return False

# print(Solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(Solution.wordBreak("cars", ["car","ca","rs"]))

