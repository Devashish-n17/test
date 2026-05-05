# retryx

A lightweight retry decorator for Python.

## Install

```bash
pip install git+https://github.com/YOUR_USERNAME/retryx.git
```

## Usage

```python
from retryx import retry

@retry(attempts=3, delay=1.0)
def my_function():
    ...
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `attempts` | int | 3 | Number of attempts before failing |
| `delay` | float | 1.0 | Seconds between retries |
| `exceptions` | tuple | (Exception,) | Exception types to catch |
