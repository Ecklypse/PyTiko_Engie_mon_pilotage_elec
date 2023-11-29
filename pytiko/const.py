"""Constants for Tiko Mon Pilotage Elec."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "pytiko"
DOMAIN = "pytiko"
VERSION = "0.0.0"
ATTRIBUTION = "Data provided by https://portal-engie.tiko.ch/api/v3/graphql//"
POLL_INTERVAL = "poll_interval"
DEFAULT_POLL_INTERVAL = 5

# APIs
CONF_API_TIMEOUT = 2

#URLs
API_HOST = "https://portal-engie.tiko.ch"
API_ENDPOINT = "/api/v3/graphql/"