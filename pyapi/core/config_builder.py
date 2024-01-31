import yaml
from pathlib import Path
from dataclasses import dataclass, asdict


@dataclass
class OtherParams:
    float_params: dict[str, float]
    int_params: dict[str, int]


@dataclass
class WorldsoopSettingsConfig:
    other_params: list[OtherParams]
    init_state_values: list[list[float]]
    init_time_value: float
    seeds: list[int]
    state_widths: list[int]
    state_history_depths: list[int]
    timesteps_history_depth: int

    def dump_yaml(self, filename: Path):
        with open(filename.as_posix(), "w") as yamlfile:
            yaml.dump(asdict(self), yamlfile)

