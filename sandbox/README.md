# Sandbox

This folder lets you run the sandbox for the competition.

## 1. Getting Started

- Before getting started, check that:

  - [x] You have followed the steps under 'Dependencies' and 'Preliminaries' on root readme.
  - [x] You are connected to the internet (to pull the latest docker images).
  - [x] Your terminal is in the folder (`cd sandbox`).

- Then, ensure that the sandbox has been built:

```
docker-compose build
```

- In case you experience an error run:

```
docker-compose build --no-cache
```

## 2. Configuration

To configure the execution of TAC, you can tune the following parameters:
- `NB_AGENTS` is the minimum number of agents required for the competition to start.
- `NB_GOODS` is the number of types of goods available for trade in the competition.
- `NB_BASELINE_AGENTS` is the number of baseline agents spawned in the TAC instance. 
- `OEF_ADDR` and `OEF_PORT` allow you to specify a different OEF Node to use for the sandbox. 
- `DATA_OUTPUT_DIR` is the output directory to use for storing simulation data in `${DATA_OUTPUT_DIR}/${EXPERIMENT_ID}`.
- `EXPERIMENT_ID` is the name to give to the simulation.
- `LOWER_BOUND_FACTOR` is the lower bound factor of a uniform distribution used for generating good instances.
- `UPPER_BOUND_FACTOR` is the upper bound factor of a uniform distribution used for generating good instances.
- `TX_FEE` is the transaction fee.
- `REGISTRATION_TIMEOUT` is the amount of time (in seconds) to wait for agents to register before attempting to start the competition.
- `INACTIVITY_TIMEOUT` is the amount of time (in seconds) to wait during inactivity until the termination of the competition.
- `COMPETITION_TIMEOUT` is the amount of time (in seconds) to wait from the start of the competition until the termination of the competition.
- `SEED` is the seed for the random module.
- `WHITELIST` is the public keys permitted by the controller for the competition.
- `REGISTER_AS` indicates whether the baseline agent registers supply, demand or both services on the oef.
- `SEARCH_FOR` indicates whether the baseline agent searches supply, demand or both services on the oef.
- `PENDING_TRANSACTION_TIMEOUT` is the amount of time an in-flight transaction is kept in the transaction manager.

Specify the values in the [`.env`](.env) file.

To double-check whether the variable has been set successfully, use:

    docker-compose config

## 3. Run the sandbox:

There are three ways to run the sandbox:
- with baseline agents only
- with baseline agents and your own agents
- multiple times

### Run TAC with baseline agents only

To run a TAC instance with only baseline agents, set `NB_AGENTS` equal to `NB_BASELINE_AGENTS`.
`REGISTRATION_TIME` should be high enough (e.g. 5-10 seconds) to allow all the baseline agents to register to TAC.
    
Notice: if `NB_AGENTS` > `NB_BASELINE_AGENTS`, there are not enough agents to start the TAC.

- Start the sandbox (this starts an OEF-Node, a controller agent and a list of `NB_BASELINE_AGENTS` baseline agents):

      docker-compose up

### Run TAC with baseline agents and your own agent implementation(s)

If you want to include your own agents, set `NB_AGENTS` to a number equal to `NB_BASELINE_AGENTS` plus the number of own agents you want to connect.  

- Start the sandbox (this starts an OEF-Node, a controller agent and a list of `NB_BASELINE_AGENTS` baseline agents):

      docker-compose up
      
- Connect your agents to `localhost:10000`, e.g.:
```
python ../templates/v1/*.py
```

Be careful with the values of `NB_AGENTS` and `NB_BASELINE_AGENTS`:
- if `NB_AGENTS` <= `NB_BASELINE_AGENTS`, the competition might start even though you didn't register your agent;
- if  `NB_AGENTS` > `NB_BASELINE_AGENTS`, the competition start until `NB_AGENTS` = `NB_BASELINE_AGENTS` agents to start. If you're planning to run only one of your own agents, the difference should be just `1`, e.g. `NB_AGENTS=10` and `NB_BASELINE_AGENTS=9`. 

### Run sandbox multiple times

To run the sandbox multiple times, use the script `run_iterated_games.py`:

    python run_iterated_games.py --config config.json

Usage:
```
usage: run_iterated_games [-h] [--nb_games NB_GAMES] [--output_dir OUTPUT_DIR]
                          [--seeds SEEDS [SEEDS ...]] [--skip]
                          [--interval INTERVAL] [--config CONFIG]

Run the sandbox multiple times and collect scores for every run.

optional arguments:
  -h, --help            show this help message and exit
  --nb_games NB_GAMES   How many times the competition must be run.
  --output_dir OUTPUT_DIR
                        The directory that will contain all the data for every
                        game.
  --seeds SEEDS [SEEDS ...]
                        The list of seeds to use for different games.
  --skip                Don't ask to user for continuation.
  --interval INTERVAL   The minimum number of minutes to wait for the next
                        TAC.E.g. if 5, and the time is 09:00, then the next
                        competition will start at 09:05:00.
  --config CONFIG       The path for a config file (in JSON format). If None,
                        use only command line arguments. The config file
                        overrides the command line options.

```

The script will run the sandbox `nb_games` times with the configuration variables set in `.env`.

The only ignored variables are `DATA_OUTPUT_DIR`, `EXPERIMENT_ID` and `SEEDS`. The first is set with `--output_dir`,
the second will be `game_01` for the first game, `game_02` for the second and so on, the third is set via `--seeds` for
every game.


## 4. Visualization:

To see realtime data visualization, connect to the Visdom server at `http://localhost:8097`.
