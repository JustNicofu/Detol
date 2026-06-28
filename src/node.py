class node:
    def __init__(self) -> None:
        self.command: str = ""
        self.arguments: dict = {
            
        }

    def __repr__(self) -> str:
        return f"[node] command: {self.command}, options: {self.arguments}"
