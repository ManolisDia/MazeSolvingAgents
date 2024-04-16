from def_rules import Rule, can_move_right, move_right, can_move_down, move_down, can_move_up, move_up, can_move_left, move_left
from def_maze_entry_point import maze
from def_rules import is_goal

class Solver:
    def __init__(self):
        self.visitedCellsAndRuleUsed = {}
        self.maze = maze
        
        start_x, start_y = 0, 0
        self.initial_state = (start_x, start_y, self.maze)  
        goal_x, goal_y = 4, 5
        self.goal_state = (goal_x, goal_y, self.maze) 
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
        x, y, _ = state  
        self.visitedCellsAndRuleUsed[(x, y)] = rule

    def apply_rules(self):
        for rule in self.ruleStack:
            if rule.condition(self.current_state):
                next_state = rule.action(self.current_state)
                return rule, next_state
        return None, None  # No valid rule found
    
    def solve_maze(self):
        while True:
            print("Current state: (x={}, y={})".format(self.current_state[1], self.current_state[0]))
            if is_goal(self.current_state, self.goal_state):
                print("Maze Complete!")
                break
            
            rule, next_state = self.apply_rules()
           
            if rule is not None and next_state is not None:
                if not self.is_visited(next_state):
                    self.mark_visited(next_state, rule)
                    print("Visited Cells: ", self.visitedCellsAndRuleUsed)
                    self.current_state = next_state
                    print("The Rule used is: ", rule.action.__name__)
                else:
                    # Get the last rule used at this visited cell
                    last_rule_used = self.visitedCellsAndRuleUsed[next_state]
                    # Find the index of last_rule_used in the ruleStack
                    last_rule_index = self.ruleStack.index(last_rule_used)
                    # Rotate the ruleStack to start from the next rule after last_rule_used
                    self.ruleStack = self.ruleStack[last_rule_index+1:] + self.ruleStack[:last_rule_index+1]
                    continue  # Skip checking further rules for this iteration


