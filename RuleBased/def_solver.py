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
        goal_x, goal_y = 9, 9
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



    def apply_rules(self):
        #writing here so i dont forget, issue is that when rule is added to dictionary, it is added to
        #the cell it went to not the cell it came from.
        #so if I used move_right on 0,0 the move_right is added to 0,1 not 0,0
        x, y, _ = self.current_state  # Extract x and y from the current state
        
        visited_rules = self.visitedCellsAndRuleUsed.get((x, y), set())  # Get the set of used rule names for the current state

        # Iterate over the rule stack
        for rule in self.ruleStack:
            rule_name = rule.action.__name__
            # Check if the rule can be applied and has not been used before for this state
            if rule.condition(self.current_state, self.visitedCellsAndRuleUsed, rule) and rule_name not in visited_rules:
                next_state = rule.action(self.current_state, self.visitedCellsAndRuleUsed, rule)
                if not self.is_visited(self.current_state):
                    self.mark_visited(self.current_state, rule)
                self.current_state = next_state
                return rule, self.current_state

        return None, None  # No valid rule found or all rules exhausted


    
    def solve_maze(self):
        i = 0
        while True and i < 100:
            i += 1
            print("Iteration Number: ", i)  
            print("Current state: (x={}, y={})".format(self.current_state[1], self.current_state[0]))
            #print("Visited Cells: ", self.visitedCellsAndRuleUsed)
            if is_goal(self.current_state, self.goal_state):
                print("Maze Complete!")
                break
            #should I be starting with this? idk something seems off but maybe not.
            rule, new_state = self.apply_rules()
            x, y, _ = new_state
            #print("NEW STATE: ", (y,x))
            print("Rule used to get to this state is: ", rule.action.__name__)

            #print("ENDOFIT")
  

