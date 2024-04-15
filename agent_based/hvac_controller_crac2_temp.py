import re
from .agent_based_api.v1 import *
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
   get_value_store,
)


def discover_hvac_controller_crac2_temp(section):
    yield Service()

def check_hvac_controller_crac2_temp(section):
    hvac_snmp_name = str(section[0][0])
    hvac_snmp_value =int(section[0][1])/100

    
    hvac_snmp_name=re.sub(r"\s+", "_", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"/+", "-", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"BCN-+", "", hvac_snmp_name)


    faran_value = round((hvac_snmp_value *1.8 +32),2)
    hvac_snmp_value_converted = round(faran_value,2)
    summary_hvac = "CRAC2 RA Temperature " + ": "+str(hvac_snmp_value)+" C" +", "+str(hvac_snmp_value_converted)+" F"
    yield Metric(hvac_snmp_name,hvac_snmp_value)
    yield Result(state=State.OK,summary=summary_hvac)

    return


register.snmp_section(
    name = "hvac_controller_crac2_temp",
    detect = exists(".1.3.6.1.4.1.15255.1.2.1.3.1.5.*"),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.15255.1.2.1.3.1',
        oids = [
                '5.51', #crac2_temp
                '2.51', #crac2_temp_Value
        ],
    ),
)

##register plugins
register.check_plugin(
    name = "hvac_controller_crac2_temp",
    service_name='HVAC Controller CRAC2 RA Temperature',
    discovery_function= discover_hvac_controller_crac2_temp,
    check_function= check_hvac_controller_crac2_temp,
    )
