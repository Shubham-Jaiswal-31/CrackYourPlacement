class Solution:
    def reorganizeString(self, s: str) -> str:
        res, c = [], Counter(s)
        pq = [(-value,key) for key,value in c.items()]
        heapq.heapify(pq)
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b
        res = ''.join(res)
        if len(res) != len(s): return ''
        return res