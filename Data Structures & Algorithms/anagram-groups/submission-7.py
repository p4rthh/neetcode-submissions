class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = dict()
        for i in strs:
            key = "".join(sorted(i))
            if key in final.keys():
                final[key].append(i)
            else:
                final[key] = [i]
        return list(final.values())
