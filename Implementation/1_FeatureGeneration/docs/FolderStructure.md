# Folder Structure
The `ScenarioGenerator` generates a specific folder structure, which is expected by the `ScenarioLoader` and `ScenarioExporter`. This documentation outlines this structure.

The base folder is a collection of scenarios. It contains one folder per scenario, named after the scenario name.

Each scenario folder in turn contains four folders:
* `measuremnets`: This folder contains the actual simulation results. For each leak config, there is one folder named after the leak config. Within each folder there are the measurements in the seperate files `demand.csv`, `flow.csv` and `pressure.csv`.
* `sensors`: This folder contans one xml file for each sensor config, named after the config name.
* `sensorfaults`: This folder contans one xml file for each sensorfault config, named after the config name.
* `leaks`: This folder contans one xml file for each leak config, named after the config name.