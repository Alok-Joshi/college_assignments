from queue import PriorityQueue
class State:
    def __init__(self,state,g):
        self.state = state;
        self.g = g;

def h(state):
    """ Heuristic function """
    pass

def generate_sucessor_states(state_obj):
    """ Generates the sucessor states """
    pass

def a_start(initial_state,goal_state h,generate_sucessor_states):
    closed_list =[]
    open_set =PriorityQueue()
    
    init_state_obj = State(initial_state,0);
    open_set.put((0,init_state_obj))

    while(open_set.empty() == False):

        state_obj = open_set.get()

        if(state_obj == goal_state):
            return state_obj

        else:
            closed_list.append(state_obj)
            generated_nodes = generate_sucessor_states(state_obj)

            for node in generated_nodes:
                if(node not in closed_list and node not in open_set):
                    #if the generated node is already in the open set, we compare the g (Because h will be same). For now, i am assuming that the g of the node already in the open_set is lower, hence we ignore the generated node 
                    res = State(node,1+state_obj.g)
                    f = res.g + h(res)
                    open_set.put((f,res))
                


            


