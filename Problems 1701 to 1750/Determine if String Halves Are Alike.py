class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        MID = len(s) // 2
        VOWELS = "aeiouAEIOU"
        s1 = s[:MID]
        s2 = s[MID:]

        return sum(map(s1.count, VOWELS)) == sum(map(s2.count, VOWELS))
