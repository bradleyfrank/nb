# Python

Open and read a file contents

```python
with open(Path.home() / "file.example", "r", encoding="utf-8") as file:
    first_line = file.read().splitlines()[0]
```
