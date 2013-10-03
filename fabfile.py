from fabric.api import env, local, settings, abort, run, cd

env.hosts = ['myserver1', 'myserver2']


def test():
    local('bin/django test')


def deploy():
    code_dir = '/var/www/pyconza/'

    with cd(code_dir):
        run('git pull')
        run('bin/buildout -vN')
        run('bin/django migrate')
