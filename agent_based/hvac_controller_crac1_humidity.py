import re
from .agent_based_api.v1 import *
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
   get_value_store,
)


def discover_hvac_controller_crac1_humidity(section):
    yield Service()

def check_hvac_controller_crac1_humidity(section):
    hvac_snmp_name = str(section[0][0])
    hvac_snmp_value =int(section[0][1])/100

    
    hvac_snmp_name=re.sub(r"\s+", "_", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"/+", "-", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"BCN-+", "", hvac_snmp_name)


    summary_hvac = "CRAC1 RA RH" + ": "+str(hvac_snmp_value)+"% Relative Humidity"
    yield Metric(hvac_snmp_name,hvac_snmp_value)
    yield Result(state=State.OK,summary=summary_hvac)




    return


register.snmp_section(
    name = "hvac_controller_crac1_humidity",
    detect = exists(".1.3.6.1.4.1.15255.1.2.1.3.1.5.*"),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.15255.1.2.1.3.1',
        oids = [
                '5.22', #crac1_humidity
                '2.22', #crac1_humidity_Value
        ],
    ),
)

##register plugins
register.check_plugin(
    name = "hvac_controller_crac1_humidity",
    service_name='HVAC Controller CRAC1 RA Relative Humidity',
    discovery_function= discover_hvac_controller_crac1_humidity,
    check_function= check_hvac_controller_crac1_humidity,
    )
