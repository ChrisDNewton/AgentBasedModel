"""
Assessment 1: Agent Based Model - Model file
GEOG5995 Programming for Social Scientists: Core Skills [Python]
Leeds student number 201190819
"""

#Import required libraries
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import os

#check if an 'output' folder exists, and create one if not -
if not os.path.isdir ('./output'):
	os.mkdir ('./output')

"""    
Ask user to input model parameters. 
On value error, request valid integer, else use default values.
"""

while True:
    try:
        num_of_agents = int(input("Enter number of agents: "))
        break
    except ValueError:
        print("Please enter a valid integer.")
    else:
        print("Default value of 100 assigned.")
        num_of_agents = 100
        
while True:
    try:
        num_of_iterations = int(input("Enter number of iterations: "))
        break
    except ValueError:
        print("Please enter a valid integer.")
    else:
        print("Default value of 50 assigned.")
        num_of_iterations = 50

while True:
    try:        
        neighbourhood = int(input("Enter size of neighbourhood: "))
        break
    except ValueError:
        print("Please enter a valid integer.")
    else:
        print("Default value of 20 assigned.")
        neighbourhood = 20

"""
#Create an empty list of agents 
"""
agents = []

"""
#Create a 2D frame of the agents' environment - 
"""
fig = matplotlib.pyplot.figure(figsize=(6, 6))
ax = fig.add_axes([0, 0, 1, 1])

"""
#Define a function for measuring the distance between agents - 
"""
def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5

"""
#Read the input file in as an environment - 
"""
environment = []
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    rowlist = []
    #rowlist.append(row)
    for value in row:				# A list of value
        #print(value) 				# Floats
        rowlist.append(value)           #add the value to the rowlist
    environment.append(rowlist)         #add the rowlist to the environment        

f.close() 	# Close the reader

"""
# Create the specified number of agents, looping through the agentframework file
"""
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

# Move the agents.
for j in range(num_of_iterations): #For each iteration...
    #print(str(j))
    for i in range(num_of_agents): #loop through each agent carrying out their functions.
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

"""
#plot the graph
"""
matplotlib.pyplot.xlim(0, 300) #set the boundaries of the x axis
matplotlib.pyplot.ylim(0, 300) #set the boundaries of the y axis
matplotlib.pyplot.imshow(environment) #display the environment

for i in range(num_of_agents): #loop through all the agents and display them
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.savefig('./output/plot.png', bbox_inches='tight') #Save the figure in the output folder
matplotlib.pyplot.show() #Display the figure in the IPython console


"""
#Write the changed environment to a file in the output folder - 
"""
f2 = open('./output/EnvOut.txt', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		# List of values.
f2.close()

"""
#Write the total amount stored by all the agents into a text file
"""
#Create an empty list of Agent's stores
storelist = []

f2 = open('./output/AgentStore.txt', 'a', newline='') 
writer = csv.writer(f2, delimiter=',')
for i in agents:		          #Loop through each agent
    storelist.append(i.store) #appending their data to the AgentStore file (rather than overwrite it)
writer.writerow(storelist)		# List of values.
f2.close() #Close the writer