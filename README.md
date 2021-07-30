Ansible Keepalived role
=========

Ansible role to install Keepalived on Debian/Red Hat OS family.


Requirements
------------
None

Role Variables
--------------

* `mode` describes the operating mode the sync daemons. Has two value:
  - master-master - all nodes have master role. Default
  - master-backup - only one node has master role.
* `vip` List of VIP adresses of the cluster.
* `vrrp_pass` Password for accessing vrrpd. Only the first eight (8) characters are used
* `interface` interface for inside_network, bound by vrrp

Example Playbook
----------------
Example of setup MASTERs on two nodes cluster with IP 10.0.0.1-2 and VIP 10.0.0.3-4.

```yaml
---
- name: Install keepalived
  hosts: proxy
  remote_user: vagrant
  become: true
  roles:
    - artem-shestakov.keepalived
  vars:
    vip:
      - 10.0.0.3
      - 10.0.0.4
    vrrp_pass: password
    interface: eth1

```
Inventory file:
```ini
[proxy]
10.0.3.1
10.0.3.2
```

License
-------
BSD, MIT


Author Information
------------------
Artem Shestakov (artem.s.shestakov@gmail.com)
