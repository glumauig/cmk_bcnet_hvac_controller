import re
from .agent_based_api.v1 import *
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
   get_value_store,
)


def discover_hvac_controller_bldg_chw_high_temp(section):
    yield Service()

def check_hvac_controller_bldg_chw_high_temp(section):
    hvac_snmp_name = str(section[0][0])
    hvac_snmp_value = int(section[0][1])

    
    hvac_snmp_name=re.sub(r"\s+", "_", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"/+", "-", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"BCN-+", "", hvac_snmp_name)

    if hvac_snmp_value == 0:
        hvac_snmp_value_converted = "Normal"
        summary_hvac = "bldg_chw_high_temp: " + str(hvac_snmp_value_converted)
        yield Result(state=State.OK,summary=summary_hvac)

    else:
        hvac_snmp_value_converted = "High-Temp"
        summary_hvac = "bldg_chw_high_temp: " + str(hvac_snmp_value_converted)
        yield Result(state=State.CRIT,summary=summary_hvac)

    yield Metric(hvac_snmp_name,hvac_snmp_value)

    return


register.snmp_section(
    name = "hvac_controller_bldg_chw_high_temp",
    detect = exists(".1.3.6.1.4.1.15255.1.2.1.1.1.5.*"),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.15255.1.2.1.1.1',
        oids = [
                '5.2', #bldg_chw_high_temp
                '2.2', #bldg_chw_high_temp_Value
        ],
    ),
)

##register plugins
register.check_plugin(
    name = "hvac_controller_bldg_chw_high_temp",
    service_name='HVAC Controller bldg_chw_high_temp',
    discovery_function= discover_hvac_controller_bldg_chw_high_temp,
    check_function= check_hvac_controller_bldg_chw_high_temp,
    )
