Python Crash Course
===================

Init Python

```bash
uv init 
```

Add a package
```bash
uv add pygame
```

Add a "dev" package
```bash
uv add mypy --dev
```

Run script
```bash
uv run xcom
```

Run mypy
```bash
uv run mypy src/
```

Run ruff
```bash
uv run ruff check
uv run ruff check --fix
uv run ruff format
```