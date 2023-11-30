#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_heatpynetlogo").version


from .bmi import HeatDiffusion

__all__ = [
    "HeatDiffusion",
]
