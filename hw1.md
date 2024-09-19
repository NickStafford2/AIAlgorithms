Assignment # 1
Artificial Intelligence
Fall 2024
Due on Thursday, September 19 by midnight

Total score: 100 + Bonus Problem (10 points)

Penalty if submitted after 12 AM and before 6 AM next day : 10 points, and no bonus score
No assignment accepted after 6 AM on Sept 20, 2023.
All problems are mandatory. Each subproblem should be explained well and should be at least
half a single spaced page; short, vague or cryptic answers will get you a zero. Algorithm should
be written using discrete structure symbols as explained. No credit will be given for Problem #2
if algorithm is just bunch of natural language explanations. Please submit a PDF file to the
Canvas under HW # 1. If you can not convert to PDF version, submit a Microsoft word version
that TA would convert into PDF version.


# 1. Conceptual type questions (5 pts X 8 problems) 40 points
## a. Explain the rationale behind heuristic search being fast yet incomplete.
In real life, finding perfect solutions may not be phesable. Algorithms may take too long to run or be to complex to implement. The goal state may not be known. Sometimes it does not matter that the goal state is not achieved, and close enough may be acceptable. For all these reasons, heuristics may be prefered to algorithms. 


## b. Explain triangular inequality of heuristic functions.
When traversing a graph, the distance between two directly connected nodes must be less than an indirect route with the same start and end points, but additional nodes are travesed on the route. 

The distance of direct route from A to C is less than the distance of the indirect route from A to B to C. 

## c. Explain the problems of global heuristic searches.
While a global heuristic search may find the optimal solution, it may require unacceptably large resources to complete. They may not be practical in large complex datasets used in the real world. 


## d. Explain the problems of local search.
While local searches may be fast or efficient, they may not find the optimal solution. 


## e. Explain simulated annealing abstractly including the use of probability, temperature, temperature drop rate, and stochastic nature in the algorithm.
Simulated annealing is inspired by the annealing process in metallurgy where a hot metal is gradually cooled. As the temperature of the metal cools, the atoms in the metal rearange themselves to a more ordered state which makes the resulting metal less brittle. In simulated annealing the initial solution represents the hot metal, the optimal solution represents the stronger cooled metal, and a control parameter is adjusted to represent the gradual cooling of the metal until the optimal state is reached.

Random pertubations are recursively used to adjust the initial solution. The peretubation represents a new state. To decide if the new state is accepted, a stochastic algorithm is used that usually accepts improved states, but sometimes accepts a worse one. Since the improved state is usually chosen, the state improves as interations continue; similar to the cooling metal. However, the occasional acceptance of worse states allows the solution to escape local optima, and eventually an approximate global optima is reached. 


## f. Explain genetic algorithms using a simple figure.
The genetic algorithm is inspired by the method DNA replicates itself during evolution.Similar to chromosomes during DNA replication, a variety of inital states are selected and evaluated to estimate their quality. Crossover selection is represented in the algorithm by merging two of the better current solutions, to hopefully produce an even better solution. As this process is recursively performed, the batch of potential next states improves. This is done until an approximate global state is reached. 


<add figure here> 


## g. Explain min-max algorithm in adversarial game search, its properties and limitations.
This algorithm is used to aproximate the optimal next move in an game. It assumes the opponent will make an optimal move for themselves. In the algorithm, a maximizer tries to get the highest score possible to represent ones own move, and a minimizer tries to find the lowest score to represent an opponents counter-move. The resulting states are calculated and an ideal move is selected. 

This algorithm looks ahead several moves and guesses the future state assuming opponent makes their own optimal moves. This results in the algorithm selecting a move that is the most beneficial in the long run. 

This algorithm is limited by how computationally difficult it is to look ahead and predict future states. Some games have potential states that grow exponentally with each turn, so the look ahead is limited. Additionally, the algorithm may not accurately predict the opponents move, so potental better states may be missed. 


## h. Explain the ant colony optimization.
This algorithm is inspired by the methods ants use when foraging for resources. The ants give off pheromones as they forage, and the concentration of pheremones signal other ants tho persue a route or resource. 


# 2. Write a memory bound A* algorithm that retains at most M% of the total fringe at any time where M is a parameter using universal and existential quantifiers and set-based abstractions. Discard the p% worst cost fringe candidates after every move. The value of p improves linearly as the search progresses at the rate of r%. There will be no credit for writing natural language explanations or writing a program. 10 points

Local Search: An ant is searching for food. The intensity of the nectar’s scent is given in the matrix
cells. Ant is at location (1, 1) and the nectar is at location (4, 3), where 4 is the row index and 3 is the
column index as shown in the figure. The ant can move horizontally, vertically and diagonally. There
are obstructions in three cells where ant cannot go. The cells are (2, 1), (3, 3) and (4, 1). Draw the tree
for possible movements, and the best path taken by ant assuming that ant can sense the smell up to
only two cells beyond horizontally and vertically and one cell diagonally. For example, at (1, 1), she can
sense the smell in (1, 2), (2, 1), (1, 3), (3, 1) and (2, 2).


figure 1



4. Given a population of 4 initial positions in a 4 X 4 board of N-queens given as the column
vector <1, 3, 2, 4>, < 1, 1, 1, 1>, <1, 2, 3, 4>, <1, 1, 2, 4>, Use local search and movement
of one queen picked randomly to place the queen such that the number of attacking queen
reduces for each of initial positions separately. Show at least four moves. Use random
number generator from a computer to pick up the column number of the queen to be moved.
Show the process and the table of random number generated. Do not use your brain power
to generate random numbers. 10 points
5. For the example in the book (see Figure on the next page), work out if a person has to travel
from Neamt to Craiova. Show the steps for greedy best first search and A* search. Measure
the distance from Neamt using a ruler, and convert to mile knowing that one centimeter is
approximately equivalent to 40 miles in the map for heuristic estimation. 20 points
6. Min-max tree: For the following Min-max tree identify the min-max value at each node,
and using alpha-beta pruning identify which branches need not be explored. Explain clearly
the rationale, specify the
α-
β condition which applies for each node not to be expanded. No
credit for just specifying answers.


Bonus Problem
7. For a 6 X 6 board, design a good connect four evaluation-function for in-max trees
assuming that a players (including computer) can see only upto two moves ahead and
show the Min-Max tree for the next two moves by human and two moves by the
computer for the following board position. Assume that red belongs to human; black
belongs to computer. The next move is for the human.


figure s below










