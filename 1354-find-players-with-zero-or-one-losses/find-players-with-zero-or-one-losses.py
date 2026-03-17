class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        loss_count = {}

        for winner, loser in matches:
            if winner not in loss_count:
                loss_count[winner] = 0

            loss_count[loser] = loss_count.get(loser, 0) + 1

        zero_loss = []
        one_loss = []

        for player in loss_count:
            if loss_count[player] == 0:
                zero_loss.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)

        return [sorted(zero_loss), sorted(one_loss)]