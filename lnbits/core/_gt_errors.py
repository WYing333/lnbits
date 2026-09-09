"""Synthetic GT fixture module.

Defines a custom exception class used to exercise the File-Completeness
Tier-1 non-call blind spot. In this PR the class is RENAMED here
(GtSyntheticError -> GtSyntheticErrorRenamed) while the consumer module
still imports/except/raise the OLD name. This is a non-call reference gap.
"""


class GtSyntheticErrorRenamed(Exception):
    """Renamed synthetic exception. Consumers still reference the old name."""

    pass
