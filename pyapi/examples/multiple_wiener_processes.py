from pyapi.core.spawn_processes import spawn_worldsoop_processes_from_configs
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
            iterations=[[r"firstWienerProcess"], [r"secondWienerProcess"]],
            output_condition=r"&simulator.EveryStepOutputCondition{}",
            output_function=r"&simulator.StdoutOutputFunction{}",
            termination_condition=(
                r"&simulator.NumberOfStepsTerminationCondition{MaxNumberOfSteps: 100}"
            ),
            timestep_function=r"&simulator.ConstantTimestepFunction{Stepsize: 1.0}",
        ),
        agent_by_partition={},
        extra_vars_by_package=[
            {
                "github.com/umbralcalc/stochadex/pkg/phenomena": [
                    {"firstWienerProcess": r"&phenomena.WienerProcessIteration{}"},
                    {"secondWienerProcess": r"&phenomena.WienerProcessIteration{}"},
                ],
            }
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
