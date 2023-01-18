Ansible Keepalived role
=========

Ansible role to install Keepalived on Debian/Red Hat OS family.


Requirements
------------
None

Inventory Variables
--------------

* `interface` interface for inside_network, bound by vrrp

Role Variables
--------------

* `mode` describes the operating mode the sync daemons. Has two value `master-master` or `master-backup`. Now work only `master-master`.
* `vip` List of VIP adresses of the cluster.
* `global_defs`:
  - `notification_email` - List of emails to notify from `Keepalived`.
  - `notification_email_from` - Email from address that will be in the header.
  - `smtp_server` - Remote SMTP server used to send notification email.
  - `smtp_connect_timeout` - SMTP server connection timeout in seconds.
* `vrrp_instance`
  -  `authentication`
      - `auth_type` - PASS - Simple password (suggested). AH - IPSEC (not recommended)). Default `PASS`.
      - `auth_pass` - Password for accessing vrrpd. Only the first eight (8) characters are used. If `auth_pass` has not specified, `authentication` will be missing.
* `vrrp_script` - dictionary describe tracking script (programs that Keepalived runs at regular intervals)
  - `script` - Checking script.
  - `name` - Name of tracking script
  - `interval` - How ofen run checking script, in seconds. Default: 10 sec
  - `fall` - The number of non-zero attempts befor enter FAULT state. Default: 3
  - `rise` - The number of zero attempts befor exit FAULT state. Default: 3
  - `timeout` - How many time wait up for script before assuming non-zero exit code. Default: 5 sec
  - `weight` - Reduce priority by this value on fall. Default: 10


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
      - 10.0.3.33
      - 10.0.3.34
    vrrp_pass: password
    global_defs:
      notification_email:
        - artem.s.shestakov@gmail.com
      notification_email_from: keepalive@example.com
      smtp_server: 127.0.0.1
      smtp_connect_timeout: 60
    vrrp_instance:
      authentication:
        auth_type: PASS
        auth_pass: password

```
Inventory file:
```ini
[proxy]
10.0.3.31 interface=eth1
10.0.3.32 interface=enp0s8
```

License
-------
BSD, MIT


Author Information
------------------
Artem Shestakov (artem.s.shestakov@gmail.com)
