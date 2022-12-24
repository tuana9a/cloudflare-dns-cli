class DnsRecord():
    id: str
    name: str
    type: str
    content: str
    ttl: int
    proxied: bool = False

    def __init__(self,
                 id: str,
                 name: str,
                 type: str,
                 content: str,
                 ttl: int,
                 proxied: bool = False,
                 **kwargs):
        self.id = id
        self.name = name
        self.type = type
        self.content = content
        self.proxied = proxied
        self.ttl = ttl

    def __str__(self):
        return " ".join([
            self.id, self.type, self.name, self.content,
            f"proxied={str(self.proxied)}", f"ttl={str(self.ttl)}"
        ])
