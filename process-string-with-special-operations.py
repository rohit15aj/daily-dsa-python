class Solution:
    def processStr(self, s):

        result = []

        for ch in s:

            # Append character
            if 'a' <= ch <= 'z':
                result.append(ch)

            # Remove last character
            elif ch == '*':
                if result:
                    result.pop()

            # Duplicate current string
            elif ch == '#':
                result.extend(result)

            # Reverse current string
            elif ch == '%':
                result.reverse()

        return ''.join(result)
