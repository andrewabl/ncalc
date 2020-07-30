import sys, ipaddress
from convert import Convert
from network_v4 import Network_v4
from network_v6 import Network_v6
from segmentation_v4 import Segmentation_v4
from segmentation_v6 import Segmentation_v6
from log import add_log


def flags(args):

    flags_dict = {'h':0, 'n': 1, '6': 0, 's': 0, 'b': False, 'c': 0, 'a': False}

    count = 1
    while len(args) > count:

        try:

            if args[count] == '-h' or args[count] == '--help':
                print(manual)
                sys.exit()

            elif args[count] == '-n' or args[count] == '--network' or sys.argv[count] == '-ipv4':
                flags_dict['n'] = 1
                del args[count]
                ccount -= 1

            elif args[count] == '-6' or args[count] == '-ipv6':
                flags_dict['6'] = 1
                flags_dict['n'] = 0
                del args[count]
                count -= 1
            
            elif args[count] == '-c' or args[count] == '--convert':
                flags_dict['c'] = 1
                flags_dict['n'] = 0
                del args[count]
                count -= 1
        
            elif args[count] == '-s' or args[count] == '--segm':
                flags_dict['s'] = args[count + 1]
                flags_dict['n'] = 0
                del args[count:count + 2]
                count -= 1
            
            elif args[count] == '-b':
                flags_dict['b'] = True
                del args[count]
                count -= 1

            elif args[count] == '-a':
                flags_dict['a'] = True
                del args[count]
                count -= 1

            count += 1

            if len(args) == 1:
                raise Exception("E: Uncorrect syntax. Try '--help' for clarification.\a")

        except IndexError:
            print("E: Uncorrect syntax. Try '--help' for clarification.\a")
            sys.exit()
        except Exception as exp:
            print(str(exp))
    return flags_dict

manual =  '''
Usage:
    ncalc -[OPTION] [ADDRESS or NUM]
        Options:\t
            -n      <--network> <--ipv4>    print IPv4 network information
            -6      <--ipv6>                print IPv6 network information
            -b      <--binary>              adding binary representation
            -s      <--segm>                network greedy segmentation
            -vslm                           segmentation(only IPv4)
            -eui                            EUI_64 process(only IPv6)
            -c      <--convert>             convert(hex, bin, dec)
            -h      <--help>                this manual\n'''

if len(sys.argv) == 1:
    print(manual)

dict_flag = flags(sys.argv)

for param in sys.argv[1:]:

    try:
        
        if dict_flag['n'] != 0:
            network = Network_v4(address=param)
            network.view(binary_flag=dict_flag['b'])

        if dict_flag['6'] != 0: 

            if not dict_flag['s']:
                network = Network_v6(address=param)
                network.view(binary_flag=dict_flag['b'])

        if dict_flag['c'] != 0:

            conv = Convert(value=param)
            conv.output()

        if dict_flag['s']:

            if dict_flag['6']:
                segm = Segmentation_v6(address=param, count=dict_flag['s'], add_info=dict_flag['a'], binary_flag=dict_flag['b'])
                segm.output()
            else:
                segm = Segmentation_v4(address=param, count=dict_flag['s'], add_info=dict_flag['a'], binary_flag=dict_flag['b'])
                segm.output()

    # except ipaddress.AddressValueError as exp:
    #     print("\tE: \a", str(exp))
    #     add_log(str(exp))

    # except ipaddress.NetmaskValueError as exp:
    #     print("\tE: \a", str(exp))
    #     add_log(str(exp))

    # except Exception as exp:
    #     print("\tE: \a", str(exp))
    #     add_log(str(exp))    
    except KeyError:
        pass