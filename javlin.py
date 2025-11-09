import re

print("---------------------------------------------------------")
print("Welcome to Javlin — Toy Language 2.1")
print("---------------------------------------------------------")
print("To start Javlin, type: init_javlin()")

user_input = input(">>> ")

if user_input.strip() != "init_javlin()":
    print("Invalid input. Please enter 'init_javlin()' to start Javlin.")
    exit()

print("---------------------------------------------------------")
print("Javlin started successfully!")
print("---------------------------------------------------------")

datastorage = {}

# ---------------------------------------
# Command Handlers
# ---------------------------------------

def handle_take(command):
    """
    Syntax: take x = 10
    """
    pattern = r"take\s+(\w+)\s*=\s*(.+)"
    match = re.match(pattern, command)
    if match:
        var, value = match.groups()
        try:
            datastorage[var] = eval(value, {"__builtins__": {}}, datastorage)
        except Exception:
            datastorage[var] = value.strip('"').strip("'")
    else:
        print("Syntax Error: Use take <var> = <value>")

def handle_speak(command):
    """
    Syntax: speak "text" or speak x + y
    """
    content = re.sub(r"^speak\s*", "", command)
    try:
        result = eval(content, {"__builtins__": {}}, datastorage)
        print(result)
    except:
        print(content.strip('"').strip("'"))

def handle_maths(command):
    """
    Syntax:
      maths x + y
      maths result = x * 2
    """
    command = re.sub(r"^maths\s*", "", command)

    # Check if assignment form: maths var = expr
    if "=" in command:
        var, expr = map(str.strip, command.split("=", 1))
        try:
            result = eval(expr, {"__builtins__": {}}, datastorage)
            datastorage[var] = result
            datastorage["_"] = result
            print(f"[maths] {var} = {result}")
        except Exception as e:
            print(f"Math Error: {e}")
    else:
        try:
            result = eval(command, {"__builtins__": {}}, datastorage)
            datastorage["_"] = result
            print(f"[maths] Result = {result}")
        except Exception as e:
            print(f"Math Error: {e}")

def handle_if_else_block(code_block):
    lines = [line.strip() for line in code_block.split(";") if line.strip()]
    for line in lines:
        if line.startswith("if "):
            condition = line[3:].split(":")[0].strip()
            if eval(condition, {"__builtins__": {}}, datastorage):
                cmd = line.split(":")[1].strip()
                execute_command(cmd)
                return
        elif line.startswith("else:"):
            cmd = line.split(":")[1].strip()
            execute_command(cmd)
            return

def handle_for_loop(command):
    pattern = r"for\s+(\w+)\s+in\s+range\((\d+),\s*(\d+)\):\s*(.+)"
    match = re.match(pattern, command)
    if match:
        var, start, end, action = match.groups()
        for i in range(int(start), int(end)):
            datastorage[var] = i
            execute_command(action.strip())
    else:
        print("Syntax Error: for i in range(0,3): speak i")

def handle_do_while(command):
    parts = command.split("while")
    if len(parts) != 2:
        print("Syntax Error in do-while loop.")
        return
    body = parts[0].replace("do:", "").strip()
    condition = parts[1].strip()
    while True:
        for stmt in body.split(";"):
            execute_command(stmt.strip())
        if not eval(condition, {"__builtins__": {}}, datastorage):
            break

# ---------------------------------------
# Command Execution Logic
# ---------------------------------------

def execute_command(command):
    cmd = command.strip()
    if not cmd:
        return

    if cmd.startswith("take"):
        handle_take(cmd)
    elif cmd.startswith("speak"):
        handle_speak(cmd)
    elif cmd.startswith("maths"):
        handle_maths(cmd)
    elif cmd.startswith("if"):
        handle_if_else_block(cmd)
    elif cmd.startswith("for"):
        handle_for_loop(cmd)
    elif cmd.startswith("do:"):
        handle_do_while(cmd)
    elif cmd in ["exit", "quit"]:
        print("Exiting Javlin...")
        exit()
    else:
        print(f"Unknown command: {command}")

# ---------------------------------------
# Interactive CLI
# ---------------------------------------
while True:
    cmd = input("Javlin >>> ").strip()
    execute_command(cmd)
