import socket
import sys
import time


class IT85xxPlus:

    def __init__(self):
        self.it85_ip = ''
        self.it85_port = 8085
        self.it85_socket = socket.socket()
        self.it85_info_dict = {}
        self.it85_mes_dict = {}

    def it85_connect(self):
        try:
            self.it85_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print('Failed to create socket.')
            return

        try:
            self.it85_socket.connect((self.it85_ip, self.it85_port))
        except socket.error:
            print('failed to connect to ip ' + self.it85_ip)
            return

        self.it85_setup('SYST:REM')
        self.it85_setup('SYST:BEEP:IMM')

    def it85_setup(self, cmd):
        try:
            self.it85_socket.sendall('{}\n'.format(cmd).encode())
            time.sleep(0.1)
        except socket.error:
            print('Send failed')
            sys.exit()

    def it85_query(self, cmd):
        try:
            self.it85_socket.sendall('{}\n'.format(cmd).encode())
            time.sleep(0.1)
        except socket.error:
            print('Send failed')
            sys.exit()
        while True:
            reply = self.it85_socket.recv(4096)
            if reply:
                return reply.strip().decode()

    def it85_equipment_info(self):
        return self.it85_query('*IDN?')

    def it85_close(self):
        self.it85_setup('SYST:LOC')
        self.it85_socket.close()

    def it85_cc_setup(self, max_curr, max_power, use_4wire=False, volt_auto=True, max_volt=30):
        self.it85_setup('SOUR:FUNC CURR')
        self.it85_setup('SOUR:FUNC:MODE FIX')

        self.it85_setup('SYST:SENS {}'.format(int(use_4wire)))

        self.it85_setup('SOUR:CURR:RANG {}'.format(max_curr))

        self.it85_setup('SOUR:POW:PROT {}'.format(max_power))
        self.it85_setup('SOUR:POW:CONF {}'.format(max_power))

        self.it85_setup('SOUR:VOLT:RANG:AUTO {}'.format(int(volt_auto)))
        if not volt_auto:
            self.it85_setup('SOUR:VOLT:RANG {}'.format(max_volt))

    def it85_get_settings(self):
        self.it85_info_dict = {
            'EEPROM': bool(int(self.it85_query('*TST?'))),
            'System Version': float(self.it85_query('SYST:VERS?')),
            'Four-Wire Sensing': bool(int(self.it85_query('SYST:SENS?'))),
            'System Channel #': int(self.it85_query('SYST:CHAN:NUMB?')),
            'System Link Mode': self.it85_query('LINK:MODE?'),
            'System Current Channel #': int(self.it85_query('CHAN?')),

            'Prog Load Mode Setup': self.it85_query('SOUR:FUNC?').lower(),
            'Prog Load Mode Setting': self.it85_query('SOUR:FUNC:MODE?').lower(),
            'Prog Load CC Mode Curr setting': float(self.it85_query('SOUR:CURR:LEV?')),

            'Prog Load Voltage Range': float(self.it85_query('SOUR:VOLT:RANG?')),
            'Prog Load Voltage Range Auto': bool(int(self.it85_query('SOUR:VOLT:RANG:AUTO?'))),
            'Prog Load Current Range': float(self.it85_query('SOUR:CURR:RANG?')),
            'Prog Load Current Slew Rise': float(self.it85_query('SOUR:CURR:SLEW:RISE?')),
            'Prog Load Current Slew Fail': float(self.it85_query('SOUR:CURR:SLEW:FALL?')),
            'Prog Load Power Protection': float(self.it85_query('SOUR:POW:PROT?')),
            'Prog Load Power Maximum': float(self.it85_query('SOUR:POW:CONF?')),
        }

    def it85_get_measure(self):
        self.it85_mes_dict = {
            'Volt Avg': float(self.it85_query('MEAS:VOLT?')),
            'Volt Max': float(self.it85_query('MEAS:VOLT:MAX?')),
            'Volt Min': float(self.it85_query('MEAS:VOLT:MIN?')),
            'Curr Avg': float(self.it85_query('MEAS:CURR?')),
            'Curr Max': float(self.it85_query('MEAS:CURR:MAX?')),
            'Curr Min': float(self.it85_query('MEAS:CURR:MIN?')),
            'Volt PTP': float(self.it85_query('MEAS:VOLT:RIPP?')),
            'Curr PTP': float(self.it85_query('MEAS:VOLT:RIPP?')),
        }
