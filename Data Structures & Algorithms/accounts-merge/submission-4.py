class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        owner = {}   # email -> account name

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])   # path compression: point directly at root
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        # Register every email, then union all of an account's emails to the first
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email not in parent:
                    parent[email] = email
                owner[email] = name
            for email in emails:
                union(email, emails[0])

        # Group emails by the root of their tree
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        # Format: name first, then emails sorted
        merged = []
        for root, emails in groups.items():
            name = owner[root]
            merged.append([name, *sorted(emails)])

        return merged