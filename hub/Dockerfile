FROM jupyterhub/jupyterhub:latest

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install dockerspawner mysqlclient jupyterhub-dummyauthenticator


