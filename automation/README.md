### Configuration Generation Example

The files in this repository are an example of using
Python, Jinja2, and YAML to create Cisco configurations.

I've intended for this to be a simple example where the
goal is to introduce these three technologies and how
they can be applied to improve configuration
generation. 

#### Environment Requirements

- Python 3
- Jinja2 library
- git (if you'd like to clone the repository)

#### Usage
I recommend setting up and activating a Python virtual
environment prior to working through this; however,
I don't have time right now to provide examples on
how to do so.

- Clone repository.
```sh
git clone https://github.com/billminear/educational.git
````
- Change to the "automation" directory.
```sh
cd automation
````
- Install required libraries using requirements.txt.
```sh
pip3 install -r requirements.txt
````
- Modify .yaml and .j2 files as needed.
- Run create_configs.py.
```sh
py create_configs.py
````
- Output files are stored in a "configs" directory
  in the directory where create_configs.py was ran.
- Open files and copy the contents.
- Paste the contents into an appropriate device's CLI. 
