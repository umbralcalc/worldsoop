import pytest

from pathlib import Path


def test_config_dump(basic_config):
    basic_config.dump_yaml(Path("/tmp/config.yaml"))

