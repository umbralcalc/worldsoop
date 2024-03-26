import pytest

from pyapi.core.implementation_wrappers import (
    ConstantTimestepFunction,
    EveryStepOutputCondition,
    NilOutputFunction,
    NumberOfStepsTerminationCondition,
    WienerProcessIteration,
)
from pyapi.core.config_builder import (
    StochadexPartition,
    StochadexSettingsConfig,
    SimulatorImplementationsConfig,
    StochadexImplementationsConfig,
    OtherParams,
)


@pytest.fixture
def stochadex_settings_config() -> StochadexSettingsConfig:
    return StochadexSettingsConfig(
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


@pytest.fixture
def simulator_implementations_config() -> SimulatorImplementationsConfig:
    return SimulatorImplementationsConfig(
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
        output_function=NilOutputFunction(),
        termination_condition=NumberOfStepsTerminationCondition(
            max_number_of_steps=100,
        ),
        timestep_function=ConstantTimestepFunction(
            stepsize=1.0,
        ),
    )


@pytest.fixture
def stochadex_implementations_config(
    simulator_implementations_config,
) -> StochadexImplementationsConfig:
    return StochadexImplementationsConfig(
        simulator=simulator_implementations_config,
        extra_vars_by_package=[],
    )
