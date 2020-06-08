from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run

REPO_URL = 'https://github.com/cyanlink/TDD-exp.git'

def deploy():
    site_folder = f'/root/sites/{env.host}'
    source_folder = site_folder + '/TDD-exp'
    _create_directory_structure_if_necessary(site_folder)
    