class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        account_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])   # compress: point directly at root
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        for account in accounts:
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                account_name[email] = account[0]

        for account in accounts:
            emails = account[1:]
            for email in emails:
                union(email, emails[0])

        graph = defaultdict(list)
        for node in parent:
            graph[find(node)].append(node)

        merged_accounts = []
        for node in graph:
            name = account_name[node]
            emails = sorted(graph[node])
            account = [name, *emails]
            merged_accounts.append(account)
        
        return merged_accounts