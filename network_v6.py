import ipaddress, logging

logging.basicConfig(level= logging.DEBUG, format = ' %(message)s')

class Network_v6:

    def __init__(self, address):
        
        self.info_dict = {}
        network = self.network = ipaddress.IPv6Network(address, strict = False)
        self.info_dict['Network']  = network.exploded
        self.info_dict["NetMask"] = network.netmask.exploded
        self.info_dict["HostMask"] = network.hostmask.exploded

        if str(address).find('/') == -1:
            logging.debug("\a\nWARNING - Network address should be with prefix. Ex: '/64'", )

        elif network.prefixlen != 128:
            self.info_dict["FirstAdd"], self.info_dict["LastAdd"], self.info_dict["WideAdd"] = network[1].exploded, network[-2].exploded, network[-1].exploded

    def view(self, title='IPv6-Network', binary_flag = False):
        
        position_var = 100 if binary_flag else 70
        print(title.center(position_var, '-'))

        for key in self.info_dict.keys():
            self.view_slave(key=key, value=self.info_dict[key], binary_flag=binary_flag)

        temp_var = "-" * len(title)
        print(temp_var.center(position_var, '-'))
    
    def view_slave(self, key, value, binary_flag):
        print('\t', key, str(value).rjust(54 - len(key)), end = '\n')

        if binary_flag is True:
            bits = self.to_bits(value)
                
            for count in range(0, 8):
                if count == 0 or count == 4:
                    print('\t\t\t', end = '')
                        
                print(bits[count], end = '')

                if count != 3 and count != 7:
                    print('_', end = '')
                else:
                    print()

    def to_bits(self, address):
        bits = []
        for hextet in str(address).split('/')[0].split(':'):
            bits.append(bin(int(hextet, base=16)).replace("0b",'').rjust(16, '0'))
        return bits