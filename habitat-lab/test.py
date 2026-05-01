import habitat

config = habitat.get_config(
    "/mnt/d/ml/habitat-lab/habitat-lab/configs/tasks/pointnav.yaml"
)

env = habitat.Env(config=config)

obs = env.reset()
print(obs.keys())