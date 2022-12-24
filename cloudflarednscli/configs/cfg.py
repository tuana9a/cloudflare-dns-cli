import os
import dotenv

from cloudflarednscli.models.credentials import CredentialParams

dotenv.load_dotenv()

base_url = "https://api.cloudflare.com/client/v4"
email = str(os.getenv("CLOUDFLARE_EMAIL"))
access_token = str(os.getenv("CLOUDFLARE_ACCESS_TOKEN"))
zone_id = str(os.getenv("CLOUDFLARE_ZONE_ID"))
