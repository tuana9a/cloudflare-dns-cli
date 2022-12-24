import os

base_url = "https://api.cloudflare.com/client/v4"
email = os.getenv("CLOUDFLARE_EMAIL") or ""
access_token = os.getenv("CLOUDFLARE_ACCESS_TOKEN") or ""
zone_id = os.getenv("CLOUDFLARE_ZONE_ID") or ""
