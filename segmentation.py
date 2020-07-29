import ipaddress
from network_v4 import Network_v4


class Segmentation(Network_v4):

    def __init__(self, address, binary_flag=False):
        Network_v4.__init__(self, address)
        Network_v4.view(self, binary_flag=binary_flag, title="Base-IPv4-Network")