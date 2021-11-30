from collections import defaultdict
from typing import *


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name_dict = dict()
        email_dict = defaultdict(set)
        for i in range(len(accounts)):
            name = accounts[i][0]
            first_email = accounts[i][1]
            for email in accounts[i][1:]:
                email_dict[first_email].add(email)
                email_dict[email].add(first_email)
                name_dict[email] = name

        visited, ans = set(), list()

        for email in email_dict:
            if email in visited:
                continue
            res = list()
            name = name_dict[email]
            queue = [email]
            while queue:
                node = queue.pop()
                for c in email_dict[node]:
                    if c not in visited:
                        res.append(c)
                        visited.add(c)
                        queue.append(c)
            ans.append([name] + sorted(res))

        return ans


if __name__ == '__main__':
    sol = Solution()
    assert sol.accountsMerge([["John", "johnsmith@mail.com", "john_newyork@mail.com"]]) == [["John",
                                                                                             "john_newyork@mail.com",
                                                                                             "johnsmith@mail.com"]]
    assert sol.accountsMerge([["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                              ["John", "johnsmith@mail.com", "john00@mail.com"],
                              ["Mary", "mary@mail.com"],
                              ["John", "johnnybravo@mail.com"]]) == [["John", "john00@mail.com",
                                                                      "john_newyork@mail.com", "johnsmith@mail.com"],
                                                                     ["Mary", "mary@mail.com"],
                                                                     ["John", "johnnybravo@mail.com"]]
    assert sol.accountsMerge([["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                              ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                              ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                              ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                              ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]) == [["Gabe", "Gabe0@m.co",
                                                                                        "Gabe1@m.co", "Gabe3@m.co"],
                                                                                       ["Kevin", "Kevin0@m.co",
                                                                                        "Kevin3@m.co", "Kevin5@m.co"],
                                                                                       ["Ethan", "Ethan0@m.co",
                                                                                        "Ethan4@m.co", "Ethan5@m.co"],
                                                                                       ["Hanzo", "Hanzo0@m.co",
                                                                                        "Hanzo1@m.co", "Hanzo3@m.co"],
                                                                                       ["Fern", "Fern0@m.co",
                                                                                        "Fern1@m.co", "Fern5@m.co"]]
