class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if (len(s) != len(goal)):
            return False

        newstr = s+s
        return goal in newstr