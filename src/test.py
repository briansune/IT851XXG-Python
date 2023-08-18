import it85xxg_series
from pprint import pprint

pld = it85xxg_series.IT85xxPlus()

pld.it85_ip = '192.168.1.212'

pld.it85_connect()
sys_info = pld.it85_equipment_info()
print(sys_info)

pld.it85_get_settings()
pprint(pld.it85_info_dict)

pld.it85_get_measure()
pprint(pld.it85_mes_dict)

pld.it85_cc_setup(5, 30, True, False, 10)

pld.it85_get_settings()
pprint(pld.it85_info_dict)

pld.it85_close()
