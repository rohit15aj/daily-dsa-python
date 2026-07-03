from collections import deque

class Solution:
    
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        weights = set()

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            weights.add(w)

       
        q = deque()
        topo = []

        deg = indegree[:]

        for i in range(n):
            if deg[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in graph[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)

        vals = sorted(weights)

        def check(limit):
            INF = 10 ** 30
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

            return dist[n - 1] <= k

        if not vals:
            return -1

        
        lo = 0
        hi = len(vals) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(vals[mid]):
                ans = vals[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans