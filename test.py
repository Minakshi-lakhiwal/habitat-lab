import habitat

config = habitat.get_config(
    "habitat-lab/habitat/config/benchmark/nav/pointnav/pointnav_habitat_test.yaml"
)

env = habitat.Env(config=config)

obs = env.reset()

print("Observation keys:", obs.keys())