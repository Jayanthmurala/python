#67


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        max_length = max(len(a), len(b))
        a = a.zfill(max_length)
        b = b.zfill(max_length)
        for i in range(max_length - 1, -1, -1):
            sum_bits = int(a[i]) + int(b[i]) + carry
            result.append(str(sum_bits % 2))
            carry = sum_bits // 2
        if carry:
            result.append('1')
        return ''.join(reversed(result))
