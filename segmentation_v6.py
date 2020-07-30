import ipaddress, math
from network_v6 import Network_v6

class Segmentation_v6(Network_v6):

    def __init__(self, address, count, add_info=False, binary_flag=False):

        super().__init__(address)
        self.view(binary_flag=binary_flag, title="Base-IPv6-Network")
        self.count = int(count)
        self.binary_flag = binary_flag
        self.add_info = add_info

    def output(self):

        count = 1
        for subnet_address in self.segmentation():
            subnetwork = Network_v6(address=subnet_address)
            if self.add_info:
                subnetwork.view(binary_flag=self.binary_flag, title="IPv6-Subnet-#" + str(count))
            else:
                subnetwork.view_slave(key="Subnet#" + str(count), value=subnet_address, binary_flag=self.binary_flag)
            count += 1

    # ERROR
    def segmentation(self):

        prefixlen_diff = math.ceil(math.sqrt(self.count))

        if prefixlen_diff >= 128:
            raise ipaddress.NetmaskValueError

        return_list = []
        count = 0

        for subnet_address in self.network.subnets(prefixlen_diff=prefixlen_diff):
            count += 1
            if count > self.count:
                break
            return_list.append(subnet_address.exploded)

        return return_list