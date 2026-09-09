"""Synthetic GT fixture consumer (different layer/dir from the def module).

This module imports and uses the exception via NON-CALL references only:
- an `import` of the symbol
- an `except <Class>:` handler
- a `raise <Class>(...)` statement

It intentionally references the OLD name `GtSyntheticError`, which the
def module no longer provides (it was renamed to GtSyntheticErrorRenamed).
"""

from lnbits.core._gt_errors import GtSyntheticError


def _gt_do_work(should_fail: bool) -> str:
    if should_fail:
        raise GtSyntheticError("synthetic failure")
    return "ok"


def gt_handle(should_fail: bool) -> str:
    try:
        return _gt_do_work(should_fail)
    except GtSyntheticError as exc:
        return f"handled: {exc}"
