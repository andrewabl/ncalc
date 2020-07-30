import ipaddress, math
from network_v4 import Network_v4
from convert import Convert


class Segmentation(Network_v4):

    def __init__(self, address, count, binary_flag=False):

        super().__init__(address)
        self.view(binary_flag=binary_flag, title="Base-IPv4-Network")
        self.count = int(count)
        self.binary_flag = binary_flag

    def output(self):

        count = 1
        for subnet_address in self.segmentation():
            subnetwork = Network_v4(address=subnet_address)
            subnetwork.view(binary_flag=self.binary_flag, title="IPv4-Subnet-#" + str(count))
            count += 1

    def segmentation(self):

        prefixlen_diff = math.ceil(math.sqrt(self.count))

        if prefixlen_diff >= 32:
            raise ipaddress.NetmaskValueError

        return list(self.network.subnets(prefixlen_diff=prefixlen_diff))[:self.count]
