'''
config_create.py
author: Bill Minear

Generates configs for CIT labs using data found in YAML files which represent
the desired state of the lab devices.
'''
import os
import yaml

from jinja2 import Environment, FileSystemLoader

# modify for current lab.
lab_directory = 'lab_02'

# setting up the jinja environment.
template_directory = os.path.join(lab_directory, 'templates') # should generalize this.
configuration_yaml_file = os.path.join(lab_directory, 'configuration.yaml')
env = Environment(loader=FileSystemLoader(template_directory), trim_blocks=True, lstrip_blocks=True)

config_directory = os.path.join(lab_directory, 'configs')
if not os.path.exists(config_directory):
	os.makedirs(config_directory)

with open(configuration_yaml_file,'r') as configuration_yaml:
	configurations = yaml.safe_load(configuration_yaml)

p = input('Enter secret to use for devices: ')
for configuration in configurations:

	j2_template = f"{configuration['device_type']}.j2"
	template = env.get_template(j2_template)

	# set filename as hostname and create path string.
	filename = configuration['hostname'] + '.txt'
	file_path = os.path.join(config_directory, filename)

	# print(template.render(device=configuration, key=p))
	with open(file_path, 'w') as config_file:
		print(f'Storing {file_path}.')
		config_file.write(template.render(device=configuration, key=p))
