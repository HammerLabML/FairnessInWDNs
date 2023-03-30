#!/usr/bin/env python3

import sys
from ScenarioLoader import ScenarioCollection
import pandas as pd

if __name__ == '__main__':

    # Check if enough arguments are given
    if len(sys.argv) != 7:
        print('Usage: ScenarioExporter.py collection_path scenario_name leak_config_name sensorconfig_name sensorfault_config_name output')
        sys.exit(1)

    # Retrieve command line arguments
    collection_path = sys.argv[1]
    scenario_name = sys.argv[2]
    leak_config_name = sys.argv[3]
    sensorconfig_name = sys.argv[4]
    sensorfault_config_name = sys.argv[5]
    output = sys.argv[6] if sys.argv[6].endswith('.xlsx') else f'{sys.argv[6]}.xlsx'

    # Initialize scenario collection and retrieve the measurements
    collection = ScenarioCollection(collection_path)
    data = collection.get(scenario_name, leak_config_name, sensorconfig_name, sensorfault_config_name)

    # Add measurements to excel writer and write
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    for sheet in data.keys():
        data[sheet].to_excel(writer, sheet_name=sheet)

    writer.save()

 