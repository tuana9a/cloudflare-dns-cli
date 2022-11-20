import setuptools

setuptools.setup(
    name="cloudflare-dns-cli",
    packages=setuptools.find_packages(exclude=["test"]),
    version="1.0.0",
    author="Tuan Nguyen Minh",
    author_email="tuana9a@gmail.com",
    entry_points={
        "console_scripts": [
            "cloudflare-list-dns=cloudflare.api.v4.cmd.list_dns:list_dns_records",
            "cloudflare-list-dns-names=cloudflare.api.v4.cmd.list_dns_names:list_dns_names",
            "cloudflare-list-zones=cloudflare.api.v4.cmd.list_zones:list_zones",
            "cloudflare-delete-dns-by-id=cloudflare.api.v4.cmd.delete_dns_by_id:delete_dns_by_id",
            "cloudflare-update-dns=cloudflare.api.v4.cmd.update_dns:update_dns",
            "cloudflare-insert-dns=cloudflare.api.v4.cmd.insert_dns:insert_new_dns",
        ]
    },
    install_requires=["requests==2.28.0", "python-dotenv==0.19.2"])
