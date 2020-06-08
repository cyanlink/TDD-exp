from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://github.com/cyanlink/TDD-exp.git'


def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('virtualenv', 'TDD-exp/superlists'):
        run(f'mkdir -p {site_folder}')


def _get_latest_source(site_folder):
    if exists(site_folder+'/TDD-exp/.git'):
        run(f'cd {site_folder + "/TDD-exp"} && git fetch')
    else:
        run(f'git clone {REPO_URL} {site_folder + "/TDD-exp"}')


def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/superlists/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS =.+$',
        f'ALLOWED_HOSTS = ["{site_name}"]')
    secret_key_file = source_folder + "superlists/secret_key.py"
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopgrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, f'SECRET_KEY = "{key}"')
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')

def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run(f'python3 -m venv {virtualenv_folder}')
    run(f'{virtualenv_folder}/bin/pip install -r {source_folder}/requirements')

def _update_static_files(source_folder):
    run(
        f'cd {source_folder}'
        '&& ../virtualenv/bin/python manage.py collectstatic --noinput'
    )

def _update_database(source_folder):
    run(
        f'cd {source_folder}'
        '&& ../virtualenv/bin/python3 manage.py migrate --noinput'
    )

def deploy():
    site_folder = f'/root/sites/{env.host}'
    source_folder = site_folder + '/TDD-exp/superlists'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)


