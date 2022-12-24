from typing import List


class ZoneRecord():
    id: str
    name: str
    status: str
    name_servers: List[str]

    def __init__(self, id: str, name: str, status: str,
                 name_servers: List[str], **kwargs):
        self.id = id
        self.name = name
        self.status = status
        self.name_servers = name_servers
        pass

    def __str__(self) -> str:
        return " ".join([
            self.id, self.name, f"name_servers={str(self.name_servers)}",
            self.status
        ])
