from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(email: str) -> List[str]:
            stack = [email]
            emails = []

            while stack:
                email = stack.pop()

                if email in visited:
                    continue

                visited.add(email)
                emails.append(email)

                for neighbor in graph[email]:
                    stack.append(neighbor)

            return sorted(emails)

        graph = defaultdict(set)
        email_to_account = {}

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                email_to_account[email] = name
                graph[account[1]].add(email)
                graph[email].add(account[1])

        answer = []
        visited = set()
        for email, account in email_to_account.items():
            if email not in visited:
                answer.append([account] + dfs(email))

        return answer
