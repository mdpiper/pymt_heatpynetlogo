from __future__ import absolute_import

import pkg_resources
from heat import BmiHeatDiffusion as HeatDiffusion

HeatDiffusion.__name__ = "HeatDiffusion"
HeatDiffusion.METADATA = pkg_resources.resource_filename(__name__, "data/HeatDiffusion")

__all__ = [
    "HeatDiffusion",
]
