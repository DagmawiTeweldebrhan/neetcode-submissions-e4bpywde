class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finale = {}
        for word in strs:
            key = str(sorted(list(word)))
            if key not in finale:
                finale[key] = []
            finale[key].append(word)

        output = []
        for group in finale.values():
            output.append(group)
        return output



