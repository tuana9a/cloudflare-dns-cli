import setuptools

setuptools.setup(name="cloudflare-dns-cli",
                 packages=setuptools.find_packages(exclude=["test"]),
                 version="1.0.0",
                 author="Tuan Nguyen Minh",
                 author_email="tuana9a@gmail.com",
                 entry_points={
                     "console_scripts": [
                         "cloudflare-dns-cli=cloudflarednscli.cmd.index:main",
                     ]
                 },
                 install_requires=["requests>=2.28.0"])
