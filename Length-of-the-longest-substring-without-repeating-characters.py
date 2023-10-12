def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        for start in range(len(s)):
            visited = set()
            for current in range(start, len(s)):
                ch = s[current]
                if ch in visited:
                    break
                visited.add(ch)
            maxLength = max(maxLength, len(visited))
        return maxLength
            