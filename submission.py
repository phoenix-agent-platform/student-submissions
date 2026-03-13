# Student Submission v6

def hello(name: str) -> str:
    if not name:
        raise ValueError("name cannot be empty")
    return f"Hello, {name}\!"

def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print(hello("World"))
    print(add(1, 2))
