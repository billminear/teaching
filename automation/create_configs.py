import os
import yaml

from jinja2 import Environment, FileSystemLoader

DEVICE_FILE = "devices.yaml"
TEMPLATE_DIRECTORY = "./"
OUTPUT_DIRECTORY = "./configs"

with open(DEVICE_FILE, "r") as device_filehandle:
    devices = yaml.safe_load(device_filehandle)

jinja_environment = Environment(
    loader=FileSystemLoader(TEMPLATE_DIRECTORY), trim_blocks=True, lstrip_blocks=True
)

if not os.path.isdir(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)

for device in devices:

    device_filename = f"{device['hostname']}.config"
    output_file_path = os.path.join(OUTPUT_DIRECTORY, device_filename)

    jinja_template_name = f"{device['type']}.j2"
    jinja_template = jinja_environment.get_template(jinja_template_name)

    with open(output_file_path, "w") as output_file:
        output_file.write(jinja_template.render(device=device))
