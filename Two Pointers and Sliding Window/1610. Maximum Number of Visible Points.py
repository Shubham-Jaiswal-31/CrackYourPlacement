class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        def getAngle(p):
            angle = math.atan2(p[0]-location[0], p[1]-location[1]) / (2 * math.pi) * 360
            if angle < 0:
                angle += 360
            return angle

        angles = []
        same = 0
        for p in points:
            if p == location:
                same += 1
            else:
                angles.append(getAngle(p))

        angles.sort()
        res = 0
        q = deque()

        for a in angles:
            q.append(a)
            while a - q[0] > angle:
                q.popleft()
            res = max(res, len(q))
        
        for a in angles:
            a += 360
            q.append(a)
            while a - q[0] > angle:
                q.popleft()
            res = max(res, len(q))
        
        return res + same