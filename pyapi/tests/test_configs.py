from pathlib import Path

from pyapi.core.config_builder import dump_temporary_yaml


def test_config_dumps(
    stochadex_settings_config,
    stochadex_implementations_config,
):
    f = dump_temporary_yaml(stochadex_settings_config)
    f.close()
    f = dump_temporary_yaml(stochadex_implementations_config)
    f.close()
