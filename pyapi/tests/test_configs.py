from pathlib import Path
from pyapi.core.config_builder import (
    StochadexImplementationsConfig, 
    StochadexSettingsConfig, 
    dump_temporary_yaml,
)


def test_config_dumps(
    stochadex_settings_config,
    stochadex_implementations_config,
):
    f = dump_temporary_yaml(stochadex_settings_config)
    f.close()
    f = dump_temporary_yaml(stochadex_implementations_config)
    f.close()


def test_config_loads(
    stochadex_settings_config,
    stochadex_implementations_config,
):
    f = dump_temporary_yaml(stochadex_settings_config)
    config = StochadexSettingsConfig.from_yaml(Path(f.name))
    assert stochadex_settings_config == config
    f.close()
    f = dump_temporary_yaml(stochadex_implementations_config)
    config = StochadexImplementationsConfig.from_yaml(Path(f.name))
    assert stochadex_implementations_config == config
    f.close()
