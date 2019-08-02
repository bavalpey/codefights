/*
You have a strongly connected directed graph that has positive weights in the adjacency matrix g. The graph is represented as a
square matrix, where g[i][j] is the weight of the edge (i, j), or -1 if there is no such edge.

Given g and the index of a start vertex s, find the minimal distances between the start vertex s and each of the vertices of the
graph.

Example

For
  g = [[-1, 3, 2],
       [2, -1, 0],
       [-1, 0, -1]]
  and s = 0, the output should be
    graphDistances(g, s) = [0, 2, 2].
    
  The distance from the start vertex 0 to itself is 0.
  The distance from the start vertex 0 to vertex 1 is 2 + 0 = 2.
  The distance from the start vertex 0 to vertex 2 is 2.
*/


use std::collections::HashSet;
use std::cmp;

fn graphDistances(g: Vec<Vec<i32>>, s: i32) -> Vec<i32> {
  // This is Dijkstra's algorithm. Let's implement it!
  // A bit simple, since the graph is strongly connected
  
  
  let size = g.len();
  
  
  // Explored is a set for keeping track of nodes that have been visited.
  let mut explored: HashSet<i32> = HashSet::new();
  
  let mut ans: Vec<i32> = g[s as usize].clone();
  explored.insert(s);
  ans[s as usize] = 0;
  
  // The following steps are to be repeated size-1 times.
  // To start, ans is a vec of the distance to each node from the start
  // We pick the next node by iterating through ans and choosing the lowest weight of the unexplored nodes
  // (explored nodes are kept track of in the set 'explored')
  // Then, we update the weights of unexplored nodes in ans by comparing their current weight to the
  //   weight of travelling to the newly picked node first and then to that node.
  for _i in 1..size {
    // Iterate through ans as described above
    let (next_node, cost) = 
      ans.iter().enumerate().fold((0, std::i32::MAX), |mut a, v| {
        {if v.1 != &-1 && v.1 < &a.1 && ! explored.contains(&(v.0 as i32)) {a = (v.0, v.1.clone());}} a
      });
    // Add the newly picked node to explored
    explored.insert(next_node as i32);
    // And set its cost to be that weight
    ans[next_node] = cost;
    
    // Cloning the array is probably unnecessary, but it results in simpler code.
    let next_costs = g[next_node].clone();
    
    // For each node j
    for j in 0..size {
      // Skip if it has already been explored
      if explored.contains(&(j as i32)) {
        continue;
      } else if next_costs[j] == -1 {
        // also skip if there is no edge between the new node and j
        continue;
      } else if ans[j] == -1 {
        // If there was no edge between j and s, we don't have to compare costs, so
        //   just unconditionally update it.
        ans[j] = next_costs[j] + cost;
        continue;
      } else {
        ans[j] = cmp::min(ans[j], next_costs[j] + cost);
      }
    }
  }
  ans
}
