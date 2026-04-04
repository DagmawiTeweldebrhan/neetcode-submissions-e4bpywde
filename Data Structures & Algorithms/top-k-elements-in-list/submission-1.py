class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        finale=[]
        for c in nums:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        while len(finale) < k:
            for c in dic:
                if dic[c]==max(dic.values()):
                    finale.append(c)
                    dic[c] = -20
                    break

        return finale
