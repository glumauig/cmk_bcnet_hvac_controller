import re
from .agent_based_api.v1 import *
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
   get_value_store,
)


def discover_hvac_controller_temp_flow_delta(section):
    yield Service()

def check_hvac_controller_temp_flow_delta(section):
    hvac_snmp_name = str(section[0][0])
    hvac_snmp_value =int(section[0][1])/100

    
    hvac_snmp_name=re.sub(r"\s+", "_", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"/+", "-", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"BCN-+", "", hvac_snmp_name)


    celsius_value = round((32-hvac_snmp_value) *0.5556,2)
    hvac_snmp_value_converted = round(celsius_value,2)
    summary_hvac = "Temperature Flow Delta " + ": "+str(hvac_snmp_value)+" F" +", "+str(hvac_snmp_value_converted)+" C"
    yield Metric(hvac_snmp_name,hvac_snmp_value_converted)
    yield Result(state=State.OK,summary=summary_hvac)

    return


register.snmp_section(
    name = "hvac_controller_temp_flow_delta",
    detect = exists(".1.3.6.1.4.1.15255.1.2.1.3.1.5.*"),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.15255.1.2.1.3.1',
        oids = [
                '5.11', #temp_flow_delta
                '2.11', #temp_flow_delta_Value
        ],
    ),
)

##register plugins
register.check_plugin(
    name = "hvac_controller_temp_flow_delta",
    service_name='HVAC Controller Temperature Flow Delta',
    discovery_function= discover_hvac_controller_temp_flow_delta,
    check_function= check_hvac_controller_temp_flow_delta,
    )
