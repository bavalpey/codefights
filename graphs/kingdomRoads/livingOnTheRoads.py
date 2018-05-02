"""
In a kingdom far, far away, there lives a king Byteasar IX. The history of the kingdom is rich with events and actions, most of which
has something to do with the cities of that kingdom. King Byteasar doesn't want to go down in history, and, most of all, he doesn't
want to have anything to do with the cities of the kingdom. Cities are lame!

Instead, king Byteasar wants to focus on the roads, which is why he issued a new decree: from now on, all roads are considered to be
cities, and all cities are considered to be roads. Now his gratefuller subjects pack their livings and move out from the cities to
the roads, and the cartographers are busy with building a new roadRegister of the kingdom. All roads of the kingdom are to be named
by the cities they connect (i.e. [city1, city2], city1 < city2), sorted lexicographically and enumerated starting from 0. A new road
register for such a system should be created.

Your task is to help the cartographers with building the new road register. Handle the challenge, and the glorious kingdom of Byteasar
IX will never have to deal with the tasks related to cities ever again!

Example
For
  roadRegister = [
    [false, true,  true,  false, false, false],
    [true,  false, false, true,  false, false],
    [true,  false, false, false, false, false],
    [false, true,  false, false, false, false],
    [false, false, false, false, false, true ],
    [false, false, false, false, true,  false]
  ]
the output should be
  livingOnTheRoads(roadRegister) = [
    [false, true,  true,  false],
    [true,  false, false, false],
    [true,  false, false, false],
    [false, false, false, false]
  ]
"""
from collections import OrderedDict
def livingOnTheRoads(roadRegister):
    road_dict = OrderedDict()
    for orig,roads in enumerate(roadRegister[:-1]):
        for city,road_to in enumerate(roads):
            if orig != city:
                if road_to:
                    key = ''.join(str(i) for i in sorted([orig,city]))
                    road_dict[key] = sorted([orig,city])
    ans = []
    for j in road_dict:
        for i in road_dict[j]:
            this = []
            for k in road_dict:
                if j == k:
                    this.append(False)
                elif set(road_dict[j])&set(road_dict[k]): # is there a common city from each road
                    this.append(True)
                else:
                    this.append(False)
        ans.append(this)
    return ans
