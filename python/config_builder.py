import yaml
from pathlib import Path
from dataclasses import dataclass, asdict


@dataclass
class OtherParams:
    float_params: dict[str, float]
    int_params: dict[str, int]


@dataclass
class WorldsoopConfig:
    other_params: list[OtherParams]
    init_state_values: list[list[float]]
    seeds: list[int]
    state_widths: list[int]
    state_history_depths: list[int]
    timesteps_history_depth: int

    def dump_yaml(self, filename: Path):
        with open(filename.as_posix(), 'w') as yamlfile:
            yaml.dump(asdict(self), yamlfile)


def main():
    WorldsoopConfig(
        other_params=[
            OtherParams(
                float_params={"variances": [1.0, 1.0, 1.0, 1.0, 1.0]},
                int_params={},
            ),
        ],
        init_state_values=[[0.45, 1.4, 0.01, -0.13, 0.7]],
        seeds=[4673],
        state_widths=[5],
        state_history_depths=[2],
        timesteps_history_depth=2,
    ).dump_yaml(Path("./cfg/config.yaml"))


if __name__ == "__main__":
    main()