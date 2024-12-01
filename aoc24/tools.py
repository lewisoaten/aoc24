def read_to_string(file_path: str) -> str:
    with open(file_path) as file:
        return file.read().strip()
