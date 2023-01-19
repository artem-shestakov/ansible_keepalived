import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_service_is_run(host):
    svc = host.service('keepalived')
    assert svc.is_running
    assert svc.is_enabled

def test_ip(host):
    if host.check_output('hostname -s') == 'instance01' and host.service('nginx').is_running:
        ips = host.interface('eth0').addresses
        assert len(ips) > 2
    elif not host.service('nginx').is_running:
        ips = host.interface('eth0').addresses
        assert len(ips) == 1
