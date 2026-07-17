"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module  : Truth Trajectory
Purpose : Container for the spacecraft truth trajectory.
Author  : ISHMAEL
License : MIT
===============================================================================
"""

from dataclasses import dataclass, field

from .truth_state import TruthState


@dataclass(slots=True)
class TruthTrajectory:
    """
    Collection of truth states describing the spacecraft trajectory.

    The trajectory itself performs no propagation.
    It simply stores the time history of TruthState objects.
    """

    states: list[TruthState] = field(default_factory=list)

    def append(self, state: TruthState) -> None:
        """
        Append a truth state to the trajectory.

        Parameters
        ----------
        state : TruthState
            Truth state to append.
        """
        self.states.append(state)

    def __len__(self) -> int:
        """Return the number of stored states."""
        return len(self.states)

    def __getitem__(self, index: int) -> TruthState:
        """Return the truth state at the given index."""
        return self.states[index]