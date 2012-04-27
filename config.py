import inspect
import os

class Config(object):
    def __init__(self):
        # Path to the git repo for openstack-test.
        self.data_path = os.path.dirname(inspect.getfile(inspect.currentframe()))

        # Hosts to run this test on.
        self.hosts = ['node10', 'node9']
        self.hosts_without_openstack = ['xdev']

        self.flavor_name = 'm1.tiny'
        self.image_name = 'uec-oneiric-server-vmsagent'
        self.key_name = 'openstack-test'
        self.key_path = os.path.join(self.data_path, 'openstack-test.key')
        self.guest_user = 'ubuntu'

    def id_to_hostname(self, id):
        for host in self.hosts:
            if hostname_to_id(host) == id:
                return host
        raise KeyError(id)

    def other_hosts(self, hostname=None, hostId=None):
        if hostname == None:
            hostname = id_to_hostname(hostId)
        return [host for host in self.hosts if host != hostname]

default_config = Config()
