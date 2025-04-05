from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dp(i):
            if i < 0:
                print("i is ->", i)
                return True
            for word in wordDict:
                print("word is ->", word, "and i is ->", i)
                if (i >= len(word) - 1) and dp(i - len(word)):
                    if s[i - len(word) + 1: i + 1] == word:
                        return True

            return False

        return dp(len(s) - 1)
# print(Solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(Solution.wordBreak("cars", ["car","ca","rs"]))