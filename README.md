# Tic Tac Toe Game Documentation

## **Introduction**

Welcome to the documentation for the **Tic Tac Toe game**. This document provides an overview of the game, its rules, and how to play it. Whether you're a player looking to learn how to play or a developer interested in the code, this guide has you covered.

## **Table of Contents**

1. [Game Overview](#1-game-overview)
2. [Game Rules](#2-game-rules)
3. [How to Play](#3-how-to-play)
4. [Code Structure](#4-code-structure)
5. [Contributing](#5-contributing)

## **1. Game Overview**

Tic Tac Toe is a classic two-player game where the goal is to be the first to form a line of three of your marks (either 'X' or 'O') on a 3x3 grid. The game is played on a console and allows two players to take turns.

## **2. Game Rules**

The rules for playing Tic Tac Toe are straightforward:

- The game is played on a 3x3 grid.
- There are two players: Player 1 ('X') and Player 2 ('O').
- Players take turns placing their marks ('X' or 'O') on an empty cell of the grid.
- The game ends when one player forms a line of three of their marks horizontally, vertically, or diagonally, or when there are no more empty cells.
- If no player forms a line and there are no empty cells, the game is a draw.

## **3. How to Play**

Playing Tic Tac Toe is simple:

1. Run the game.
2. Choose whether you want to be 'X' or 'O'.
3. Follow the on-screen instructions to take turns.
4. The game will announce the winner or declare a draw when the game ends.
5. You can replay the game as many times as you like.

## **4. Code Structure**

The code for the Tic Tac Toe game is structured as follows:

- `display_board(board)`: Function to display the current state of the game board.
- `player_input()`: Function to allow players to choose their markers ('X' or 'O').
- `place_marker(board, marker, position)`: Function to place a marker on the board.
- `win_check(board, mark)`: Function to check if a player has won the game.
- `choose_first()`: Function to randomly determine which player goes first.
- `space_check(board, position)`: Function to check if a cell on the board is empty.
- `full_board_check(board)`: Function to check if the board is full.
- `player_choice(board)`: Function to get a player's choice of position.
- `replay()`: Function to ask if players want to play another round.
- Game loop: A loop that manages the flow of the game.

## **5. Contributing**

If you're interested in contributing to the project, feel free to fork the repository, make improvements, and submit pull requests. Contributions are welcome!

