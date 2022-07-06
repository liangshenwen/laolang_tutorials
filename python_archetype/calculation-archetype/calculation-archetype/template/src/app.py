import os
from typing import Dict, Any

import starflow

module_name = get_module_name(__file__, mode="leaf")
logger = get_logger(module_name)
__env__ = os.getenv('MSTAR_ENV', 'default')

app = starflow.App()


@app.run(run_type='calc_app_1')
def calc_app_1(x: int, y: int) -> Dict[str, Any]:
    print('run calc app 1')
    logger.info(f'x = {x}, y = {y}, x + y = {x + y}')

    return {"sum": x + y}


@app.run(run_type='calc_app_2')
def calc_app_2() -> Dict[str, Any]:
    print('run calc app 2')


if __name__ == '__main__':
    calc_app_1(1, 2)