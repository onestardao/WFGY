# bbcr.py
# Collapse-Rebirth (BBCR) — stability enforcement
# Author: PSBigBig & Contributors
# License: MIT

from __future__ import annotations
import logging
from typing import Callable, Dict

import numpy as np

logger = logging.getLogger(__name__)


def compute_lyapunov(trajectory: np.ndarray) -> float:
    """
    Approximate Lyapunov exponent from a sequence of scalar errors.

    Parameters
    ----------
    trajectory : np.ndarray
        Sequence of error magnitudes over iterations.

    Returns
    -------
    float
        Estimated Lyapunov exponent λ (>0 indicates divergence).
    """
    if trajectory.size < 2:
        return 0.0
    diffs = np.diff(np.log(np.clip(trajectory, 1e-12, None)))
    return float(diffs.mean())


def check_collapse(
    residue_norm: float,
    f_S: float,
    *,
    Bc: float = 1.0,
    eps: float = 0.05
) -> bool:
    """
    Determine whether to trigger collapse-rebirth.

    Collapse if either:
      (i) residue_norm ≥ Bc, OR
      (ii) f_S ≤ eps

    Returns
    -------
    bool
        True if collapse condition is met.
    """
    collapse = (residue_norm >= Bc) or (f_S <= eps)
    logger.debug(
        "BBCR - Check collapse | ‖B‖=%.6f (≥%.2f?) | f_S=%.6f (≤%.2f?) → %s",
        residue_norm, Bc, f_S, eps, collapse
    )
    return collapse


def collapse_rebirth(
    state_reset_fn: Callable[[], Dict[str, float | np.ndarray]],
    *,
    max_retries: int = 3
) -> Dict[str, float | np.ndarray]:
    """
    Execute collapse-rebirth loop until stability is reached
    or maximum retries exhausted.

    Parameters
    ----------
    state_reset_fn : Callable
        A zero-arg function that recomputes the full state
        (residue, f_S, etc.) after rebirth.
    max_retries : int, optional
        Maximum number of collapse cycles.

    Returns
    -------
    dict
        Final stable state dictionary.
    """
    for attempt in range(max_retries):
        state = state_reset_fn()
        if not state.get("_collapse", False):
            logger.debug("BBCR - Stable after %d collapse(s)", attempt)
            return state
        logger.debug("BBCR - Collapse %d → retry", attempt + 1)

    logger.warning(
        "BBCR - Max retries reached; returning last unstable state"
    )
    return state

def run_demo() -> None:
    """Quick smoke-test for BBCR collapse logic."""
    traj = np.array([0.3, 0.21, 0.15, 0.14])
    lam = compute_lyapunov(traj)
    collapse = check_collapse(residue_norm=1.2, f_S=0.8, Bc=1.0, eps=0.05)
    print(f"BBCR demo λ ≈ {lam:.3f} | collapse? {collapse}")


if __name__ == "__main__":
    run_demo()
