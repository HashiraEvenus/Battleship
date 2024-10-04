# Battleship Game

A classic Battleship game implemented in Python using Pygame. Play against an AI opponent with normal or hard difficulty modes!

## Overview

This Battleship game allows you to play against an AI opponent with two difficulty settings:

- **Normal Mode**: The AI makes one move per turn.
- **Hard Mode**: The AI continues to make moves until it misses.

## Features

- Graphical interface using Pygame
- Manual ship placement by the player
- Random ship placement for the AI
- Visual indicators for hits, misses, and ship placements
- Main menu and game over screens

## Prerequisites

- Python 3.x
- Pygame library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/battleship-game.git
   ```
2. Navigate to the project directory:
   ```
   cd battleship-game
   ```
3. Install the required dependencies:
   ```
   pip install pygame
   ```

## How to Play

1. Run the game:
   ```
   python main.py
   ```

2. **Main Menu**:
   - Normal Mode: AI makes one move per turn
   - Hard Mode: AI continues to make moves until it misses
   - Quit: Exit the game

3. **Ship Placement**:
   - Place Your Ships Manually:
     - Click on the player's grid (left grid) to place your ships
     - Press the R key to rotate the ship between horizontal and vertical orientation
     - Ships must be placed within the grid without overlapping

4. **Gameplay**:
   - Your Turn:
     - Click on a cell in the AI's grid (right grid) to attack
     - A red square indicates a hit, and a gray square indicates a miss
   - AI's Turn:
     - The AI will make its move automatically
     - Hits and misses will be displayed on your grid

5. **Winning the Game**:
   - The game ends when all ships of one player are sunk
   - A game over screen will display the winner
   - Choose to play again or quit from the game over screen

## Controls

- **Mouse Left Click**: Select cells for placing ships and making attacks
- **R Key**: Rotate the ship during the placement phase
- **Esc Key**: Quit the game at any time

## Game Screens

1. **Main Menu**
   - Choose between Normal Mode, Hard Mode, or Quit the game

2. **Ship Placement**
   - Place your ships manually on the grid. Use the R key to rotate the ship

3. **Gameplay Screen**
   - Left Grid: Your grid showing your ships, hits, and misses
   - Right Grid: AI's grid where you attack