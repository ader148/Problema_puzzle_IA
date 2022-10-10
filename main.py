from Node import  Node
from BreadthFirstSearch import BreadthFirstSearch
#from Jarra import Jarra
from Puzzle import Puzzle

def main():
    #inicial=Node((3,1,2,4))
    inicial=Node((3,1,4,2))
    final=Node((1,2,3,4))
    
    puzzle = Puzzle(inicial, final) 
    bfs=BreadthFirstSearch(puzzle)
    solution=bfs.run()
    print(solution)
    
if __name__ == "__main__":
    main()
