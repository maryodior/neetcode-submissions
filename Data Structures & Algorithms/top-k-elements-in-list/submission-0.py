class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newArray = []
        counted = {}
        for i, value in enumerate(nums):
            if value in counted:
                modifiedIndex = counted[value]
                newArray[modifiedIndex].append(value)
            else:
                newArray.append([value])
                counted[value] = len(newArray) - 1
        newArray.sort(key=len, reverse=True)
        result = [child[0] for child in newArray[:k]]
        return result

        