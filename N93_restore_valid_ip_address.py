from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = list()

        def get_valid_ip_part(s, comb):
            if s == '' and len(comb) == 4:
                res.append(comb)
            else:
                for i in range(len(s)):
                    if i > 2 or int(s[:i+1]) > 255:
                        break
                    elif s[0] == '0':
                        get_valid_ip_part(s[i+1:], comb + [s[:i+1]])
                        break
                    else:
                        get_valid_ip_part(s[i+1:], comb + [s[:i+1]])

        get_valid_ip_part(s, [])
        return ['.'.join(i) for i in res]


if __name__ == '__main__':
    sol = Solution()
    assert sol.restoreIpAddresses('0000') == ['0.0.0.0']
    assert sol.restoreIpAddresses('25525511135') == ["255.255.11.135", "255.255.111.35"]
    assert sol.restoreIpAddresses('101023') == ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert sol.restoreIpAddresses('25525511135255255') == []
