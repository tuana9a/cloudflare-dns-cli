class CredentialParams():

    def __init__(self, base_url: str, email: str, access_token: str,
                 zone_id: str):
        self.base_url = base_url
        self.email = email
        self.access_token = access_token
        self.zone_id = zone_id

    def __str__(self):
        return " ".join([
            "base_url",
            "=",
            self.base_url,
            "email",
            "=",
            self.email,
            "zone_id",
            "=",
            self.zone_id,
            "access_token",
            "=",
            self.access_token,
        ])
