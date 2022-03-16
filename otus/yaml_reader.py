import yaml

config = yaml.load(open('config.yaml'), Loader=yaml.Loader)
print(config)

