from pathlib import Path
from pyapi.core.config_builder import (
    StochadexSettingsConfig, 
    dump_temporary_api_yaml,
)


def test_config_dumps(
    stochadex_settings_config,
    stochadex_implementations_config,
):
    f = dump_temporary_api_yaml(stochadex_settings_config)
    f.close()
    f = dump_temporary_api_yaml(stochadex_implementations_config)
    f.close()


def test_settings_config_loads(
    stochadex_settings_config,
):
    f = dump_temporary_api_yaml(stochadex_settings_config)
    config = StochadexSettingsConfig.from_yaml(Path(f.name))
    assert stochadex_settings_config == config
    f.close()