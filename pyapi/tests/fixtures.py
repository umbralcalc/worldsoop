import pytest

from pyapi.core.implementation_wrappers import (
    OutputCondition,
    OutputFunction,
    TerminationCondition,
    TimestepFunction,
    StochadexPhenomena,
)
from pyapi.core.config_builder import (
    StochadexSettingsConfig,
    SimulatorImplementationsConfig,
    AgentConfig,
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
                    "observation_noise_variances": [0.5, 0.5, 0.5, 0.5, 0.5],
                },
                int_params={},
            ),
            OtherParams(
                float_params={
                    "variances": [1.0, 1.0, 1.0],
                    "observation_noise_variances": [0.5, 0.5, 0.5],
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
        iterations=[["firstWienerProcess"], ["secondWienerProcess"]],
        output_condition=OutputCondition.every_step(),
        output_function=OutputFunction.nil(),
        termination_condition=TerminationCondition.number_of_steps(100),
        timestep_function=TimestepFunction.constant(1.0),
    )


@pytest.fixture
def agent_config() -> AgentConfig:
    return AgentConfig(
        actor=r"&interactions.DoNothingActor{}",
        generator=r"&interactions.DoNothingActionGenerator{}",
        observation=r"&interactions.GaussianNoiseStateObservation{}",
    )


@pytest.fixture
def stochadex_implementations_config(
    simulator_implementations_config,
    agent_config,
) -> StochadexImplementationsConfig:
    return StochadexImplementationsConfig(
        simulator=simulator_implementations_config,
        agent_by_partition={0: agent_config, 1: agent_config},
        extra_vars_by_package=[
            {
                StochadexPhenomena.package(): [
                    {"firstWienerProcess": StochadexPhenomena.wiener_process()},
                    {"secondWienerProcess": StochadexPhenomena.wiener_process()},
                ],
            }
        ],
    )
