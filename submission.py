# Student Submission v5

def hello(name: str) -> str:
    """Return a greeting string."""
    if not name:
        raise ValueError("name cannot be empty")
    return f"Hello, {name}\!"

if __name__ == "__main__":
    print(hello("World"))
