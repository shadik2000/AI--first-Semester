import os

def chunks(path: str, size: int, **kwargs):
    if not os.path.isfile(path):
        raise ValueError(f"Path {path} is not a file.")

    if size < 1:
        raise ValueError("Size must not be less than 1")

    with open(path, **kwargs) as file:
        while True:
            chunk = file.read(size)
            if not chunk:
                break
            yield chunk

for i, c in enumerate(chunks("ex2_example.txt", 25, mode="rb")):
    print(f"Chunk {i} = {c}")
