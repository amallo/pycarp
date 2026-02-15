"""
Dependencies interface for device command handlers. Implementations: ProductionDependencies (prod), TestDependencies (tests).
"""

from abc import ABC, abstractmethod

from core.device.gateways.config_gateway import ConfigGateway
from core.device.gateways.device_id_generator import DeviceIdGenerator
from core.gateways.event_publisher import EventPublisher


class Dependencies(ABC):
    """Contract: provides config_gateway, device_id_generator, event_publisher for device command handlers."""

    @property
    @abstractmethod
    def config_gateway(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def device_id_generator(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def event_publisher(self):
        raise NotImplementedError


class ProductionDependencies(Dependencies):
    """Production: holds real implementations injected at composition root."""

    def __init__(self, config_gateway, device_id_generator, event_publisher):
        self._config_gateway = config_gateway
        self._device_id_generator = device_id_generator
        self._event_publisher = event_publisher

    @property
    def config_gateway(self):
        return self._config_gateway

    @property
    def device_id_generator(self):
        return self._device_id_generator

    @property
    def event_publisher(self):
        return self._event_publisher
