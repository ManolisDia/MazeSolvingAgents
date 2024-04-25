from def_rules import Rule, can_move_right, move_right, can_move_down, move_down, can_move_up, move_up, can_move_left, move_left
from def_maze_entry_point import maze
from def_rules import is_goal

class Solver:
    def __init__(self):
        self.visitedCellsAndRuleUsed = {}
        self.maze = maze
        
        start_x, start_y = 0, 0
        self.initial_state = (start_x, start_y, tuple(map(tuple, self.maze)))
        goal_x, goal_y = 4, 5
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
            self.visitedCellsAndRuleUsed[(x, y)] = set()
        self.visitedCellsAndRuleUsed[(x, y)].add(rule_name)
        print("Added the rule: ", rule_name, " to the cell: ", (y, x))

    def apply_rules(self):
        x, y, _ = self.current_state
        visited_rules = self.visitedCellsAndRuleUsed.get((x, y), set())

        for rule in self.ruleStack:
            if rule.condition(self.current_state):
                next_state = rule.action(self.current_state)
                if not self.is_visited(next_state):
                    self.mark_visited(self.current_state, rule)
                    self.current_state = next_state
                    return rule, self.current_state

        for rule in self.ruleStack:
            rule_name = rule.action.__name__
            if rule.condition(self.current_state) and rule_name not in visited_rules:
                next_state = rule.action(self.current_state)
                self.mark_visited(self.current_state, rule)
                self.current_state = next_state
                return rule, self.current_state
        
        print("No valid moves left from this state.")
        return None, None  # No valid rule found or all rules exhausted
   
    def print_maze(self):
        display_maze = [list(row) for row in self.maze]
        x, y, _ = self.current_state
        display_maze[x][y] = 'A'
        for (vx, vy), rules in self.visitedCellsAndRuleUsed.items():
            if (vx, vy) != (x, y):
                display_maze[vx][vy] = 'V'
        for row in display_maze:
            print(' '.join(str(cell) for cell in row))
        print()

    def solve_maze(self):
        while True:  
            self.print_maze()
            print("Current state: (x={}, y={})".format(self.current_state[1], self.current_state[0]))
            if is_goal(self.current_state, self.goal_state):
                print("Maze Complete!")
                return True
            rule, new_state = self.apply_rules()
            if new_state is None:
                print("Maze Unsolvable!")
                return False
  
