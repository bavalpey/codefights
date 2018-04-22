"""
You've got tired of fixing your relatives' PCs after they visited some phishing website so you decided to implement a special plug-in
for their browsers which will check if the page they are trying to visit is similar to the one in the blacklist.

For that, you've thought of the special algorithm that for two URLs url1 and url2 computes their similarity as following:

  1. Initially their similarity is 0
  2. Then, it is increased by the following rules:
    +5, if the same protocol is used in both URLs.
    +10, if url1 and url2 have the same address.
    +k, if the first k components of path (delimited by /) are exactly the same (and in the same order) between the two URLs.
    +1 if for each varNames common between them. Additional +1 if the respective values are equal too.
    
URLs are given in the following format: protocol://address[(/path)*][?query] (where query = varName=value(&varName=value)*, parts given
in [] are optional, and parts in ()* may be repeated several times). Each of the named elements (i.e. protocol, address, path, varName
and value) are guaranteed to contain only alphanumeric characters and periods.

Given the two URLs url1 and url2, compute their similarity using the algorithm described above.

Example

For

  url1 = "https://codefights.com/home/test?param1=42&param3=testing&login=admin"
and

  url2 = "https://codefights.com/home/secret/test?param3=fish&param1=42&password=admin"
  
the output should be
  urlSimilarity(url1, url2) = 19.

Because these URLs have the same protocols, addresses, first path component (home) and two varNames, with one also having the same value
in both of them.
So the resulting similarity is thus 5 + 10 + 1 + 1 + 1 + 1 = 19.
"""
from urllib.parse import urlparse

def urlSimilarity(url1, url2):
    pts = 0
    parse1 = urlparse(url1)
    parse2 = urlparse(url2)
    if parse1.scheme == parse2.scheme:
        pts += 5
    if parse1.netloc == parse2.netloc:
        pts += 10
    path1 = parse1.path.split("/")[1:]
    path2 = parse2.path.split("/")[1:]
    for path in range(min([len(path1),len(path2)])):
        if path1[path] == path2[path]:
            pts += 1
        else:
            break
    query1 = parse1.query.split("&")
    query2 = parse2.query.split("&")
    q1dict = {}
    for i in query1:
        temp = i.split("=")
        if len(temp) == 2:
            q1dict[temp[0]] = temp[1]
    for i in query2:
        temp = i.split("=")
        if len(temp) == 2:
            if temp[0] in q1dict:
                pts +=1
                if q1dict[temp[0]] == temp[1]:
                    pts += 1
    return pts
