class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        onedelete = float('-inf')
        nodelete = arr[0]
        res = arr[0]

        for i in range(1,len(arr)):

            onedelete = max(onedelete+arr[i], nodelete)
            nodelete = max(arr[i],nodelete+arr[i])

                

            res = max(res, max(nodelete, onedelete))
        return res