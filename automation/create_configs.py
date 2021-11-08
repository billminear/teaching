import yaml

from jinja2 import Environment, FileSystemLoader

# remove when complete.
from pprint import pprint

DEVICE_FILE = "devices.yaml"
TEMPLATE_DIRECTORY = "./"
# ROUTER_TEMPLATE = "router_template.j2"
# SWITCH_TEMPLATE = "switch_template.j2"

with open(DEVICE_FILE, "r") as device_filehandle:
    devices = yaml.safe_load(device_filehandle)

jinja_environment = Environment(
    loader=FileSystemLoader(TEMPLATE_DIRECTORY), trim_blocks=True, lstrip_blocks=True
)

for device in devices:

    jinja_template_name = f"{device['type']}.j2"
    jinja_template = jinja_environment.get_template(jinja_template_name)

    print(jinja_template.render(device=device))
