from pyapi.core.spawn_processes import spawn_worldsoop_processes_from_configs
from pyapi.core.implementation_wrappers import (
    OutputCondition,
    OutputFunction,
    StochadexIterations,
    TerminationCondition,
    TimestepFunction,
    WorldsoopIterations,
)
from pyapi.core.config_builder import (
    OtherParams,
    SimulatorImplementationsConfig,
    StochadexImplementationsConfig,
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
                    "transition_rates_partition_index": [0],
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
            iterations=[
                ["constantValues", "stateTransition"], 
            ],
            output_condition=OutputCondition.every_step(),
            output_function=OutputFunction.stdout(),
            termination_condition=TerminationCondition.number_of_steps(100),
            timestep_function=TimestepFunction.exponential_distribution(1.0, 231),
        ),
        agent_by_partition={},
        extra_vars_by_package=[
            {
                StochadexIterations.package(): [
                    {"constantValues": StochadexIterations.constant_values()},
                ],
            },
            {
                WorldsoopIterations.package(): [
                    {"stateTransition": WorldsoopIterations.state_transition()},
                ],
            },
        ],
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
