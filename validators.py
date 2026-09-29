"""Input helpers. Every prompt in the program goes through one of these,
so bad input never reaches the rest of the code."""


def ask_choice(prompt, valid):
    while True:
        c = input(prompt).strip()
        if c in valid:
            return c
        print("Invalid choice. Options:", ", ".join(valid))


def ask_text(prompt):
    while True:
        t = input(prompt).strip()
        if t:
            return t
        print("This field cannot be empty.")


def ask_float(prompt, minimum=None, maximum=None):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"Value must be at most {maximum}.")
            continue
        return value


def ask_int(prompt, minimum=None, maximum=None):
    return int(ask_float(prompt, minimum, maximum))
