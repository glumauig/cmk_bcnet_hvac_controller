import re
from .agent_based_api.v1 import *
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
   get_value_store,
)


def discover_hvac_controller_crac1_mode(section):
    yield Service()

def check_hvac_controller_crac1_mode(section):
    hvac_snmp_name = str(section[0][0])
    hvac_snmp_value = int(section[0][1])

    
    hvac_snmp_name=re.sub(r"\s+", "_", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"/+", "-", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"BCN-+", "", hvac_snmp_name)

    if hvac_snmp_value == 0:
        hvac_snmp_value_converted = "DX mode"
        summary_hvac = "CRAC-1-Mode: " + str(hvac_snmp_value_converted)

    else:
        hvac_snmp_value_converted = "CHW Mode"
        summary_hvac = "CRAC-1-Mode: " + str(hvac_snmp_value_converted)
    
    yield Result(state=State.OK,summary=summary_hvac)
    yield Metric(hvac_snmp_name,hvac_snmp_value)


    return


register.snmp_section(
    name = "hvac_controller_crac1_mode",
    detect = exists(".1.3.6.1.4.1.15255.1.2.1.2.1.5*"),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.15255.1.2.1.2.1',
        oids = [
                '5.1', #crac1_mode
                '2.1', #crac1_mode_Value
        ],
    ),
)

##register plugins
register.check_plugin(
    name = "hvac_controller_crac1_mode",
    service_name='HVAC Controller CRAC-1-Mode',
    discovery_function= discover_hvac_controller_crac1_mode,
    check_function= check_hvac_controller_crac1_mode,
    )
