import os
import dotenv

from cloudflare.api.v4.configs.credentials import CredentialParams

dotenv.load_dotenv()

default_cloudflare_base_url = "https://api.cloudflare.com/client/v4"
default_cloudflare_email = str(os.getenv("CLOUDFLARE_EMAIL"))
default_cloudflare_access_token = str(os.getenv("CLOUDFLARE_ACCESS_TOKEN"))
default_cloudflare_zone_id = str(os.getenv("CLOUDFLARE_ZONE_ID"))

default_credentials = CredentialParams(
    base_url=default_cloudflare_base_url,
    email=default_cloudflare_email,
    zone_id=default_cloudflare_zone_id,
    access_token=default_cloudflare_access_token)