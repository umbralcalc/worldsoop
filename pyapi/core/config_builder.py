from typing import Any
import yaml
import tempfile

from pathlib import Path
from dataclasses import dataclass, asdict

from pyapi.core.implementation_wrappers import (
    OutputCondition, 
    OutputFunction, 
    StochadexIteration, 
    TerminationCondition, 
    TimestepFunction,
)


def load_yaml(filename: Path) -> dict:
    with open(filename.as_posix(), "r") as f:
        return yaml.safe_load(f)


def dump_yaml(data, filename: Path):
    to_yaml = getattr(data, "to_yaml", None)
    d = data.to_yaml() if callable(to_yaml) else asdict(data)
    with open(filename.as_posix(), "w") as yamlfile:
        yaml.dump(d, yamlfile)


def dump_temporary_yaml(data) -> tempfile._TemporaryFileWrapper:
    file = tempfile.NamedTemporaryFile(mode="w", suffix=".yaml")
    dump_yaml(data, Path(file.name))
    return file


@dataclass
class OtherParams:
    float_params: dict[str, float]
    int_params: dict[str, int]


@dataclass
class StochadexSettingsConfig:
    other_params: list[OtherParams]
    init_state_values: list[list[float]]
    init_time_value: float
    seeds: list[int]
    state_widths: list[int]
    state_history_depths: list[int]
    timesteps_history_depth: int

    @classmethod
    def from_yaml(cls, filename: Path) -> "StochadexSettingsConfig":
        data = load_yaml(filename)
        data["other_params"] = [OtherParams(**p) for p in data["other_params"]]
        return cls(**data)


@dataclass
class StochadexPartition:
    iteration: StochadexIteration
    params_by_upstream_partition: dict[int, str]

    def to_yaml(self) -> dict[str, Any]:
        yaml_dict = asdict(self)
        yaml_dict["iteration"] = self.iteration.to_yaml()
        return yaml_dict


@dataclass
class SimulatorImplementationsConfig:
    partitions: list[StochadexPartition]
    output_condition: OutputCondition
    output_function: OutputFunction
    termination_condition: TerminationCondition
    timestep_function: TimestepFunction

    def to_yaml(self) -> dict[str, Any]:
        return {
            "partitions": [p.to_yaml() for p in self.partitions],
            "output_condition": self.output_condition.to_yaml(),
            "output_function": self.output_function.to_yaml(),
            "termination_condition": self.termination_condition.to_yaml(),
            "timestep_function": self.timestep_function.to_yaml(),
        }


@dataclass
class StochadexImplementationsConfig:
    simulator: SimulatorImplementationsConfig
    extra_vars_by_package: list[dict[str, list[dict[str, str]]]]

    def __post_init__(self):
        used_packages = set()
        used_packages.add("github.com/umbralcalc/stochadex/pkg/simulator")
        for p in self.simulator.partitions:
            package = p.iteration.value.package()
            if package not in used_packages:
                self.extra_vars_by_package.append({package: []})
                used_packages.add(package)

    @classmethod
    def from_yaml(cls, filename: Path) -> "StochadexImplementationsConfig":
        data = load_yaml(filename)
        data["simulator"] = SimulatorImplementationsConfig(**data["simulator"])
        return cls(**data)
    
    def to_yaml(self) -> dict[str, Any]:
        yaml_dict = asdict(self)
        yaml_dict["simulator"] = self.simulator.to_yaml()
        return yaml_dict


@dataclass
class DashboardConfig:
    address: str
    handle: str
    millisecond_delay: int
    react_app_location: str
    launch_dashboard: bool


@dataclass
class WorldsoopConfig:
    settings: StochadexSettingsConfig
    implementations: StochadexImplementationsConfig
    dashboard: DashboardConfig | None = None

    def to_yaml(self) -> dict[str, Any]:
        yaml_dict = asdict(self)
        yaml_dict["implementations"] = self.implementations.to_yaml()
        return yaml_dict
