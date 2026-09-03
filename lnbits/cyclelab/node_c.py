# Test fixture: NEW file absorbed into the existing node_a<->node_b cycle.
# node_c -> node_a, and node_b -> node_c (added below), so the SCC grows from
# {a,b} to {a,b,c} but the SCC COUNT stays 1 (base 1 -> head 1, delta 0). The
# pre-fix DS missed this (SCC-count based); the fix derives introduced_cycle
# from new_cycle_members, which now includes node_c (bench 4c799f4).
from lnbits.cyclelab import node_a


def c_val() -> str:
    return "c" + node_a.a_val()
