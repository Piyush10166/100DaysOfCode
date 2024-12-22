class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        left_symbols = []

        for c in s:
            if c in mapping.values():
                left_symbols.append(c)
            elif c in mapping:
                if not left_symbols or left_symbols.pop() != mapping[c]:
                    return False
            else:
                return False

        return not left_symbols