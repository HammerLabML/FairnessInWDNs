# Waterfutures Scenario Generation (v2.2)
This repository contains scripts to generate water network simulations with leaks and sensorfaults. 
It also provides a loader uitility and a script to export given configurations to an excel sheet.

There is seperate documentation for each functionality offered in this repostiory:

* [Scenario Configuration](docs/ScenarioConfig.md)
* [Scenario Generator](docs/ScenarioGenerator.md)
* [Scenario Loader](docs/ScenarioLoader.md)
* [Folder Structure](docs/FolderStructure.md)
* [Scenario Export to Excel](docs/Export.md)

All scripts are based on the dependencies listed in the `requirements.txt`.

## Version History

### v2.2
- The `partId` attribute was split into `pipeId` and `nodeId` to ensure compatability with input files that reuse identifiers.
- Reworked threading to be more functional, also now using `threading` library.
- Improved job memory estimation
- Using library to validate XML
- Using library to parse command line params
- Improved logging
- General Refactoring and Code maintenance up

### v2.1
- Leaks can now be simulated on pipes and nodes
- The `pipeId` attribute for leaks was renamed to `partId`.
- Added code snippet to import `ScenarioLoader` in a python notebook to docs

### v2.0
- Complete new codebase compared to v1.0
- Added documentation
- All known issues from v1.0 fixed
- Moved v1.0 in its own subfolder

### v1.0
- Initial version with several bugs and little documentation