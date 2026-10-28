class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # create hash map
        m = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))  
            m[key].append(s)
        
        #return m(s.values())
        return list(m.values())
