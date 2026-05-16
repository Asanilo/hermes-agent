import asyncio, yaml, os
from gateway.platforms.feishu import FeishuAdapter, FEISHU_DOMAIN
from gateway.config import PlatformConfig

with open('/home/arinp22/.hermes/config.yaml') as f:
    config = yaml.safe_load(f)

feishu_extra = config['platforms']['feishu']
pconfig = PlatformConfig(extra=feishu_extra)
adapter = FeishuAdapter(pconfig)
adapter._client = adapter._build_lark_client(FEISHU_DOMAIN)

async def run():
    result = await adapter.send_image_file(
        'oc_35f06c83d91c9e0038ae5b0b93e8f5d4',
        '/home/arinp22/Pictures/壁纸/🌼_107262522.jpg'
    )
    print(result)

asyncio.run(run())