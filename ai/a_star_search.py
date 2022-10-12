from queue import PriorityQueue
import copy

def h(state_obj,goal_state):
    """ Heuristic Function for State """
    h_score = 0

    for i in range(len(state_obj)):

        for j in range(len(state_obj[i])):
                if(state_obj[i][j] != goal_state[i][j]):
                    h_score  = h_score +1 

    return h_score

class State:
    def __init__(self,state_data,g,f_score)
        self.state_data = state_data;
        self.g = g
        self.f_score = f_score

    def generate_sucessor_states(self,goal_state):
        """ Generates the sucessor states and returns them """
        generated_nodes = []
        es = []
        for i in range(len(self.state_data)):
            for j in range(len(self.state_data[i])):
                if self.state_data[i][j] == -1:
                   es.append(i)
                   es.append(j)
                   break
                    
        if((es[0]+1) < len(self.state_data) and (es[1]+1) < len(self.state_data[0])):
                new_node = copy.deepcopy(self.state_data)
                temp = new_node[es[0]][es[1]]
                new_node[es[0]][es[1]] = new_node[es[0]+1][es[1]+1]
                new_node[es[0]+1][es[1]+1] = temp

                new_state = State(new_node,self.g+1,h(new_node,goal_state)+self.g+1)
                generated_nodes.append(new_state)

        if((es[0]-1)>= 0  and (es[1]-1)>=0):
                new_node = copy.deepcopy(self.state_data)
                temp = new_node[es[0]][es[1]]
                new_node[es[0]][es[1]] = new_node[es[0]-1][es[1]-1]
                new_node[es[0]-1][es[1]-1] = temp

                new_state = State(new_node,self.g+1,h(new_node,goal_state)+self.g+1)
                generated_nodes.append(new_state)


        if((es[0]+1) < len(self.state_data) and (es[1]-1)>=0):
                new_node = copy.deepcopy(self.state_data)
                temp = new_node[es[0]][es[1]]
                new_node[es[0]][es[1]] = new_node[es[0]+1][es[1]-1]
                new_node[es[0]+1][es[1]-1] = temp

                new_state = State(new_node,self.g+1,h(new_node,goal_state)+self.g+1)
                generated_nodes.append(new_state)


        if((es[0]-1) >= 0 and (es[1]+1) < len(self.state_data[0]) ):
                new_node = copy.deepcopy(self.state_data)
                temp = new_node[es[0]][es[1]]
                new_node[es[0]][es[1]] = new_node[es[0]-1][es[1]+1]
                new_node[es[0]-1][es[1]+1] = temp

                new_state = State(new_node,self.g+1,h(new_node,goal_state)+self.g+1)
                generated_nodes.append(new_state)
        
        return generated_nodes


    def __hash__(self):
        return hash((self.state_data,self.g,self.f_score))
    def __eq__(self,other):
        return (self.state_data == other.state_data) and (self.g == other.g) and (self.f_score == other.f_score)

def a_star(initial_state,goal_state):
    closed = dict() #a map containing visited States and their F scores 
    open_set =PriorityQueue()
    
    open_set.put((initial_state.f,initial_state))

    while(open_set.empty() == False):

        state_obj = open_set.get()

        if(state_obj == goal_state):
            return state_obj

        elif(state_obj.state in closed):
            if(state_obj.f_score < closed[state_obj]):
                closed[state_obj] = state_obj.f_score
            else:
                continue
        else:
            closed[state_obj.state] = state_obj.f_score
            generated_nodes = state_obj.generate_sucessor_states()

            for node in generated_nodes:
                if(node not in closed):
                    open_set.put((node.f_score,node))
                


            


