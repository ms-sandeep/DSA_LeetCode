class Solution(object):
    def groupAnagrams(self, strs):
        group = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in group:
                group[sorted_word] = []
            
            group[sorted_word].append(word)

        return list(group.values())
        