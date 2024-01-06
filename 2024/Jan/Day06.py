#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/?envType=daily-question&envId=2024-01-06

#S O L U T I O N

import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
        n = len(jobs)
        endTimes = [e for s, e, p in jobs]
        
        dp = [0] * n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            s = jobs[i][0]
            e = jobs[i][1]
            p = jobs[i][2]

            # don't schedule current job
            dp[i] = dp[i - 1]

            # schedule current job
            index = bisect.bisect_right(endTimes, s) - 1
            dp[i] = max(dp[i], (dp[index] if index >= 0 else 0) + p)

        return dp[-1]