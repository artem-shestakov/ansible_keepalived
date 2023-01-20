import os
import time
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_service_is_run(host):
    svc = host.service('keepalived')
    assert svc.is_running
    assert svc.is_enabled

def test_ip(host):
    assert host.service('nginx').is_running
    ips = host.interface('eth0').addresses
    assert len(ips) >= 2

def test_ip_migration(host):
    if host.check_output('hostname -s') == 'instance01':
        host.run("systemctl stop nginx")
        for i in range(0,3):
            if len(host.interface('eth0').addresses) != 1 and i != 2:
                time.sleep(3)
                continue
            else:
                assert len(host.interface('eth0').addresses) == 1
    if host.check_output('hostname -s') == 'instance02':
       assert len(host.interface('eth0').addresses) == 3

        