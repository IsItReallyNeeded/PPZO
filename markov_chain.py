import random
import matplotlib.pyplot as plt
import numpy as np

# Define the possible states (rock, paper, scissors)
states = ["rock", "paper", "scissors"]

# Initialize the transition matrix with equal probabilities to start
transition_matrix = np.full((3, 3), 1.0 / 3)


def prepare_data(n=1000):
    k_stats = {"rock": 0, "paper": 0, "scissors": 0}
    p_stats = {"rock": 0, "paper": 0, "scissors": 0}
    n_stats = {"win": 0, "loss": 0, "tie": 0}

    prev_move = None

    for _ in range(n):
        # Use the transition matrix to determine the AI's move
        if prev_move is not None:
            si_move_index = np.random.choice(3, p=transition_matrix[states.index(prev_move)])
        else:
            si_move_index = random.randint(0, 2)
        si_move = states[si_move_index]

        # Let the player choose a move
        player_move = get_player_move()

        result = check_result(player_move, si_move)

        # Update the transition matrix based on the result
        if prev_move is not None:
            update_transition_matrix(states.index(prev_move), states.index(player_move), result)

        k_stats[si_move] += 1
        p_stats[player_move] += 1
        n_stats[result] += 1

        prev_move = player_move

    print(k_stats, p_stats, n_stats)
    return k_stats, p_stats, n_stats


def update_transition_matrix(prev_state, current_state, result):
    # Adjust the transition matrix based on the result of the round
    if result == "win":
        transition_matrix[prev_state][current_state] += 0.1
    elif result == "loss":
        transition_matrix[prev_state][current_state] -= 0.1

    # Ensure probabilities are non-negative
    transition_matrix[transition_matrix < 0] = 0

    # Normalize the row to make sure probabilities sum to 1
    row_sum = np.sum(transition_matrix[prev_state])
    transition_matrix[prev_state] /= row_sum


def check_result(player_move, si_move):
    if player_move == si_move:
        return "tie"
    elif (player_move == "rock" and si_move == "scissors") or \
            (player_move == "paper" and si_move == "rock") or \
            (player_move == "scissors" and si_move == "paper"):
        return "win"
    else:
        return "loss"


def get_player_move():
    return random.choice(states)


def main():
    player_points = 0
    si_points = 0
    prev_move = None
    scores = {"Player": [], "AI": []}  # Track scores over time

    train_si = input("Do you want to train the AI? (y/n): ").lower()

    while train_si not in ["y", "n"]:
        train_si = input("Please provide a valid answer (y/n): ").lower()

    k_stats, p_stats, n_stats = None, None, None
    if train_si == "y":
        k_stats, p_stats, n_stats = prepare_data()

    while True:
        # Use the transition matrix to determine the AI's move
        if prev_move is not None:
            si_move_index = np.random.choice(3, p=transition_matrix[states.index(prev_move)])
        else:
            si_move_index = random.randint(0, 2)
        si_move = states[si_move_index]

        player_move = input("Your move (rock/paper/scissors): ").lower()

        while player_move not in states:
            player_move = input("Please provide a valid move (rock/paper/scissors): ").lower()

        prev_move = player_move
        result = check_result(player_move, si_move)

        if result == "loss":
            si_points += 1
        elif result == "win":
            player_points += 1

        scores["Player"].append(player_points)  # Append player score
        scores["AI"].append(si_points)  # Append AI score

        print(f"Player Points: {player_points}")
        print(f"AI Points: {si_points}")

        decision = input("Do you want to continue the game? (y/n): ").lower()
        if decision == "n":
            plt.plot(scores["Player"], label="Player")
            plt.plot(scores["AI"], label="AI")
            plt.xlabel("Rounds")
            plt.ylabel("Points")
            plt.legend()
            plt.title("Game Progression")
            #plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
            plt.show()

            break


if __name__ == '__main__':
    main()
