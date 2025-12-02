#This file showcases the random subpackage of numpy.
# It also features code incorporating all previous info presented

import numpy as np
np.random.rand() #?pseudo-random numbers

#! Set the seed for the random numbers - keep the same random numbers being generated
np.random.seed(123) #? ensures reproducibility - other people can test in the same way as you
#?first random number
np.random.rand()
#?second random number
np.random.rand()

#! COIN TOSS problem - RANDOM STEP
np.random.seed(123)
coin = np.random.randint(0,2) #? randomly generate 0 or 1
print(coin)
if coin % 2 == 0:
    print("heads")
else:
    print("tails")

# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice > 2 and dice <=5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

#what is above is a random step, but if you want to do it
#multiple times it would be called a random walk 
# (path of molecules, gambler's finalcial status)

np.random.seed(123)
outcomes = []
for x in range(10): #? generates a list of numbers that you can use to iterate over
    coin = np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads") #? appends to the list
    else:
        outcomes.append("tails")
print(outcomes)

#! RANDOM WALK
np.random.seed(123)
tails = [0]
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
print(tails[-1]) #tells how often tails was thrown


# NumPy is imported, seed is set
# Initialize random_walk
random_walk = [0]

for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        # step = step - 1
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1) #? returns the max value
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

#? visualize the random walk
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

#DISTRIBUTION of random walks
#distribution of final steps (because the walks are random)

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
final_tails = []
for x in range(100): #10000 is better
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    #each number from this list is the number of tails that were thrown in a game of 10 tosses
    final_tails.append(tails[-1]) 
print(final_tails)
plt.hist(final_tails, bins = 10)
plt.show()

#!-------------------------
# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(5) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw) #? initial il vede ca pe 101 linii de cate 5 puncte fiecare
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw) #? dupa care transpose ii zice e invers

# Plot np_aw_t and show
plt.plot(np_aw_t) #? si apoi ies 5 linii cu cate 101 puncte fiecare
plt.show()

#!--------------------------------------
#making a histogram of the ends
# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()