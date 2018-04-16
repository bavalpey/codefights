"""
Once upon a time, in a kingdom far, far away, there lived a king Byteasar VII. He reigned during the Dark Times, so very little is known
about those times. It is known that when he ascended the throne, there were n cities in the kingdom, connected by several two-way roads.
But before the young king managed to start ruling, the enemy came to the gates: the evil emperor Bugoleon invaded the kingdom and
started to conquer the cities day after day.

It is not known how long it took to capture each of the cities, but you've recently discovered an ancient chronicle saying that each
day Bugoleon captured all the cities that had at most 1 neighboring free city at the moment. Knowing this fact, the number of cities
n and all the roads of the kingdom, determine in how many days each of the cities was conquered.

Example

For n = 10 and
  roads = [[1, 0], [1, 2], [8, 5], [9, 7], 
           [5, 6], [5, 4], [4, 6], [6, 7]]
the output should be
  citiesConquering(n, roads) = [1, 2, 1, 1, -1, -1, -1, 2, 1, 1].
"""
def citiesConquering(n, roads):
    answer = [-1]*n
    connections = [[] for i in range(n)]
    for road in roads:
        connections[road[0]].append(road[1])
        connections[road[1]].append(road[0])
    
    counter = 0
    loop = True
    while loop:
        counter += 1
        loop = False
        remove = []
        for city,lst in enumerate(connections):
            if answer[city] == -1:
                if len(lst) <= 1:
                    answer[city] = counter
                    if len(lst) != 0:
                        remove.append([city,lst[0]])
                    loop = True
        for i in remove:
            connections[i[1]].remove(i[0])
    return answer
