class Solution:
    def exist(self, board: list, word: str) -> bool:
        def dfs(board, word, x, y):
            if not word:
                return True

            letter = word[0]
            for i, j in [[max(x-1, 0), y], [min(x+1, m-1), y], [x, max(y-1, 0)], [x, min(y+1, n-1)]]:
                if board[i][j] == letter:
                    board[i][j] = ''
                    res = dfs(board, word[1:], i, j)
                    if res:
                        return True
                    board[i][j] = letter

            return False

        m, n = len(board), len(board[0])
        letter = word[0]

        for i in range(m):
            for j in range(n):
                if board[i][j] == letter:
                    board[i][j] = ''
                    res = dfs(board, word[1:], i, j)
                    if res:
                        return True
                    board[i][j] = letter

        return False


if __name__ == '__main__':
    sol = Solution()
    assert sol.exist([["A"]], word="B") is False
    assert sol.exist([["A", "A"]], word="AA") is True
    assert sol.exist([["A", "B"]], word="ABA") is False
    assert sol.exist([["A", "B"], ["C", "D"]], word="ABCD") is False
    assert sol.exist([["A", "B"], ["D", "C"]], word="ABCD") is True
    assert sol.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], word="AAB") is True
    assert sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED") is True
    assert sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE") is True
    assert sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB") is False
