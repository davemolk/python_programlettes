import environ
env = environ.Env()
environ.Env.read_env()

client_id = env("client_id")
client_secret = env("client_secret")

