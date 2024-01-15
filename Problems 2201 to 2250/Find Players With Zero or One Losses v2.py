from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        losses = Counter()
        res = [[], []]

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)

            losses[loser] += 1

        for player in sorted(players):
            if losses[player] == 0: res[0].append(player)
            if losses[player] == 1: res[1].append(player)


        return res
