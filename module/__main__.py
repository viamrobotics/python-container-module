import asyncio, logging
from typing import Any, Dict, Mapping, Optional

from viam.components.sensor import Sensor
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
from viam.module.module import Module
from viam.resource.registry import Registry, ResourceCreatorRegistration

logger = logging.getLogger(__name__)

class MySensor(Sensor):
    MODEL = Model(ModelFamily("viam","wifi_sensor"), "linux")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        sensor = cls(config.name)
        return sensor

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        logger.info("get_readings top")
        with open("/proc/net/wireless") as wifi_stats:
            content = wifi_stats.readlines()
        logger.info("get_readings ok read")
        wifi_signal = [x for x in content[2].split(" ") if x != ""]
        return {"link": wifi_signal[2], "level": wifi_signal[3], "noise": wifi_signal[4]}

    async def get_geometries(self):
        return []

# Anything below this line is optional and will be replaced later, but may come in handy for debugging and testing.
# To use, call `python wifi_sensor.py` in the command line while in the `src` directory.
async def main():
    logging.basicConfig(level=logging.INFO)
    Registry.register_resource_creator(MySensor.SUBTYPE, MySensor.MODEL, ResourceCreatorRegistration(MySensor.new))
    module = Module.from_args()
    module.add_model_from_registry(MySensor.SUBTYPE, MySensor.MODEL)
    await module.start()

if __name__ == '__main__':
    asyncio.run(main())
