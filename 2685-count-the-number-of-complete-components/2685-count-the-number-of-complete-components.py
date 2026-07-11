class Solution:
    def countCompleteComponents(self, n, edges):

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(start):
            stack = [start]
            visited[start] = True

            nodes = 0
            degree_sum = 0

            while stack:
                node = stack.pop()
                nodes += 1
                degree_sum += len(graph[node])

                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

            return nodes, degree_sum // 2

        ans = 0

        for i in range(n):
            if not visited[i]:
                nodes, edges_cnt = dfs(i)

                if edges_cnt == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans