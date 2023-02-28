import os
from fastapi import Header, HTTPException


async def get_token_headers(x_neon_token: str = Header(),
                            client_id: str = Header()):
    '''
    Enforces the X-SECRET-TOKEN and CLIENT-ID in headers for incoming requests
    '''
    print("RECEIVED: ", x_neon_token, client_id)
    bad_custom_auth = x_neon_token != '' or client_id != ''
    bad_custom_auth = x_neon_token != os.getenv(
        'X-SECRET-TOKEN') or client_id != os.getenv('CLIENT-ID')
    if bad_custom_auth:
        raise HTTPException(
            status_code=400, detail="Headers are invalid or unauthenticated.")
