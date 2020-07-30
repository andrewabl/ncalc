import logging
from ipaddress import IPv4Network

logging.basicConfig(level= logging.DEBUG, format = ' %(message)s')

class Network_v4:

    def __init__(self, address):

        self.info_dict = {}
        network = self.network = self.info_dict["Network"] = IPv4Network(address=address, strict=False)
        self.info_dict["NetMask"] = network.netmask
        self.info_dict["HostMask"] = network.hostmask

        if str(address).find('/') == False:
            logging.debug("\a\nWARNING - Network address should be with prefix. Ex: '/24'\n", )

        elif network.prefixlen != 32:
            self.info_dict["FirstAdd"], self.info_dict["LastAdd"], self.info_dict["WideAdd"] = network[1], network[-2], network[-1]

    def view(self, binary_flag = False, title='IPv4-Network'):

        position_var = 80 if binary_flag == True else  40
        print(title.center(position_var, '-'))

        for key in self.info_dict.keys():
           self.view_slave(key=key, value=self.info_dict[key], binary_flag=binary_flag)
        temp_var = "-" * len(title)
        print(temp_var.center(position_var, '-'))

    def view_slave(self, key, value, binary_flag):

        print('\t', key, str(value).rjust(30 - len(key)), end = '\t')

        if binary_flag is True:
            print(self.to_bits(value))
        else:
            print()

    def to_bits(self, address):

        bits = []
        for octet in str(address).split('/')[0].split('.'):
            bits.append(bin(int(octet)).replace("0b",'').rjust(8, '0'))
        return "_".join(bits)
    
    # def prefix_to_mask(self, prefix):

    #     bits = ''
    #     for count in range(0, 32):
    #         if count < prefix:
    #             bits += '1'
    #         else:
    #             bits += '0'
    #     return bits
