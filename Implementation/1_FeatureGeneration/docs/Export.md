# Excel Export
To export a scenario to an excel sheet, the `ScenarioExporter.py` script can be used.
It takes 6 positional command line arguments:
1. `collection_path`: Path to the scenario collection to export out of.
2. `scenario_name`: Name of the scenario to export
3. `leak_config_name`: Name of the selected leak config
4. `sensorconfig_name`: Name of the selected sensorconfig
5. `sensorfault_config_name`: Name of the selected sensorfault config
6. `output`: Name of the output excel file

The example call
```
./ScenarioExporter.py collection Scenario1 Leak1 Sensor1 Sensrofault1 MyScenario.xlsx
```
exports the `Scenario1` scenario from the `collection` folder with the configs `Leak1`, `Sensor1` and `Sensorfault1` to the file `MyScenario.xlsx`.

In the excel file, the different measurements are available in different sheets.

The `ScenarioExporter.py` script needs the `ScenarioLoader.py` as a dependency.