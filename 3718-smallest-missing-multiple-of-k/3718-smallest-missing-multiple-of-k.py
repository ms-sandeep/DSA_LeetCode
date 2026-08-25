class Solution(object):
    def missingMultiple(self, nums, k):
        i=1

        while True:
            multiple = i*k

            if multiple not in nums:
                return multiple

            i+=1
