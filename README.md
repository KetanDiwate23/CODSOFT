# 🐍 CodSoft Python Programming Internship

> **Intern:** Ketan Diwate  
> **College:** G.H. Raisoni College of Engineering, Nagpur  
> **Internship:** Python Programming @ [CodSoft](https://www.codsoft.in)  
> **GitHub:** [@KetanDiwate23](https://github.com/KetanDiwate23)  
> **LinkedIn:** [ketan-diwate](https://linkedin.com/in/ketan-diwate)

---

## 📋 Tasks Overview

| # | Task | Description | File |
|---|------|-------------|------|
| 1 | ✅ To-Do List | CLI app to manage and track tasks | `task1_todo.py` |
| 2 | ✅ Calculator | Basic arithmetic calculator | `task2_calculator.py` |
| 3 | ✅ Password Generator | Generate strong random passwords | `task3_password_gen.py` |
| 4 | ✅ Rock-Paper-Scissors | Game with score tracking | `task4_rps.py` |
| 5 | ✅ Contact Book | Full CRUD contact manager with search | `task5_contacts.py` |

---

## 🚀 How to Run

Make sure you have **Python 3.6+** installed.

```bash
# Clone the repo
git clone https://github.com/KetanDiwate23/CODSOFT.git
cd CODSOFT

# Run any task
python3 task1_todo.py
python3 task2_calculator.py
python3 task3_password_gen.py
python3 task4_rps.py
python3 task5_contacts.py
```

No external libraries needed — all tasks use Python's standard library only.

---

## 📁 Task Details

### Task 1 — To-Do List
A command-line to-do list app that lets you manage your daily tasks.

**Features:**
- Add new tasks
- View all tasks with completion status
- Mark tasks as done
- Edit existing tasks
- Delete tasks

```
=== To-Do List ===
1. View  2. Add  3. Done  4. Edit  5. Delete  6. Quit
Choose: 2
Task description: Buy groceries
Added: 'Buy groceries'
```

---

### Task 2 — Calculator
A simple yet complete calculator supporting multiple operations.

**Features:**
- Addition, Subtraction, Multiplication, Division
- Modulo (`%`) and Exponentiation (`**`)
- Clean output (no unnecessary `.0` decimals)
- Loop to calculate multiple times

```
=== Calculator ===
First number: 15
Operation: **
Second number: 2
  15 ** 2 = 225
```

---

### Task 3 — Password Generator
Generates strong, random passwords with customizable complexity.

**Features:**
- Choose password length (min 6)
- Toggle uppercase, digits, and symbols
- Generates 3 options at once to pick from
- Strength indicator (Weak / Fair / Good / Strong)

```
=== Password Generator ===
Password length (min 6): 16
Include uppercase? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

  W}y!1_{@F4SjKm2#  [Strong 💪]
  9.>tM?1x*zt6@R#q  [Strong 💪]
  ix1%3%;PF>><$mNw  [Strong 💪]
```

---

### Task 4 — Rock-Paper-Scissors
Classic game against the computer with round-by-round score tracking.

**Features:**
- Quick shortcut keys: `r`, `p`, `s`
- Computer picks randomly
- Win/loss/tie detection with emoji feedback
- Score tracked across all rounds
- Final match summary on quit

```
=== Rock Paper Scissors ===
Your move: r
  You:      🪨 Rock
  Computer: ✂️ Scissors
  → You win this round! 🎉

  Score — You: 1  Computer: 0  (Round 1)
```

---

### Task 5 — Contact Book
A persistent contact manager that saves data to a local JSON file.

**Features:**
- Add contacts with name, phone, email, address
- View full contact list
- Search by name or phone number
- Update any contact field
- Delete contacts
- Data saved to `contacts.json` (persists between runs)

```
=== Contact Book ===
1.View  2.Add  3.Details  4.Search  5.Update  6.Delete  7.Exit
Choose: 4
Search by name or phone: ketan
  → Ketan Diwate  |  9876543210  |  ketan@email.com
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** `random`, `string`, `json`, `os` (all standard library)
- **Paradigm:** Procedural, CLI-based

---

## 📜 About CodSoft

CodSoft is a vibrant community focused on leadership development, learning, and student engagement. This internship provided hands-on experience building real Python applications from scratch.

---

*Made with 🐍 by Ketan Diwate*
