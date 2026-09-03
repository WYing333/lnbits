# Test fixture: base-branch 2-node cycle with node_b (SCC size 2 at base).
from lnbits.cyclelab import node_b


def a_val() -> str:
    return "a" + node_b.b_val()
