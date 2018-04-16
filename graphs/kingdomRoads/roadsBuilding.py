"""
Once upon a time, in a kingdom far, far away, there lived a king Byteasar II. There was nothing special neither about him, nor about his
kingdom. As a mediocre ruler, he did nothing about his kingdom and preferred hunting and feasting over doing anything about his kingdom
prosperity.

Luckily, his adviser, wise magician Bitlin, was working for the kingdom welfare daily and nightly. However, since there was no one to
advise him, he completely forgot about one important thing: the roads. Over the years most of the two-way roads built by Byteasar II
predecessors were forgotten and no longer traversable. Only a few roads can still be used.

Bitlin wanted each pair of cities to be connected, but couldn't find a way to figure out which roads are missing. Desperate, he turned
to his magic crystal, seeking help. The crystal showed him a programmer from the distant future: you! Now you're the only one who can save
the kingdom. Given the existing roads and the number of cities in the kingdom, you should use the most modern technologies and find out
what roads should be built again to make each pair of cities connected. Since the magic crystal is quite old and meticulous, it will only
transfer the information that is sorted properly.

The roads to be built should be returned in an array sorted lexicographically, with each road stored as [cityi, cityj], where
cityi < cityj.

Example

For cities = 4 and roads = [[0, 1], [1, 2], [2, 0]],
the output should be
  roadsBuilding(cities, roads) = [[0, 3], [1, 3], [2, 3]].
"""
import itertools
def roadsBuilding(cities, roads):
    road = list([a,b] for a in range(cities) for b in range(a,cities) if a != b)
    answer = []
    for x in road:
        if x not in roads and x[::-1] not in roads:
            answer.append(x)
    return answer
