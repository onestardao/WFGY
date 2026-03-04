# bbam.py
# Attention Modulation (BBAM) — variance gating
# Author: PSBigBig & Contributors
# License: MIT

from __future__ import annotations
import logging
import numpy as np
from typing import Tuple

logger = logging.getLogger(__name__)


def modulate_attention(
    logits: np.ndarray,
    *,
    gamma: float = 0.5,
    window_size: int | None = None
) -> np.ndarray:
    """
    Apply variance-based gating to logits.

    Parameters
    ----------
    logits : np.ndarray
        Raw logits (any shape).
    gamma : float, optional
        Modulation strength (0 → no effect).
    window_size : int or None, optional
        If provided, compute local std with the given sliding window
        (1D only). Otherwise, use global std of the tensor.

    Returns
    -------
    np.ndarray
        Modulated logits (same shape as input).
    """
    if window_size is None:
        sigma = float(np.std(logits))
        factor = np.exp(-gamma * sigma)
        logger.debug("BBAM - global σ = %.6f | factor = %.6f", sigma, factor)
        return logits * factor

    # Local (1-D) variant
    if logits.ndim != 1:
        raise ValueError("window_size is supported only for 1-D logits")

    pad = window_size // 2
    padded = np.pad(logits, (pad, pad), mode="reflect")
    modulated = np.empty_like(logits)

    for i in range(logits.size):
        window = padded[i : i + window_size]
        sigma = float(np.std(window))
        modulated[i] = logits[i] * np.exp(-gamma * sigma)

    logger.debug(
        "BBAM - local window=%d applied to %d logits", window_size, logits.size
    )
    return modulated

def run_demo() -> None:
    """Quick smoke-test for BBAM."""
    import numpy as np

    logits = np.random.randn(20)
    mod = modulate_attention(logits, gamma=0.6)
    print(f"BBAM demo | first 3 logits before/after: {logits[:3]} -> {mod[:3]}")


if __name__ == "__main__":
    run_demo()
