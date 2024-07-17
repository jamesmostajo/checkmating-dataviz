filenames = []
fileouts = []
base = "ChessData/lichess_elite_2023-"
for i in range(1, 12+1):
    if i < 10: 
        filenames.append(base+"0"+str(i)+".pgn")
        fileouts.append("Games/0"+str(i)+"GamesChessMoves.csv")
    else:
        filenames.append(base+str(i)+".pgn")
        fileouts.append("Games/"+str(i)+"GamesChessMoves.csv")


for i in range(12):
# filepath = "ChessData/lichess_elite_2023-01.pgn"
# fileout = "JanuaryGamesChessMoves.csv"
    filepath = filenames[i]
    fileout = fileouts[i]
    f = open(filepath, "r")
    s = open(fileout,"w")
    data = f.read()

    data = str(data)
    raw_data = data.split("[Event ")

    del raw_data[0]

    games = []
    for game_index in range(len(raw_data)):
        game = raw_data[game_index]
        index = game.find("1. ")
        games.append(game[index:].split())

    for game_index in range(len(games)):
        moves = []
        game = games[game_index]
        for token in game:
            if token[-1] != ".":
                moves.append(token)
        games[game_index] = moves

    # print(len(games))
    for game in games:
        for move in game:
            s.write(move)
            s.write(",")
        s.write("\n")

    f.close()
    s.close()