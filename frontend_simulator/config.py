from dynaconf import Dynaconf
import os

# Determine the default value based on the environment
default_server = 'docker' if 'DOCKER_ENV' in os.environ else 'local'

# Configure Dynaconf with default_env
settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
    default_env=default_server,
    environments=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
