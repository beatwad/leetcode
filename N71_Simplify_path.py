import re


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub('/+', '/', path)
        res = list()

        for p in path.split('/'):
            if p == '' or p == '.':
                continue
            elif p == '..':
                if res:
                    res.pop()
            else:
                res.append(p)

        return '/' + '/'.join(res)


if __name__ == '__main__':
    sol = Solution()
    assert sol.simplifyPath('/') == '/'
    assert sol.simplifyPath('/.') == '/'
    assert sol.simplifyPath('/..') == '/'
    assert sol.simplifyPath('//') == '/'
    assert sol.simplifyPath('//.') == '/'
    assert sol.simplifyPath('///.') == '/'
    assert sol.simplifyPath('/././.') == '/'
    assert sol.simplifyPath('/./../.') == '/'
    assert sol.simplifyPath('//./../.') == '/'
    assert sol.simplifyPath('//./../home/.') == '/home'
    assert sol.simplifyPath('/home/..') == '/'
    assert sol.simplifyPath('/../') == '/'
    assert sol.simplifyPath('/...') == '/...'
    assert sol.simplifyPath('/home/') == '/home'
    assert sol.simplifyPath('/_') == '/_'
    assert sol.simplifyPath('//') == '/'
    assert sol.simplifyPath('..') == '/'
    assert sol.simplifyPath('/home//foo') == '/home/foo'
    assert sol.simplifyPath('/home//foo/') == '/home/foo'
    assert sol.simplifyPath('/home//foo..') == '/home/foo..'
    assert sol.simplifyPath('/home/../foo..') == '/foo..'
