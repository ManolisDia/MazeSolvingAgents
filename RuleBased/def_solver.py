from def_rules import Rule, can_move_right, move_right, can_move_down, move_down, can_move_up, move_up, can_move_left, move_left
from def_maze_entry_point import maze
from def_rules import is_goal

class Solver:
    def __init__(self):
        #initialize a dictionary to keep track of visited cells and the rules used to visit them

        self.visitedCellsAndRuleUsed = {}
        self.maze = maze
        
        start_x, start_y = 0, 0
        # Convert maze (a list) to a tuple to make the state immutable
        self.initial_state = (start_x, start_y, tuple(map(tuple, self.maze)))
        goal_x, goal_y = 4,5
        self.goal_state = (goal_x, goal_y, tuple(map(tuple, self.maze))) 
        self.current_state = self.initial_state

        self.ruleStack = [
            Rule(condition=can_move_right, action=move_right),
            Rule(condition=can_move_down, action=move_down),
            Rule(condition=can_move_up, action=move_up),
            Rule(condition=can_move_left, action=move_left)
        ]

    
    def is_visited(self, state):
        x, y, _ = state  
        return (x, y) in self.visitedCellsAndRuleUsed

    def mark_visited(self, state, rule):
        rule_name = str(rule.action.__name__)
        x, y, _ = state
        if (x, y) not in self.visitedCellsAndRuleUsed:
            self.visitedCellsAndRuleUsed[(x, y)] = set()  # Initialize with an empty list
        self.visitedCellsAndRuleUsed[(x, y)].add(rule_name)
        print("Added the rule: ", rule_name, " to the cell: ", (y, x))



    def apply_rules(self):

        x, y, _ = self.current_state
        
        visited_rules = self.visitedCellsAndRuleUsed.get((x, y), set()) 
        #print("list of cells and rules used: ", self.visitedCellsAndRuleUsed)
        #first prioritize unvisited cells
        for rule in self.ruleStack:
            next_state = rule.action(self.current_state)
            if rule.condition(self.current_state) and not self.is_visited(next_state):
                next_state = rule.action(self.current_state)
                
                self.mark_visited(self.current_state, rule)
                self.current_state = next_state
                return rule, self.current_state


        #then once you have to use visited cells, prioritize rules you havent used on those cells before
        for rule in self.ruleStack:
            rule_name = rule.action.__name__
            if rule.condition(self.current_state) and rule_name not in visited_rules:
                next_state = rule.action(self.current_state)
                
                self.mark_visited(self.current_state, rule)
                self.current_state = next_state
                return rule, self.current_state

        print("Returning None, None")
        return None, None  # No valid rule found or all rules exhausted


    
    def solve_maze(self):
        i = 0
        while True and i < 500:
            i += 1
            print("Iteration Number: ", i)  
            print("Current state: (x={}, y={})".format(self.current_state[1], self.current_state[0]))
            #print("Visited Cells: ", self.visitedCellsAndRuleUsed)
            if is_goal(self.current_state, self.goal_state):
                print("Maze Complete!")
                break
            rule, new_state = self.apply_rules()
            

            #print("ENDOFIT")
  

