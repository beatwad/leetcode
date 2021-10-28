class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, l = len(s1), len(s2), len(s3)
        if l != m + n:
            return False
        stack, visited = [[0, 0]], {(0, 0)}
        while stack:
            i, j = stack.pop()
            if i + j == l:
                return True
            if i < n and s1[i] == s3[i+j] and (i+1, j) not in visited:
                visited.add((i+1, j))
                stack.append([i+1, j])
            if j < m and s2[j] == s3[i+j] and (i, j+1) not in visited:
                visited.add((i, j+1))
                stack.append([i, j+1])
        return False


if __name__ == '__main__':
    sol = Solution()
    assert sol.isInterleave("", "", "") is True
    assert sol.isInterleave("a", "b", "a") is False
    assert sol.isInterleave("aa", "bb", "aabb") is True
    assert sol.isInterleave("aa", "ab", "aaab") is True
    assert sol.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
    assert sol.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False
    assert sol.isInterleave("aabcc", "dbbca", "aabccdbbca") is True
    assert sol.isInterleave("aabccaa", "dbbcadd", "aabccdbbcaaadd") is True
    assert sol.isInterleave("aabccba", "dbbcadd", "aabccdbbcaaadd") is False
    assert sol.isInterleave("aabaac", "aadaaeaaf", "aadaaeaabaafaac") is True