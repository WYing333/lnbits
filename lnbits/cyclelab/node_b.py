# Test fixture: base-branch 2-node cycle with node_a.
from lnbits.cyclelab import node_a


def b_val() -> str:
    return "b"


def b_uses_a() -> str:
    return node_a.a_val()
