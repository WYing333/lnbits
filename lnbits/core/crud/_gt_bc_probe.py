# Synthetic ground-truth probe for Boundary-Coverage (BC) testing.
# This file lives in the data/service layer (lnbits/core/crud) and deliberately
# makes a FORBIDDEN call into the API layer (lnbits/core/views), creating a
# data->api backward crossing. It is contrived and never invoked in production.
from lnbits.core.views.auth_api import _auth_redirect_response


def _gt_probe():
    # Forbidden data-layer -> api-layer CALL crossing.
    return _auth_redirect_response("/", "gt_user", "gt@example.com")
