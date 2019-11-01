def h(start, goal):
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    
    # Work out the manhattah distance of each tile from its eventual goal
    sboard = [int(num) if num != " " else 0 for num in start]
    gboard = [int(num) if num != " " else 0 for num in goal]

    manhattan_distance = 0
    for s,g in ((sboard.index(i), gboard.index(i)) for i in range (1,9)):
    	manhattan_distance += abs(s % 3 - g % 3) + abs(s // 3 - g // 3)
    	
    return manhattan_distance
