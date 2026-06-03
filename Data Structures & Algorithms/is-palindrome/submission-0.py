class Solution:
    def isPalindrome(self, s: str) -> bool:
        length: int = len(s)
        i: int = 0
        j: int = length - 1

        while i <= j:
            l: str = s[i].lower()
            r: str = s[j].lower()

            if not l.isalnum():
                i += 1
                continue
            if not r.isalnum():
                j -= 1
                continue
            
            if l != r:
                return False

            i += 1
            j -= 1

        return True
        