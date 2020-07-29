import re, sys

class Convert:

    bin_regex = r'(0b)?[0-1]+'
    dec_regex = r'(0d)?[0-9]+'
    hex_regex = r'(0x)?[0-9, a-f, A-F]+'

    def __init__(self, value):

        self.value = self.setvalue(value)
    
    def setvalue(self, value):

        if re.search(self.bin_regex, str(value)) is not None:
            if re.search(self.bin_regex, str(value)).group() == value:
                return int(value, base=2)
        elif re.search(self.dec_regex, str(value)) is not None:
            if re.search(self.dec_regex, str(value)).group() == value:
                return int(value, base=10)
        elif re.search(self.hex_regex, str(value)) is not None:
            if re.search(self.hex_regex, str(value)).group() == value:
                return int(value, base=16)
        raise Exception("Uncorrect syntax")
        
    def output(self):

        print("\tBin: ", bin(self.value),
              "\n\tDec: ", str(self.value),
              "\n\tHex: ", hex(self.value))