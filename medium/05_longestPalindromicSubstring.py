class Solution:
    def longestPalindrome(self, s:str) -> str:
        def check_palin(s):
            return (s == s[::-1])

        # Grow from center
        biggest = s[0]
        step = len(biggest) // 2

        # Handle single letter centers
        for center in range(1, len(s) - 1):
            bounds = [center - (1 + step), center + (1 + step)]
            while (bounds[0] > -1) and (bounds[1] < len(s)):
                if check_palin(s[bounds[0]:bounds[1] + 1]):
                    biggest = s[bounds[0]:bounds[1] + 1]
                    step = len(biggest) // 2
                    bounds[0] -= 1
                    bounds[1] += 1
                else:
                    break

        # Handle double letter centers
        for center in range(step, len(s) - step - 1):
            bounds = [center - (step), center + (1 + step)]
            while (bounds[0] > -1) and (bounds[1] < len(s)):
                if check_palin(s[bounds[0]:bounds[1] + 1]):
                    biggest = s[bounds[0]:bounds[1] + 1]
                    step = len(biggest) // 2
                    bounds[0] -= 1
                    bounds[1] += 1
                else:
                    break
        
        return biggest



        # Check all substrings - slow solution
        for length in range(len(s), 0, -1):
            for start_index in range(0, len(s) + 1-length):
                if check_palin(s[start_index:(start_index + length)]):
                    return s[start_index:(start_index + length)]

print(Solution().longestPalindrome("babad"))