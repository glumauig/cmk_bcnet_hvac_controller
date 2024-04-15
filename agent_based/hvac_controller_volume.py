import re
from .agent_based_api.v1 import *
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
   get_value_store,
)


def discover_hvac_controller_volume(section):
    yield Service()

def check_hvac_controller_volume(section):
    hvac_snmp_name = str(section[0][0])
    hvac_snmp_value =int(section[0][1])/100
    hvac_snmp_value_converted = round(hvac_snmp_value * 0.06309,2)

    
    hvac_snmp_name=re.sub(r"\s+", "_", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"/+", "-", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"BCN-+", "", hvac_snmp_name)
    

    if hvac_snmp_value < 2:   
        summary_hvac = "Very Low CHW Flow - " + hvac_snmp_name + ": "+str(hvac_snmp_value)+" GPM"
        yield Result(state=State.CRIT,summary=summary_hvac)
    else:
        summary_hvac = "" + hvac_snmp_name + ": "+str(hvac_snmp_value)+" GPM"
        yield Result(state=State.OK,summary=summary_hvac)
    
    
    yield Metric(hvac_snmp_name,hvac_snmp_value)
        

    return


register.snmp_section(
    name = "hvac_controller_volume",
    detect = exists(".1.3.6.1.4.1.15255.1.2.1.3.1.5.*"),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.15255.1.2.1.3.1',
        oids = [
                '5.8', #Volume
                '2.8', #Volume_Value
        ],
    ),
)

##register plugins
register.check_plugin(
    name = "hvac_controller_volume",
    service_name='HVAC Controller Volume',
    discovery_function= discover_hvac_controller_volume,
    check_function= check_hvac_controller_volume,
    )
