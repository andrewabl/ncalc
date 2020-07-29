import ipaddress, logging

logging.basicConfig(level= logging.DEBUG, format = ' %(message)s')

class Network_v6:

    def __init__(self, address):
        
        self.info_dict = {}
        network = ipaddress.IPv6Network(address, strict = False)
        self.info_dict['Network']  = network.exploded
        self.info_dict["NetMask"] = network.netmask.exploded
        self.info_dict["HostMask"] = network.hostmask.exploded

        if str(address).find('/') == -1:
            logging.debug("\a\nWARNING - Network address should be with prefix. Ex: '/64'", )

        elif network.prefixlen != 128:
            self.info_dict["FirstAdd"], self.info_dict["LastAdd"], self.info_dict["WideAdd"] = network[1].exploded, network[-2].exploded, network[-1].exploded

    def view(self, binary_flag = False):
        
        position_var = 100 if binary_flag else 70
        print('\n' + 'IPv6-Network'.center(position_var, '-'))
        for key in self.info_dict.keys():
            print('\t', key, str(self.info_dict[key]).rjust(54 - len(key)), end = '\t')

            if binary_flag is True:
                bits = self.to_bits(self.info_dict[key])
                print()
                
                for count in range(0, 8):
                    if count == 0 or count == 4:
                        print('\t\t\t', end = '')
                        
                    print(bits[count], end = '')

                    if count != 3 and count != 7:
                        print('_', end = '')
                    else:
                        print()
                print()
            else:
                print()
        print('----------'.center(position_var, '-'))
    
    def to_bits(self, address):
        bits = []
        for hextet in str(address).split('/')[0].split(':'):
            bits.append(bin(int(hextet, base=16)).replace("0b",'').rjust(16, '0'))
        return bits