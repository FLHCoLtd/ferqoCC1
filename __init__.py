"""Example Load Platform integration."""
from homeassistant.helpers import discovery
from datetime import timedelta
import logging
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
import async_timeout
from .hub import FerqoCCApi
from homeassistant.helpers.event import async_track_time_interval, _LOGGER
import asyncio
from homeassistant.helpers.discovery import async_load_platform
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.const import (
    CONF_HOST,
    CONF_USERNAME,
    CONF_PASSWORD,
)
FERQOCC_COMPONENTS = [
    "cover",
    "light",
    "sensor",
    # "lock",
    "switch",
]
from .const import DOMAIN, serverList, CC_COORDINATORS

CONFIG_SCHEMA = vol.Schema(
    vol.All(
        cv.deprecated(DOMAIN),
        {
            DOMAIN: vol.Schema(
                {
                    vol.Required(CONF_HOST): cv.string,
                    vol.Required(CONF_USERNAME): cv.string,
                    vol.Required(CONF_PASSWORD): cv.string,
                }
            )
        },
    ),
    extra=vol.ALLOW_EXTRA,
)


def setup(hass, config):
    """Setup the eWelink/Sonoff component."""

    _LOGGER.debug("Create the main object")

    hass.data[DOMAIN] = FerqoCCApi(config)
    hass.data[DOMAIN].getEntitiesList()
    for component in FERQOCC_COMPONENTS:
        discovery.load_platform(hass, component, DOMAIN, {}, config)

    def update_devices(event_time):
        asyncio.run_coroutine_threadsafe(async_updateData(hass), hass.loop)

    async_track_time_interval(hass, update_devices, timedelta(seconds=20))


    return True

async def async_updateData(hass):
    list = hass.data[DOMAIN].getEntitiesList()
    return list

