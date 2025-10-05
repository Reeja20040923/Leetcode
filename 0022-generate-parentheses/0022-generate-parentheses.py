class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backTrack(current,open_count,close_count):
            if open_count == n and close_count == n:
                result.append(current)
                return

            if open_count < n:
                backTrack(current+'(',open_count+1,close_count)

            if close_count < open_count:
                backTrack(current+')',open_count,close_count+1)

        backTrack("",0,0)
        return result
        