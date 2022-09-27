class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l = len(dominoes)
        if l == 1:
            return dominoes

        res = [0 for _ in range(l)]

        dist = l
        for i in range(l):
            if dominoes[i] == 'R':
                dist = 0
            elif dominoes[i] == 'L':
                dist = l
            elif i > 0:
                dist = min(l, dist + 1)
            res[i] += dist

        dist = l
        for i in range(l-1, -1, -1):
            if dominoes[i] == 'L':
                dist = 0
            elif dominoes[i] == 'R':
                dist = l
            elif i < l-1:
                dist = min(l, dist + 1)
            res[i] -= dist

        return ''.join('R' if res[i] < 0 else 'L' if res[i] > 0 else '.' for i in range(l))


if __name__ == '__main__':
    sol = Solution()
    assert sol.pushDominoes(".") == "."
    assert sol.pushDominoes("L") == "L"
    assert sol.pushDominoes("R") == "R"
    assert sol.pushDominoes("..") == ".."
    assert sol.pushDominoes("RR") == "RR"
    assert sol.pushDominoes("LL") == "LL"
    assert sol.pushDominoes("RL") == "RL"
    assert sol.pushDominoes("RL") == "RL"
    assert sol.pushDominoes("RR.L") == "RR.L"
    assert sol.pushDominoes(".L.R.") == "LL.RR"
    assert sol.pushDominoes("R..L") == "RRLL"
    assert sol.pushDominoes("RR.LL") == "RR.LL"
    assert sol.pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."
