"""
WFGY SDK – public facade
Exports:

• get_engine() – singleton factory
• enable()    – tiny helper used by the CI test
"""

from .wfgy_engine import get_engine, WFGYEngine     # re-export
from typing import Any, Dict

__all__ = ["get_engine", "enable", "WFGYEngine"]


def enable(model: Any, *, reload: bool = False, **_) -> Any:
    """
    Minimal helper for `tests/test_sdk_full.py`.

    If *model* is a dict that contains the three keys
    { "I", "G", "attention_logits" }, its logits are routed
    through WFGY and the dict is returned (in-place).  
    Otherwise the object is returned untouched.
    """
    if (
        isinstance(model, dict)
        and {"I", "G", "attention_logits"} <= model.keys()
    ):
        eng = get_engine(reload=reload)
        model["attention_logits"] = eng.run(
            model["I"], model["G"], model["attention_logits"]
        )
    return model

