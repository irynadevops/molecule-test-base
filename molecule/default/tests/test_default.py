import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    import os
    import pytest
    import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    ("/etc/ansible/facts.d"),
])
def test_facts_directories(host, name):
    if name:
        d = host.file(name)
        assert d.is_directory
        assert d.exists
    if not name:
        d = host.file(name)
        assert not d.exists


@pytest.mark.parametrize("name", [
    ("/etc/sudoers"),
])
def test_files(host, name):
    assert not host.file(name).contains('requiretty')
    assert host.file(name).is_file


@pytest.mark.parametrize("name", [
    ("httpd"),
])
def test_service(host, name):
    assert host.service(name).is_running
    assert host.service(name).is_enabled


@pytest.mark.parametrize("package", [
    ("epel-release"),
])
def test_required_packages_exist(host, package):
    pkg = host.package(package)
    assert pkg.is_installed


@pytest.mark.parametrize("p", [
    ("Jinja2"),
])
def test_required_pip_packages_exist(host, p):
    assert p in host.pip_package.get_packages()
