players = {}

while True:
    command = input()
    if command == "Season end":
        break

    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players:
            players[player] = {}
        if position not in players[player] or skill > players[player][position]:
            players[player][position] = skill

    elif "vs" in command:
        player1, player2 = command.split(" vs ")
        if player1 in players and player2 in players:
            common_positions = set(players[player1].keys()) & set(players[player2].keys())
            if common_positions:
                total_skill1 = sum(players[player1][pos] for pos in common_positions)
                total_skill2 = sum(players[player2][pos] for pos in common_positions)
                if total_skill1 > total_skill2:
                    del players[player2]
                elif total_skill2 > total_skill1:
                    del players[player1]

sorted_players = sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0]))
for player, positions in sorted_players:
    total_skills = sum(positions.values())
    print(f"{player}: {total_skills} skill")
    for position, skill in sorted(positions.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
