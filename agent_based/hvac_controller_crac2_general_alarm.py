import re
from .agent_based_api.v1 import *
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
   get_value_store,
)


def discover_hvac_controller_crac2_general_alarm(section):
    yield Service()

def check_hvac_controller_crac2_general_alarm(section):
    hvac_snmp_name = str(section[0][0])
    hvac_snmp_value = int(section[0][1])

    
    hvac_snmp_name=re.sub(r"\s+", "_", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"/+", "-", hvac_snmp_name)
    hvac_snmp_name=re.sub(r"BCN-+", "", hvac_snmp_name)

    if hvac_snmp_value == 0:
        hvac_snmp_value_converted = "None"
        summary_hvac = "CRAC2 General Alarm: " + str(hvac_snmp_value_converted)
        yield Result(state=State.OK,summary=summary_hvac)

    else:
        hvac_snmp_value_converted = "Present on CRAC Unit 2"
        summary_hvac = "CRAC2 General Alarm: " + str(hvac_snmp_value_converted)
        yield Result(state=State.WARN,summary=summary_hvac)

    yield Metric(hvac_snmp_name,hvac_snmp_value)


    return


register.snmp_section(
    name = "hvac_controller_crac2_general_alarm",
    detect = exists(".1.3.6.1.4.1.15255.1.2.1.3.1.5.*"),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.15255.1.2.1.3.1',
        oids = [
                '5.56', #crac2_general_alarm
                '2.56', #crac2_general_alarm_Value
        ],
    ),
)

##register plugins
register.check_plugin(
    name = "hvac_controller_crac2_general_alarm",
    service_name='HVAC Controller CRAC2 General Alarm',
    discovery_function= discover_hvac_controller_crac2_general_alarm,
    check_function= check_hvac_controller_crac2_general_alarm,
    )
