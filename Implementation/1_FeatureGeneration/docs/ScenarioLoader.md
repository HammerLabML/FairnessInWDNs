# Scenario Loader
The `ScenarioLoader.py` helper is a utility to easily load measurements from a scenario collection.

To import the `ScenarioLoader` in a python notebook environment, you can use this snippet:
```
# Add directory to path
import os, sys
module_path = os.path.abspath('path-to-this-git')
if module_path not in sys.path:
    sys.path.append(module_path)

# Import ScenarioLoader
import ScenarioLoader
```

There are two classes that can be used for loading, either the `ScenarioCollection` or the `Scenario`.

## ScenarioCollection
There are several functions to explore the collection and retrive measurements:

|Function       |Description                                                    |
|---------------|---------------------------------------------------------------|
|constructor    |Construct the collection object, given a path to a collection  |
|list_scenarios |List all scenarios in the collection                           |
|get_scenario   |Get a scenario by name                                         |
|list_configs   |List the configs of a given scenario withing the collection    |
|get            |Retrive measurements for specific scenario and set of configs  |

## Scenario
If only one scenario is relevant, a scenario object can be used. It can be either constructed directly or retrieved from a collection.

|Function       |Description                                                    |
|---------------|---------------------------------------------------------------|
|constructor    |Construct the Scenario object, given a path to a Scenario      |
|list_configs   |List the configs of this scenario                              |
|get            |Retrive measurements for specific set of configs               |


## Return Types
* Scenario List: List of strings containing scenario names
* Config list: Dict with keys `LeakConfigs`, `SensorConfigs` and `SensorfaultConfigs`. Each entry contains a list of strings.
* Measurements: Dict with keys `demand`, `flow` and `pressure`. Each containing a dataframe with the requested measurements

## Example
```
from ScenarioLoader import ScenarioCollection, Scenario

# Initialize Collection
collection = ScenarioCollection('samples')

# List Scenarios
scenarios = collection.list_scenarios()
print('Scenarios in collection:', scenarios)

# List Configs of first scenario
first_configs = collection.list_configs(scenarios[0])
print('Leak configs in first scenario:', first_configs['LeakConfigs'])
print('Sensor configs in first scenario:', first_configs['SensorConfigs'])
print('Sensorfault configs in first scenario:', first_configs['SensorfaultConfigs'])

# Load data with first configs
example_data = collection.get(scenarios[0], first_configs['LeakConfigs'][0], first_configs['SensorConfigs'][0], first_configs['SensorfaultConfigs'][0])

# Extract data from dict
demand = example_data['demand']
flow = example_data['flow']
pressure = example_data['pressure']
```