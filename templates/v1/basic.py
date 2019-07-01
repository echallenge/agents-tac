#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Baseline agent, ready to run."""

import argparse
import logging

from tac.agents.v1.examples.baseline import BaselineAgent

logger = logging.getLogger(__name__)


def parse_arguments():
    """Arguments parsing."""
    parser = argparse.ArgumentParser("baseline_agent", description="Launch my agent.")
    parser.add_argument("--name", default="my_baseline_agent", help="Name of the agent.")
    parser.add_argument("--oef-addr", default="127.0.0.1", help="TCP/IP address of the OEF Agent")
    parser.add_argument("--oef-port", default=10000, help="TCP/IP port of the OEF Agent")
    parser.add_argument("--gui", action="store_true", help="Show the GUI.")

    return parser.parse_args()


def main():
    """Run the script."""
    args = parse_arguments()
    agent = BaselineAgent(name=args.name, oef_addr=args.oef_addr, oef_port=args.oef_port)

    agent.connect()
    agent.search_for_tac()

    logger.debug("Running baseline agent...")
    agent.run()


if __name__ == '__main__':
    main()
