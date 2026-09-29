class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(s.lower().split())
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', st) 
        reverse_str = clean_text[::-1]
        if reverse_str==clean_text:
            return True
        return False
        