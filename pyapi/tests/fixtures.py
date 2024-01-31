import pytest

from pathlib import Path
from pyapi.core.config_builder import WorldsoopSettingsConfig, OtherParams


@pytest.fixture
def basic_config() -> WorldsoopSettingsConfig:
    return WorldsoopSettingsConfig(
        other_params=[
            OtherParams(
                float_params={"variances": [1.0, 1.0, 1.0, 1.0, 1.0]},
                int_params={},
            ),
        ],
        init_state_values=[[0.45, 1.4, 0.01, -0.13, 0.7]],
        init_time_value=0.0,
        seeds=[4673],
        state_widths=[5],
        state_history_depths=[2],
        timesteps_history_depth=2,
    )