#!/opt/stackstorm/st2/bin/python
# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

from oslo_config import cfg

from st2common import config
from st2common import log as logging
from st2common.script_setup import setup as common_setup
from st2common.script_setup import teardown as common_teardown
from st2common.util.virtualenvs import setup_pack_virtualenv

__all__ = [
    'main'
]

LOG = logging.getLogger(__name__)

cfg.CONF.register_cli_opt(cfg.StrOpt('pack', default=None))

def main():
    common_setup(config=config, setup_db=False, register_mq_exchanges=False)
    setup_pack_virtualenv(cfg.CONF.pack, logger=LOG)
    common_teardown()

if __name__ == '__main__':
    sys.exit(main())
