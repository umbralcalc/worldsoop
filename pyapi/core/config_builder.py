import yaml
import tempfile

from pathlib import Path
from dataclasses import dataclass, asdict


def dump_yaml(data, filename: Path):
    with open(filename.as_posix(), "w") as yamlfile:
        yaml.dump(asdict(data), yamlfile)


def dump_temporary_yaml(data) -> tempfile._TemporaryFileWrapper:
    file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".yaml")
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


@dataclass
class SimulatorImplementationsConfig:
    iterations: list[str]
    output_condition: str
    output_function: str
    termination_condition: str
    timestep_function: str


@dataclass
class AgentConfig:
    actor: str
    generator: str
    observation: str


@dataclass
class StochadexImplementationsConfig:
    simulator: SimulatorImplementationsConfig
    agents: list[AgentConfig]
    extra_vars_by_package: list[dict[str, list[dict[str, str]]]]


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
