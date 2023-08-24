import asyncio, logging, subprocess
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
    MODEL = Model(ModelFamily("viam","disk_sensor"), "linux")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        sensor = cls(config.name)
        return sensor

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        lines = subprocess.check_output(['df']).splitlines()[1:]
        logger.info("get_readings ok %d lines", len(lines))
        return {
            (row := line.strip().split())[-1]: row[-2] for line in lines
        }

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
