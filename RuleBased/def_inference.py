class InferenceEngine:

    def __init__(self, rules):#what needs to be initialised?
        self.rules = rules

        


    def infer_next_action(self, current_state):
       for rule in self.rules:
            if rule.matches(current_state):
                return rule.execute(current_state)


       

    #PSEUDOCODE:
    #Agent Initialised on initial state
    #Rule stack initialised 
    #Agent checks if goal
    #if no:
    #   Agent checks if visited
    #   if no:
    #      agent takes from top of rule stack
    #      can agent go this way?
    #      if yes:
    #           agent goes that way
    #           agent checks if goal
    #           if no:
    #               go back to ln(24)
    #           if yes: 
    #               maze complete!
    #                
    #     if no:
    #           agent pops that movement from stack 
    #           and chooses next rule
    #           go back to ln(28)
    #   if yes: 
    #       pop rule from stack and use next rule
    #if yes:
    #   goal reached


    #PSEUDOCODE 2
    #Agent Inititalised at start point
    #Rule Stack Initialised
    #Check if goal
    #If Yes:
    #   Maze Complete!
    #If No:
    #   Check If Visited
    #   If No:
    #       Use Top Rule
    #       Go Back ln(50)
    #   If Yes:
    #       Check what Rule was used last time(Gonna need another List)(Or at least add another item to the list which states which Rule I used when I last visited the square)
    #       Pop rules off of rule stack until previous rule is removed
    #       If all Rules are removed: 
    #           Maze Unsolvable
    #       Else: 
    #           Use rule!           