---

## Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Tech Stack](#tech-stack)
* [Tests](#tests)
* [Contributing](#contributing)
* [License](#license)
* [Credits](#credits)

---

## Features

Key functionalities of the project:

* Multiplayer word scoring system
* Scrabble-style letter point mapping
* Case-insensitive word handling
* Real-time score updates after each word
* Supports unlimited words per player
* STOP command to end a player’s turn
* Automatic winner detection at the end
* Handles unknown characters safely (0 points)

---

## Installation

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/word-score-cli.git
cd word-score-cli
```

### 2. Ensure Python is installed

Python 3.7+ is recommended.

```bash
python --version
```

### 3. Run the program

```bash
python main.py
```

No external libraries are required.

---

## Usage

After running the script:

### 1. Enter number of players

```text
Enter the number of players: 2
```

### 2. Enter player names

```text
Enter name of the player 1: Alice
Enter name of the player 2: Bob
```

### 3. Players enter words

```text
Enter Word: hello
'hello' score 8 points!
Alice's total = 8
```

Type:

```text
STOP
```

to end a player's turn.

### 4. End of game

The program prints final scores and declares the winner.

---

## Tech Stack

Technologies used in this project:

* Python 3
* Standard library only
* Dictionary-based scoring logic
* CLI input/output workflow

---

## Tests

No automated tests are included yet.

You can manually test by running:

```bash
python main.py
```

Then verify:

* Words score correctly
* Totals accumulate properly
* STOP ends a player’s turn
* Winner detection works
* Multiple players function correctly

---

## Contributing

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

For larger gameplay improvements, please open an issue first to discuss the proposal.

---

## License

MIT License

Copyright (c) 2026 SiddharthShah30

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Credits

* Built using Python standard libraries
* Letter scoring inspired by Scrabble rules
* Developed by SiddharthShah30

---
