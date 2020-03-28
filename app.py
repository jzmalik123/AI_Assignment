from queue import SimpleQueue
from node import Node

MNT = str(input())
MNT = MNT.split()
M=int(MNT[0])
N=int(MNT[1])
T=int(MNT[2])
states = []
actions = []
transition_table = []
for i in range(M):
    states.append(input())
for i in range(N):
    actions.append(input())
# take input in graph
for i in range(M):
    row = []
    row = input().split()
    row = [int(z) for z in row]
    transition_table.append(row)
def search(start_goal):
        start = start_goal[0]
        goal = start_goal[1]
        """"
        print("The table is: ", transition_table)
        print("The states are: ", states)
        print("The actions are:", actions)
        print("The start is:", start)
        print("The goal are:", goal)
        """
        initial_state = Node(None,start,None)
        if initial_state.state == goal:
            return "Do Nothing"
        frontier = SimpleQueue()
        explored_set = []
        frontier.put(initial_state)
        solution = []
        while True:
            if frontier.empty():
                return "Goal Unachieveable"
            node = frontier.get()
            #print(node.action)
            index = states.index(node.state)
            #print(index)
            count = 0
            explored_set.append(index)
            #put the children in frontier
            for child in transition_table[index]:
                if child not in explored_set and child is not index:
                    #print(child)
                    if goal == node.state:
                        return
                    explored_set.append(child)
                    #print(explored_set)
                    #print(actions[count])
                    solution.append(actions[count])
                    if goal == states[child]:
                        return solution
                    frontier.put(Node(node,states[child],actions[count]))
                    break
                count = count+1

def main():
    for x in range(T):
        start_goal = input().split("\t")
        solution = search(start_goal)
        for i in range(len(solution)):
            print(solution[i],end="")
            if i is not len(solution)-1:
                print("->",end="")
        print("")

main()
