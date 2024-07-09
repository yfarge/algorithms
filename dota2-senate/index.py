class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s = [*senate]
        r_remove = d_remove = 0
        r_count = senate.count("R")
        d_count = len(senate) - r_count

        while r_count and d_count:
            for i, v in enumerate(s):
                if v == "R":
                    if r_remove > 0:
                        s[i] = None
                        r_count -= 1
                        r_remove -= 1
                    else:
                        d_remove += 1
                elif v == "D":
                    if d_remove > 0:
                        s[i] = None
                        d_count -= 1
                        d_remove -= 1
                    else:
                        r_remove += 1

        return "Radiant" if d_count == 0 else "Dire"
