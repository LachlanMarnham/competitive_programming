from typing import List


class Solution:
    def best_team_score(self, scores: List[int], ages: List[int]) -> int:
        players = []
        for i in range(len(scores)):
            player = (ages[i], scores[i])
            players.append(player)

        # Will sort in increasing order of age. In the event of
        # two players having the same age, it will sort in increasing
        # order of score
        players.sort()
        scores = [p[1] for p in players]
        dp = scores.copy()
        max_score = 0
        for i in range(len(dp)):
            for j in range(i):
                if scores[j] <= scores[i]:
                    dp[i] = max(dp[i], dp[j] + scores[i])
            if dp[i] > max_score:
                max_score = dp[i]
        return max_score
