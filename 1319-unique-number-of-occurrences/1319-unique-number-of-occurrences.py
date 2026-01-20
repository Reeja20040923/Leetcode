class Solution:
    def uniqueOccurrences(self,arr: List[int]) -> bool:
        checker = []
        counter = 1
        arr.sort()
        if len(arr) == 1:
            return False
        
        for i in range(len(arr)):
            if i == 0:
                continue
            if arr[i] == arr[i-1]:
                counter += 1
                if i == len(arr)- 1:
                    checker.append(counter)
            if arr[i] != arr[i-1]:
                checker.append(counter)
                counter = 1
                if i == len(arr) - 1:
                    checker.append(counter)
        checker.sort()
        return checker == sorted(list(set(checker)))
        
