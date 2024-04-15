# Created by: Gualberto Lumauig
# Title: Migration of HVAC monitoring from Intermapper to CHECKMK
# Date: Jan 2024
#
# Description - this is the custom graph of the hvac controller oid
#

from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import (
    metric_info,
    graph_info,
)


metric_info["ENERGY-HOUR"] = {
    "title": _("Energy per Hour - Watt/hr"),
    "unit": "wh",
    "color": "16/a",
}

metric_info["ENERGY_TOTAL"] = {
    "title": _("Energy Total - Watt/hr"),
    "unit": "wh",
    "color": "16/a",
}

metric_info["Y-T-D-ENERGY_TOTAL"] = {
    "title": _("Year-To-Date Energy Total - Watt/hr"),
    "unit": "wh",
    "color": "16/a",
}

metric_info["VOLUME-TOTAL"] = {
    "title": _("Volume Total in Gallon"),
    "unit": "",
    "color": "16/a",
}


metric_info["Y-T-D-VOLUME-TOTAL"] = {
    "title": _("Year-To-Date Volume in Gallon"),
    "unit": "",
    "color": "16/a",
}

metric_info["PREV-YR-VOLUME-TOTAL"] = {
    "title": _("Previous Year Volume in Gallon"),
    "unit": "",
    "color": "16/a",
}

metric_info["VOLUME"] = {
    "title": _("Volume in GPM"),
    "unit": "",
    "color": "16/a",
}

metric_info["SUPPLY-WATER-TEMP"] = {
    "title": _("Temperature Flow in - Celsius"),
    "unit": "c",
    "color": "16/a",
}

metric_info["RETURN-WATER-TEMP"] = {
    "title": _("Temperature Flow return - Celsius"),
    "unit": "c",
    "color": "16/a",
}

metric_info["DELTA-TEMP"] = {
    "title": _("Temperature Flow Delta - Celsius"),
    "unit": "c",
    "color": "16/a",
}

metric_info["CRAC1-R-A-TEMP"] = {
    "title": _("CRAC1 R/A Temp - Celsius"),
    "unit": "c",
    "color": "16/a",
}
metric_info["CRAC2-R-A-TEMP"] = {
    "title": _("CRAC2 R/A Temp - Celsius"),
    "unit": "c",
    "color": "16/a",
}
metric_info["CRAC1-R-A-RH"] = {
    "title": _("CRA1 R/A Relative Humidity - Percentage"),
    "unit": "%",
    "color": "16/a",
}
metric_info["CRAC2-R-A-RH"] = {
    "title": _("CRAC2 R/A Relative Humidity - Percentage"),
    "unit": "%",
    "color": "16/a",
}

#This portion is a metric for value output 0 and 1 only. 
#Created to have a historical graph of the states.


metric_info["CRAC-Alarm-Light"] = {
    "title": _("CRAC Alarm Light [0- OFF | 1- ON]"),
    "unit": "count",
    "color": "16/a",
}

metric_info["CRAC-Alarm-Reset"] = {
    "title": _("CRAC Alarm Reset [0- NORMAL | 1- ALARM]"),
    "unit": "count",
    "color": "16/a",
}

metric_info["Bldg-CHW-Flow"] = {
    "title": _("Bldg CHW Flow [0- NORMAL | 1- FAIL]"),
    "unit": "count",
    "color": "16/a",
}

metric_info["Bldg-CHW-High-Temp"] = {
    "title": _("Bldg CHW High Temp [0- NORMAL | 1- HIGH TEMP]"),
    "unit": "count",
    "color": "16/a",
}

metric_info["Crac1-General-Alarm"] = {
    "title": _("CRAC1-GENERAL-ALARM [0- NONE | 1- PRESENT]"),
    "unit": "count",
    "color": "16/a",
}

metric_info["Crac1-Critical-Alarm"] = {
    "title": _("CRAC1-CRITICAL-ALARM [0- NONE | 1- PRESENT]"),
    "unit": "count",
    "color": "16/a",
}

metric_info["CRAC-1-Mode"] = {
    "title": _("CRAC-1-Mode [0- DX MODE | 1- CHW MODE]"),
    "unit": "count",
    "color": "16/a",
}

metric_info["Crac2-General-Alarm"] = {
    "title": _("CRAC2-GENERAL-ALARM [0- NONE | 1- PRESENT]"),
    "unit": "count",
    "color": "16/a",
}

metric_info["Crac2-Critical-Alarm"] = {
    "title": _("CRAC2-CRITICAL-ALARM [0- NONE | 1- PRESENT]"),
    "unit": "count",
    "color": "16/a",
}

metric_info["CRAC-2-Mode"] = {
    "title": _("CRAC-2-Mode [0- DX MODE | 1- CHW MODE]"),
    "unit": "count",
    "color": "16/a",
}