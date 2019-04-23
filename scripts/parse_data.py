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

"""Parse game data generated by the examples."""

import argparse
import json
import pprint
from typing import Dict, Any

from tac.game import Game
from tac.stats import GameStats


def parse_arguments():
    parser = argparse.ArgumentParser("parse_data", description="Parse a data dump.")

    parser.add_argument("filepath", type=str, help="The path to the file of the experiment (JSON).")
    return parser.parse_args()


def read_data(filepath: str) -> Dict[str, Any]:
    with open(filepath) as f:
        data = json.load(f)

    return data


if __name__ == '__main__':
    arguments = parse_arguments()
    filepath = arguments.filepath

    data = read_data(filepath)
    game = Game.from_dict(data)

    pprint.pprint(data)
    for g in game.game_states:
        print(str(g))

    game_stats = GameStats(game)
    game_stats.plot_score_history()
