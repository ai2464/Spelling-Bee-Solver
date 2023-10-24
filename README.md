# SpellingBeeSolver

SpellingBeeSolver is a Python-based tool to assist players of the New York Times game, "Spelling Bee". This tool not only helps you find possible words but also scores them based on the game's rules.

## Overview

"Spelling Bee" challenges players with a honeycomb of letters, requiring players to generate as many words as possible. Among these letters, one is the central letter that holds specific importance. This solver aids players by generating all potential words and providing a score for each, ensuring they abide by the game's regulations.

### Game Rules:

- **Center Letter**: Each word must include this pivotal letter.
- **Word Length**: Every word should contain at least four letters.
- **Repeating Letters**: Letters can be used multiple times in a word.
- **Word Restrictions**: The provided word list omits words that could be considered offensive, obscure, hyphenated, or are proper nouns.
- **Scoring**: 
  - Four-letter words grant one point each.
  - Words exceeding four letters earn points equivalent to their length.
  - Spotting a “pangram”, a word utilizing all available letters, rewards an additional seven points.

## Getting Started

### Prerequisites

Before diving into the SpellingBeeSolver, ensure you have:

- Python installed on your system.
- A word list named `wordlist.txt` placed in the root directory. This list should avoid including offensive, hyphenated words or proper nouns.

### Installation

1. Clone this repository to your local machine.
```bash
git clone https://github.com/yourusername/SpellingBeeSolver.git
```

## Navigate to the project directory:

```bash
cd SpellingBeeSolver
```
## Usage

Execute the SpellingBeeSolver.py script:

```bash
python SpellingBeeSolver.py
```

Upon running the solver:

1) You'll be prompted to input the set of letters showcased in the Spelling Bee game.
2) Next, specify which among these letters is the center one.
3) The solver will then:
    - Display valid words crafted using the provided letters.
    - Assign a score to each word based on the game's rules.
    - Offer a cumulative score detailing the total points achievable with the given letters.
