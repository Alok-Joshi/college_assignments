### Assignment 2
from queue import PriorityQueue
import pdb


def hueristic(node):
    #Straight line distance hueristic
    #4 is the goal state, 0 is our starting state here
    # key is the state, and value is the straight line distance from the goal state

    dist_dict = { 0: 5, 1: 6, 2: 2, 3: 1, 4: 0}
    return dist_dict[node]



adj_mat = [[1,2],[0,3,4],[0,3,4],[0,1,2,4],[1,2,3]]

visited = set()
start_state = 0
goal_state =  4

pq =PriorityQueue()

pq.put(start_state)
path = []

while(not pq.empty()):
      state = pq.get()
      pdb.set_trace()
      visited.add(state)
      path.append(state)

      if(state == goal_state):
         break;

      else:
        for i in adj_mat[state]:
                if(i not in visited):
                    pq.put(hueristic(i))
    
        
            

print(f"Final Path: {path}")



