from cloudflare.api.v4.configs.cfg import default_credentials

default_headers = {
    "X-Auth-Email": default_credentials.email,
    "Authorization": f"Bearer {default_credentials.access_token}",
    "Content-Type": "application/json"
}
