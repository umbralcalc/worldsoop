from pyapi.core.spawn_processes import spawn_worldsoop_processes_from_configs
from pyapi.core.implementation_wrappers import (
    ConstantValuesIteration,
    EveryStepOutputCondition,
    ExponentialDistributionTimestepFunction,
    NumberOfStepsTerminationCondition,
    StateTransitionIteration,
    StdoutOutputFunction,
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
                float_params={},
                int_params={},
            ),
            OtherParams(
                float_params={},
                int_params={
                    "transitions_from_0": [1, 2, 3, 4],
                    "transitions_from_1": [3, 4, 5],
                    "transitions_from_2": [5],
                    "transitions_from_3": [1],
                    "transitions_from_4": [3, 2],
                    "transitions_from_5": [1],
                },
            ),
        ],
        init_state_values=[
            [1.0, 2.0, 1.0, 1.0, 0.3, 1.2, 0.1, 1.0, 1.0, 1.0, 2.0, 0.5],
            [0],
        ],
        init_time_value=0.0,
        seeds=[0, 231],
        state_widths=[12, 1],
        state_history_depths=[2, 2],
        timesteps_history_depth=2,
    )
    implementations = StochadexImplementationsConfig(
        simulator=SimulatorImplementationsConfig(
            partitions=[
                StochadexPartition(
                    iteration=ConstantValuesIteration(),
                    params_by_upstream_partition={},
                ),
                StochadexPartition(
                    iteration=StateTransitionIteration(),
                    params_by_upstream_partition={
                        0: "transition_rates",
                    },
                ),
            ],
            output_condition=EveryStepOutputCondition(),
            output_function=StdoutOutputFunction(),
            termination_condition=NumberOfStepsTerminationCondition(
                max_number_of_steps=100,
            ),
            timestep_function=ExponentialDistributionTimestepFunction(
                mean=1.0, 
                seed=231,
            ),
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
