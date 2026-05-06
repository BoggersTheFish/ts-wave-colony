# Basic Agent skeleton
class TSAgent:
    def __init__(self, name, initial_graph=None):
        self.name = name
        self.graph = initial_graph  # Will connect to TS-Core later
        self.goals = []
    
    def propagate(self):
        pass
    
    def sense_colony_field(self, field):
        pass
        
print('TSAgent ready')