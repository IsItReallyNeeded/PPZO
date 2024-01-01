# Rock Paper Scissors using Markov chain

Description of the program
The program " Rock, Paper, Scissors" is a simple simulation of a game in which the user competes against the computer. The program uses strategies and a transition matrix to learn the best choice based on the history of the game. After the simulation, the user has the opportunity to face the learned computer. After the simulation and gameplay against the computer are completed, graphs are displayed with the results of the game. 

Code description

1. Import the necessary libraries

2. Initalization of game states and transition matrix

3. Function `prepare_data`
Performs a simulation of game where ai learns with random choice.

4. Function `update_transition_matrix` that takes values of previous state, current state and result updates transition matrix based on result of the round.
Aktualizuje macierz przejść na podstawie wyniku rundy, zwiększając prawdopodobieństwo wygranej strategii i zmniejszając pozostałe.

5. Function `check_result`
checks what is the result of the round and displays information about it

6. Function `main`
performs interaction with user, counts points and displays charts

USAGE:
1. Run the program.
2. Choose `y` if you want to learn AI with random or `n` if you want to start playing.
3. Choose 1 out of 3 (`rock`,`paper`,`scissors`) and watch results.
4. Choose `y` if you want to continue playing or `n` if you want to end the game and display chart.
