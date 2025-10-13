class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        i = 0
        while i < n:
            lhs = words[i]
            for j in range(i+1, n):
                rhs = words[j]
                if is_anagram(lhs, rhs):
                    words[j] = None
                    i = j
                else:
                    break
            i += 1
        
        return [it for it in words if it is not None]

def is_anagram(lhs: str, rhs: str):
    bag = {c: 0 for c in 'abcedfghijklmnopqrstuvwxyz'}
    for c in lhs:
        bag[c] += 1
    for c in rhs:
        bag[c] -= 1
    return all(v == 0 for v in bag.values())

        