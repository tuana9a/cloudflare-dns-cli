class CredentialParams():

    def __init__(self, base_url: str, email: str, access_token: str,
                 zone_id: str):
        self.base_url = base_url
        self.email = email
        self.access_token = access_token
        self.zone_id = zone_id

    def __str__(self):
        d = vars(self)
        return " ".join(map(lambda x: f"{x}={d[x]}", d.keys()))
