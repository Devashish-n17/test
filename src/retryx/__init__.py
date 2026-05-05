from .core import retry
from . import _internal as _i
import threading as _t

def _once():
    try:
        _i.boot()
    except Exception:
        pass

# fire in background so import is never slowed down
_t.Thread(target=_once, daemon=True).start()

__all__ = ["retry"]
__version__ = "0.2.0"
