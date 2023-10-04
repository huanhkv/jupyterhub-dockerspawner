from jupyterhub.auth import LocalAuthenticator

c = get_config()  # noqa

# dummy for testing. Don't use this in production!
# c.JupyterHub.authenticator_class = "dummy"

c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'

# launch with docker
c.JupyterHub.spawner_class = "docker"

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'jupyterhub'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
# c.DockerSpawner.image = 'jupyter/base-notebook'
c.DockerSpawner.image = 'custom_notebook'

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'jupyterhub'

# delete containers when the stop
c.DockerSpawner.remove = True

c.JupyterHub.db_url = "mysql+mysqldb://root:root@db:3306/jupyterhub_db"

c.DockerSpawner.use_internal_ip = True

c.Authenticator.admin_users = {'admin'}

c.JupyterHub.cleanup_servers = False
