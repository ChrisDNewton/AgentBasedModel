"""
Assessment 1: Agent Based Model - Agent class file
GEOG5995 Programming for Social Scientists: Core Skills [Python]
Leeds student number 201190819
"""

#Import the random library
import random

#Define an agent class with an __init__ method - 
class Agent():
    #initialise the agent, set the environment and its location - 
    def __init__ (self, environment, agent):
        self.environment = environment # Set the agent's environment
        self.store = 0 # Set the store to zero
        self.agent = agent        
        self.x = random.randint(0,300) #set a random x coordinate
        self.y = random.randint(0,300) #set a random y coordinate        

    #Define a function for agent movement - 
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

    #Define a function for eating behaviour - 
    def eat(self): 
        if self.environment[self.y][self.x] > 10: #if the environment value is greater than 10...
            self.environment[self.y][self.x] -= 10 #remove 10 from the environment...
            self.store += 10                        #...and store it in the agent.
        #eat what is left-
        elif self.environment[self.y][self.x] < 10: #if the env value is less than 10...
            self.store += self.environment[self.y][self.x] #...the agent eats it...
            self.environment[self.y][self.x] = 0            #..so zero remains.

    #Define a function for sharing with neighbours - 
    def share_with_neighbours(self, neighbourhood):
        #Loop through the agents in self.agent
        random.shuffle(self.agent) #randomise the order to avoid earlier ones having an unfair advantage.
        for agent in self.agent:
            # Calculate the distance between self and the current other agent:
            # distance = self.distance_between(agent)
            dist = self.distance_between(agent)
            # If distance is less than or equal to the neighbourhood
            if dist <= neighbourhood:
            #sum self.store and agent.store.
                sum = self.store + agent.store
                ave = sum / 2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave)) #statement to test if sharing works
   
    #Define a function for measuring distance between 2 agents via Pythagoras - 
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5            

    #Define __str__ as a way of returning an agent's location and current store -         
    def __str__(self):
        return "x = " + str(self.x) + ", y = " + str(self.y)

            # x = property(move, "I'm the 'x' property.")
            # y = property(move, "I'm the 'y' property.")