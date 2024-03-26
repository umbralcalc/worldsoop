from pyapi.core.spawn_processes import spawn_worldsoop_processes_from_configs
from pyapi.core.implementation_wrappers import (
    ConstantTimestepFunction,
    EveryStepOutputCondition,
    NumberOfStepsTerminationCondition,
    StdoutOutputFunction,
    WienerProcessIteration,
)
from pyapi.core.config_builder import (
    OtherParams,
    SimulatorImplementationsConfig,
    StochadexImplementationsConfig,
    StochadexPartition,
    StochadexSettingsConfig,
    WorldsoopConfig,
)


def main():
    settings = StochadexSettingsConfig(
        other_params=[
            OtherParams(
                float_params={
                    "variances": [1.0, 1.0, 1.0, 1.0, 1.0],
                },
                int_params={},
            ),
            OtherParams(
                float_params={
                    "variances": [1.0, 1.0, 1.0],
                },
                int_params={},
            ),
        ],
        init_state_values=[
            [0.45, 1.4, 0.01, -0.13, 0.7],
            [0.01, -0.13, 0.7],
        ],
        init_time_value=0.0,
        seeds=[4673, 2531],
        state_widths=[5, 3],
        state_history_depths=[2, 2],
        timesteps_history_depth=2,
    )
    implementations = StochadexImplementationsConfig(
        simulator=SimulatorImplementationsConfig(
            partitions=[
                StochadexPartition(
                    iteration=WienerProcessIteration(),
                    params_by_upstream_partition={},
                ),
                StochadexPartition(
                    iteration=WienerProcessIteration(),
                    params_by_upstream_partition={},
                ),
            ],
            output_condition=EveryStepOutputCondition(),
            output_function=StdoutOutputFunction(),
            termination_condition=NumberOfStepsTerminationCondition(
                max_number_of_steps=100,
            ),
            timestep_function=ConstantTimestepFunction(stepsize=1.0),
        ),
        extra_vars_by_package=[],
    )
    config = WorldsoopConfig(
        settings=settings,
        implementations=implementations,
    )
    spawn_worldsoop_processes_from_configs(
        max_workers=2,
        configs=[config, config],
    )


if __name__ == "__main__":
    main()
