import hashlib

import getmac


class Host:

    @property
    def identifier(self):
        salt = Host._cpu_serial() + Host._mac_address()
        return hashlib.md5(salt.encode()).hexdigest()

    @staticmethod
    def _cpu_serial():
        # Extract serial from cpuinfo file
        cpuserial = "0000000000000000"
        try:
            f = open('/proc/cpuinfo', 'r')
            for line in f:
                if line[0:6] == 'Serial':
                    cpuserial = line[10:26]
            f.close()
        except:
            cpuserial = "ERROR000000000"
        return cpuserial

    @staticmethod
    def _mac_address():
        return getmac.get_mac_address()
