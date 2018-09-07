# RELEASES

## Introduction
Releases (> 0.1.0) correspond to the version hosted on [pypi.org](https://pypi.org/manage/project/beacontau/releases/), which can be obtained via `pip install BeaconTau`.
The version hosted on github may be ahead of the most recent pypi, if this is the case then this tag is unstable, may be moved or removed, as it represents a release under active development.
The [libbeacon](https://github.com/beaconTau/libbeacon) library is tagged in sync with the BeaconTau since setup.py pulls in the matching version.

## [0.1.4] - 2018-09-07

### Added
- RunAnalyzer class to draw, scan, event properties, wraps aroun
- RELEASES.md to prevent cluttering of the README.md
- EventAnalyzer.py, RunAnalyzer.py, DataDirectory.py get their own file.

### Changed
- Track name change in upstream repository from libnuphase -> libbeacon, this is reflected in BeaconTau.cpp
- Fix module imports so it now works not in the directory.
- Reflected restructured module in __init__.py
- Rename RunReader to FileReader to make the distrinction between RunAnalyzer clear

### Removed
- BeaconTau.py




## [0.1.3] - 2018-09-05

### Fixed
- Add std=c++11 flag for compiling against pybind11




## [0.1.2] - 2018-09-05

### Fixed
- Ensure pybind11 is installed before running setup.py (since we need to compile the c++ code which includes the pybind11 headers)




## [0.1.1] - 2018-09-05

### Added
- Ability to install project from PyPI
- setup.py, required for a pip install




## [0.1.0] - 2018-09-04

### Added
- Working local implementation of BeaconTau, which has the binary data in the python interpreter
- Proto-web viewer Flame (Facility for Live Action Monitoring of Events) using bokeh


