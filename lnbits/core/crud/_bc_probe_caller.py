# data-layer (crud) module that reaches UP into the api layer (backward
# crossing data->api, NOT in data allow-list [domain, utils]) -> BC should flag.
from lnbits.core.views._bc_probe_target import bc_probe_target


def read_api_value() -> str:
    return bc_probe_target()
