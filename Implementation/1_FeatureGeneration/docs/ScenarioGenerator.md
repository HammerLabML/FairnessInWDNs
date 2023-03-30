# Scenario Generator
The `ScenarioGenerator.py` script is used to generate scenarios from a xml configuration file. It can take multiple command line arguments:
```
./ScenarioGenerator.py config [collection_path] [-h] [-f] [-s [SELECTION ...]] [-p] [-t THREADS] [-m MAX_MEMORY] [-v]
```
Only the `config_file` parameter is required.

By default, the script checks which parts are already present and only generates those which are missing. To override this behaviour, use the force flag.

## Parameters
|Parameter                  |Function                                                                                           |
|---------------------------|---------------------------------------------------------------------------------------------------|
|`config`                   |Path to the Scenario Collection configuration file |
|`collection_path`          |Path where simulation results are saved to (Default: Scenario Collection path)|
|`-f`/`--force-regenerate`  |Force existing simulations results to be re-generated|
|`-s`/`--selection`         |Selection, which Scenarios and Leak Configurations should be generated in format "[SCENARIO].[LEAK_CONFIG]" where [LEAK_CONFIG] can use "*" as wildcard|
|`-p`/`--parallel`          |Enable parallelized simulation on all available cores|
|`-t`/`--threads`           |Specify a number of threads for parallelized simulation (Overwrites "-p")|
|`-m`/`--max-memory`        |Maximum memory this generator should consume in MB|
|`-v`/`--verbose`           |Enable verbose output, -vv for extra verbose|

### Selection String format Example

```
--selection=Scenario1.*,Scenario2.Leak1,Scenario2.Leak3
```