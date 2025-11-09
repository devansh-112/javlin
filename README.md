
# 🧠 Javlin — Toy Language 2.1

*A fun Python-based interpreted toy language inspired by Bhailang — built to make coding feel simple again.*

---

## 🚀 Introduction

Javlin is a **lightweight toy programming language** written in Python.
It’s not meant to compete with real languages — it’s a playground for creative logic, regex experiments, and interpreter design.

The idea came from one thought:

> “What if I could write code without fighting commas, semicolons, and curly braces?” 😤

So, Javlin was born — a tiny, no-syntax-drama language where logic matters more than punctuation.

You can use it as a **reference project** to learn how interpreters work or build your own toy language.

---

## ⚙️ Features

✅ Variable declarations using `take`
✅ Expression evaluation using `maths`
✅ Output printing with `speak`
✅ Conditionals (`if` / `else`)
✅ Loop support (`for` and `do-while`)
✅ Runtime variable storage using dictionaries
✅ Error-safe evaluation with restricted built-ins

---

## 💻 Getting Started

1. Clone or download the repository.
2. Run the script with Python 3:

   ```bash
   python javlin.py
   ```
3. Type:

   ```bash
   >>> init_javlin()
   ```
4. Start writing Javlin commands interactively.

---

## 🧩 Example Commands

```bash
---------------------------------------------------------
Welcome to Javlin — Toy Language 2.1
---------------------------------------------------------
To start Javlin, type: init_javlin()
>>> init_javlin()
---------------------------------------------------------
Javlin started successfully!
---------------------------------------------------------
```

### 🔹 Variables

```bash
Javlin >>> take x = 10
Javlin >>> speak x
10
```

### 🔹 Math

```bash
Javlin >>> maths x + 5
[maths] Result = 15
```

### 🔹 If / Else

```bash
Javlin >>> if x > 5: speak "x is big"; else: speak "x is small"
x is big
```

### 🔹 For Loop

```bash
Javlin >>> for i in range(0,3): speak i
0
1
2
```

### 🔹 Do While

```bash
Javlin >>> take i = 0
Javlin >>> do: speak i; maths i = i + 1 while i < 3
0
1
2
```

---

## 🧠 How It Works Internally

The interpreter follows a **modular pipeline** — similar to how real languages process code.

### **🧾 1. Input Phase**

You type a command like:

```bash
Javlin >>> maths x + 10
```

This gets passed into the main function `execute_command()`.

---

### **⚙️ 2. Command Recognition**

`execute_command()` identifies which operation you’re trying to run:

```python
if cmd.startswith("take"):
    handle_take(cmd)
elif cmd.startswith("speak"):
    handle_speak(cmd)
elif cmd.startswith("maths"):
    handle_maths(cmd)
```

Each handler (like `handle_take`, `handle_maths`, etc.) manages a specific keyword.

---

### **🧮 3. Parsing & Evaluation**

Handlers use **regex** (`re.match()`) to break down commands.
Example for `take x = 10`:

```python
pattern = r"take\s+(\w+)\s*=\s*(.+)"
```

This extracts:

* Variable name → `x`
* Value → `10`

The interpreter then evaluates the right-hand side safely using:

```python
eval(value, {"__builtins__": {}}, datastorage)
```

All values are stored in a dictionary called `datastorage`.

---

### **🔁 4. Runtime Memory**

All declared variables persist here:

```python
datastorage = {
  "x": 10,
  "y": 5,
  "_": 15   # last result
}
```

This means subsequent commands can reuse variables — just like a real REPL environment.

---

### **🧩 5. Execution Flow Diagram**

Here’s a visual overview of Javlin’s interpreter logic:

```
┌────────────────────────────────────────┐
│           User enters command          │
└────────────────────────────────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │ execute_command(cmd)    │
        └────────────────────────┘
                     │
   ┌─────────────────┼─────────────────┐
   ▼                 ▼                 ▼
handle_take()   handle_maths()    handle_speak()
   │                 │                 │
   ▼                 ▼                 ▼
Update / Eval   Perform Math     Print / Output
   │                 │                 │
   └─────────────────┴─────────────────┘
                     │
                     ▼
     ┌────────────────────────────┐
     │   Store result in memory   │
     │   datastorage[var] = val   │
     └────────────────────────────┘
```

---

## 🔮 Future Plans

* Add **functions** and user-defined commands
* Introduce **arrays** and simple data types
* Support **multi-line blocks**
* Add **importable modules** (time, random, etc.)
* Build a **web playground** using Flask

---

## 💡 Why I Built This

Because syntax shouldn’t be a war between the coder and the compiler.
Javlin is my reminder that **code can be expressive, readable, and fun** — even when it’s completely unnecessary.

> Sometimes, the best projects are the ones that don’t take themselves too seriously.

---

## 🏷️ Tags

`#Python` `#ToyLanguage` `#BhailangInspired` `#Interpreter` `#LearningByDoing` `#WeekendProject` `#OpenSource`

---

Would you like me to include a **“💬 Custom Syntax Reference”** section next — listing all commands (`take`, `speak`, `maths`, `for`, `do:`, etc.) with short syntax + example pairs, like an official language doc page?
It’ll make your README feel like *real developer documentation*.
