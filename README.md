# teaching resources

Here you'll find resources I utilize for teaching computer networking. You will primarily find resources associated with configuration generation for networking labs in Packet Tracer and on physical hardware as well as resources used to grade configurations.

Feel free to try them out and let me know if you have any questions or thoughts!

## management/create_configs.py
---
This script utilizes YAML to structure the devices in a lab and their desired configurations. It also uses the Jinja2 templating library to generate the configurations for applying to the devices.

## management/config_grader.py
---
This script will compare a configuration text file to a YAML file containing the statements needed to successfully complete a lab. It will then utilize values found associated with each statement in the YAML file to generate a score.

## management/group_generator.py
---
In the event that students need to be grouped together for a lab, this script can be utilized to generate a set of student groupings. Each execution of the script will generate a new set of groupings consisting of randomly assigned pairs.