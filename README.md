# textbased_game
This is an old textbased project which I programmed for an university course of mine.

## Semester Evaluation Game – Python Script

This Python script implements a **text-based game** in which the player must grade students to achieve a target evaluation score.
The game features multiple states and actions that influence the storyline and determine the player’s success.

---

### Requirements

The file **`Uebergänge.py`** is the main entry point of the game.
Before running the script, make sure you have **Python** installed on your system.
You’ll also need access to the following modules and files:

* **`FunktionClass.py`** – Contains the `Report` class and the `spieler1` instance used throughout the game.
* **`Einmalig.py`** – Includes helper functions that handle one-time actions during gameplay.
* **`Feedback1.py`** – Handles the first feedback phase of the evaluation process.
* **`Feedback2.py`** – Handles the second feedback phase of the evaluation process.
* **`Storyline_Programmierprojekt.txt`** – Contains the game’s storyline and dialogue.

You’ll also need the **Natural Language Toolkit (NLTK)**.
Install it using:

```bash
pip install nltk
```

Then run the following commands in Python to download the required NLTK corpora:

```python
import nltk
nltk.download('names')
nltk.download('reuters')
```

---

### How to Play

Run the main script to start the game.
You’ll be asked for your name, and then the introduction from *Storyline_Programmierprojekt.txt* will be displayed.

The game progresses through several states, such as:

* **Start**
* **Evaluation 1**
* **Evaluation 2**
* **Free Time**
* **Snack**
* **Feedback 1**
* **Feedback 2**
* **Final Evaluation**
* **Defeat**

Your actions determine how the story unfolds and which state you move to next.

In **Evaluation 1** and **Evaluation 2**, you assign grades to students.
Keep an eye on your **Energy Points (EP)** — they affect your ability to continue grading.

During **Free Time** and **Snack**, you can rest and restore energy.

In **Feedback 1**, you’ll face your first puzzle: deducing three topics from randomly generated texts.
In **Feedback 2**, you must identify a valid “code set” based on specific rules.

At the **Evaluation** stage, your final score and outcome are determined based on your choices.
If you reach the **Defeat** state, you lose — but you can always try again.

---

### Controls

Choose different options by entering the corresponding command when prompted.
Available commands include:

```
grade (g)
inspect report (i)
exit (e)
delay grade (d)  # secret skip code
rest (r)
eat snack (s)
give feedback (f)
get eval (t)
play again (p)
```

Follow the in-game instructions carefully to achieve the best results.

---

### Module Overview

#### `Einmalig.py`

Contains functions that ensure certain actions can only be executed once during a playthrough.

#### `Feedback1.py`

Implements the `Feedback1` class, which manages the first evaluation phase.
Here, the player completes tasks and collects Evaluation Points (EV).

#### `Feedback2.py`

Contains the `feedback2` function, responsible for the second evaluation phase.
The player must input a valid “code set” to earn EV points.

#### `FunktionClass.py`

Defines the `Report` class, which tracks the player’s state throughout the game.
It includes methods for grading students, managing energy, and displaying the semester report.

**Usage example:**

```python
spieler1 = Report()
```

This creates the main instance of the `Report` class, which drives the entire game logic.

---

### Have Fun!

Enjoy the game and see how well you perform!
Your choices affect the storyline, energy, and final evaluation — leading to multiple possible endings.
Good luck and have fun experimenting!

---
