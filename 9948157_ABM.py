#Import libraries
import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import os

#check if an 'output' folder exists, and create one if not -
if not os.path.isdir ('./output'):
	os.mkdir ('./output')
    

#Ask user to input model parameters
#try and do this using argv, the command line arguments, if possible - see lecture slides
while True:
    try:
        num_of_agents = int(input("Enter number of agents: "))
        break
    except ValueError:
        print("Please enter a valid interger.")
        
while True:
    try:
        num_of_iterations = int(input("Enter number of iterations: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

while True:
    try:        
        neighbourhood = int(input("Enter size of neighbourhood: "))
        break
    except ValueError:
        print("Please enter a valid integer.")


"""
#Set the number of agents - 
num_of_agents = 100
#Set the number of iterations to loop through - 
num_of_iterations = 50
#Set the size of the neighbourhood - 
neighbourhood = 20
"""
#Create an empty list of agents- 
agents = []


#Create a 2D frame of the agents' environment - 
#This seems to affect the axis not being saved on the image though?
fig = matplotlib.pyplot.figure(figsize=(6, 6))
ax = fig.add_axes([0, 0, 1, 1])


#Define a function for measuring the distance between agents - 
def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5

#read the input file in as an environment - 
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

f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

# Move the agents.
for j in range(num_of_iterations): #For each iteration...
    #print(str(j))
    for i in range(num_of_agents): #...loop through each agent carrying out their functions.
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#plot the graph
matplotlib.pyplot.xlim(0, 300) #set the boundaries of the x axis
matplotlib.pyplot.ylim(0, 300) #set the boundaries of the y axis
matplotlib.pyplot.imshow(environment) #display the environment
for i in range(num_of_agents): #loop through all the agents and display them
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.savefig('./output/plot.png', bbox_inches='tight') #Save the figure in the output folder
matplotlib.pyplot.show() #Display the figure in the IPython console

"""
#This is no longer needed; it's in 'agentframework.py'.
#measure the distance between each agent and all the other agents - 
for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)
"""

"""
#print the final coordinates of each agent - 
for i in agents:
    print(i.x, i.y)
"""
    


#Write the new environment to a file in the output folder - 

f2 = open('./output/EnvOut.txt', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		# List of values.
f2.close()

"""
Can you make a second file that writes out the total amount stored by all the 
agents on a line? 
"""
storelist = []

f2 = open('./output/AgentStore.txt', 'a', newline='') 
writer = csv.writer(f2, delimiter=',')
for i in agents:		
    storelist.append(i.store)
writer.writerow(storelist)		# List of values.
f2.close()

#print(agents[0])

"""
Can you get the model to append the data to the file, rather 
than clearing it each time it runs? Use 'a' for append rather than 'w'.
"""

"""
If you want some more practice, here's some ideas for continuing to develop your models:

Add some more behaviour to your model: make the nibblers change dynamics based on how much they have in their stores. For example, you could make them steal more resources from others if they are low, or move quicker if they have more resources.

Add a new type of agent: for example, add wolves that eat nearby sheep. The one thing we haven't done is change the number of agents (remember we discussed removing things from lists in the lecture on loops). In addition, you could add breeding to the sheep and/or wolves to make a full population model.

Adapt the model to represent something different, for example, a simple cops and robbers model (see example here).

Implement more complicated decision making, for example building a spatial version of Axelrod's tournament
"""