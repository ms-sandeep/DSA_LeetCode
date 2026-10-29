class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_counter = Counter(s1)
        window_counter = Counter(s2[:len_s1])

        if s1_counter == window_counter:
            return True

        for i in range(len_s1, len_s2):
            window_counter[s2[i]] +=1
            window_counter[s2[i - len_s1]] -=1

            if window_counter[s2[i - len_s1]] == 0:
                del window_counter[s2[i - len_s1]]
            if s1_counter == window_counter:
                return True
        return False


        