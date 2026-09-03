# Test fixture: a service-layer module that reads from the data layer (crud).
# service -> data is an ALLOWED forward crossing (service allows -> data). BC
# should stay clean; the pre-fix bug flagged ANY new cross-layer pair with
# policy_compliance=0.0 regardless of the allow-list (bench adebc54 fixes this).
from lnbits.core.crud.wallets import get_wallet


async def probe_service_reads_wallet(wallet_id: str):
    return await get_wallet(wallet_id)
