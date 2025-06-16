from collections import defaultdict

class Solution(object):
    def rankTeams(self, votes):
        if not votes:
            return ""

        team_count = len(votes[0])
        ranking = defaultdict(lambda: [0] * team_count)

        # Count votes for each team
        for vote in votes:
            for i, team in enumerate(vote):
                ranking[team][i] -= 1  # Use negative to sort descending later

        # Sort teams by their ranking lists and then alphabetically
        sorted_teams = sorted(ranking.items(), key=lambda item: (item[1], item[0]))

        return ''.join([team for team, _ in sorted_teams])
