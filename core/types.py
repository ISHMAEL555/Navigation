"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module  : Type Definitions
Purpose : Common mathematical types used throughout the framework.
Author  : ISHMAEL
License : MIT
===============================================================================
"""

from typing import TypeAlias

import numpy as np
from numpy.typing import NDArray


Vector3: TypeAlias = NDArray[np.float64]

Vector4: TypeAlias = NDArray[np.float64]

Quaternion: TypeAlias = NDArray[np.float64]

Matrix3: TypeAlias = NDArray[np.float64]

Matrix4: TypeAlias = NDArray[np.float64]