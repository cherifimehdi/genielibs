"""Common configure functions for dhcp"""
# Python
import logging

# Unicon
from unicon.core.errors import SubCommandFailure

log = logging.getLogger(__name__)


def create_dhcp_pool(
    device, pool_name, network, mask, router_id,lease_days,lease_hrs,lease_mins
):
    """ Create DHCP pool
        Args:
            device ('obj'): device to use
            pool_name ('str'): name of the pool to be created
            network ('str'): IP of the network pool
            mask ('str'): Subnet mask of the network pool
            router_id ('str'): Default router ID
        Returns:
            None
        Raises:
            SubCommandFailure: Failed creating dhcp pool
    """
    log.info(
        "Configuring DHCP pool with name={}, network={}, mask={}, and "
        "Router ID {} Lease Time days={},hrs={},mins={}".format(pool_name, network, mask, router_id,lease_days,lease_hrs,lease_mins)
    )

    try:
        device.configure(
            [
            "ip dhcp pool {}".format(pool_name),
	    "network {} {}".format(network,mask),
            "default-router {}".format(router_id),
            "lease {} {} {}".format(lease_days,lease_hrs,lease_mins)
            ]
        )

    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not configure DHCP pool {pool_name}".format(
                pool_name=pool_name
            )
        )

def remove_dhcp_pool(
    device, pool_name
):
    """ Remove DHCP pool
        Args:
            device ('obj'): device to use
            pool_name ('str'): name of the pool to be created
        Returns:
            None
        Raises:
            SubCommandFailure: Failed removing dhcp pool
    """
    log.info(
        "Removing DHCP pool with name={}".format(pool_name)
    )

    try:
        device.configure(
            [
            "no ip dhcp pool {}".format(pool_name),
            ]
        )

    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not remove DHCP pool {pool_name}".format(
                pool_name=pool_name
            )
        )

def enable_dhcp_snooping_glean(device):
    """ Enable DHCP snooping glean globally
        Args:
            device ('obj'): device to use
        Returns:
            None
        Raises:
            SubCommandFailure: Failed configuring DHCP snooping glean
    """
    log.info("Enabling DHCP snooping glean globally")
    try:
        device.configure("ip dhcp snooping glean")
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not enable DHCP snooping glean Error: {error}".format(
                error=e)
        )


def disable_dhcp_snooping_glean(device):
    """ Disable DHCP snooping glean globally
        Args:
            device ('obj'): device to use
        Returns:
            None
        Raises:
            SubCommandFailure: Failed disabling DHCP snooping glean globally
    """
    log.info("Disabling DHCP snooping glean globally")
    try:
        device.configure("no ip dhcp snooping glean")
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not disable DHCP snooping glean globally Error: {error}".format(
                error=e)
        )


def enable_dhcp_snooping_vlan(device, vlan):
    """ Enable DHCP snooping on vlan
        Args:
            device ('obj'): device to use
            vlan ('str'): vlan-id to configure
        Returns:
            None
        Raises:
            SubCommandFailure: Failed configuring DHCP snooping on vlan
    """
    log.info("Enabling DHCP snooping on vlan")
    try:
        device.configure(["ip dhcp snooping vlan {}".format(vlan)])
    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not enable DHCP snooping on vlan {vlan}".format(
                vlan=vlan
            )
        )

def enable_dhcp_snooping(device):
    """ Enable DHCP snooping
        Args:
            device ('obj'): device to use

        Returns:
            None
        Raises:
            SubCommandFailure: Failed configuring DHCP snooping
    """
    log.info("Enabling DHCP snooping")
    try:
        device.configure(["ip dhcp snooping"])
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not enable DHCP snooping, Error: {error}".format(
                error=e)

        )

def disable_dhcp_snooping_vlan(device, vlan):
    """ Disable DHCP snooping on vlan
        Args:
            device ('obj'): device to use
            vlan ('str'): vlan-id to configure
        Returns:
            None
        Raises:
            SubCommandFailure: Failed disabling DHCP snooping on vlan
    """
    log.info("Disabling DHCP snooping on vlan")
    try:
        device.configure(["no ip dhcp snooping vlan {}".format(vlan)])
    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not disable DHCP snooping on vlan {vlan}".format(
                vlan=vlan
            )
        )

def exclude_ip_dhcp(device, ip, high_ip=None):
    """ Exclude IP in DHCP
        Args:
            device ('obj'): device to use
            ip ('str'): ip to exclude
            high_ip ('str', optional): high ip range. Default is None
        Returns:
            None
        Raises:
            SubCommandFailure: Failed excluding IP in DHCP config
    """
    log.info("Excluding IP in DHCP")
    try:
        device.configure([f"ip dhcp excluded-address {ip}{f' {high_ip}' if high_ip else ''}"])
    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not exclude {ip} in DHCP config".format(
                ip=ip
            )
        )

def disable_dhcp_snooping_option_82(device):
    """ Disable DHCP snooping Option 82
        Args:
            device ('obj'): device to use
        Returns:
            None
        Raises:
            SubCommandFailure: Failed disabling DHCP snooping Option 82
    """
    log.info("Disabling DHCP snooping Option 82")
    try:
        device.configure(["no ip dhcp snooping information option"])
    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not disable DHCP snooping Option 82"
            )

def remove_dhcp_snooping_binding(
    device, vlan
):
    """ Remove DHCP snooping binding
        Args:
            device ('obj'): device to use
            vlan ('str'): vlan-id to remove binding
        Returns:
            None
        Raises:
            SubCommandFailure: Failed removing dhcp snooping binding
    """
    log.info(
        "Removing DHCP snooping binding with vlan = {}".format(vlan)
    )

    try:
        device.execute(
            [
            "clear ip dhcp snooping binding vlan {}".format(vlan),
            ]
        )

    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not remove DHCP snooping binding for vlan {vlan}".format(
                vlan = vlan
            )
        )
def enable_ip_dhcp_snooping_trust(device, interface):
    """ Enable DHCP snooping trust on interface
        Configure 'ip dhcp snooping trust' on interface
        Args:
            device ('obj'): device to use
            interface ('str'): interface to configure
        Returns:
            None
        Raises:
            SubCommandFailure: Failed enabling DHCP snooping trust on interface
    """
    log.info("Enabling DHCP snooping trust on interface")
    try:
        device.configure(
            [
             "interface {}".format(interface),
	         "ip dhcp snooping trust",
            ]
        )
    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not enable DHCP snooping trust on interface {interface}".format(
                interface=interface
            )
        )

def enable_dhcp_snooping_option_82(device):
    """ Enable DHCP snooping Option 82
        Args:
            device ('obj'): device to use
        Returns:
            None
        Raises:
            SubCommandFailure: Failed enabling DHCP snooping Option 82
    """
    log.info("Enabling DHCP snooping Option 82")
    try:
        device.configure(["ip dhcp snooping information option"])
    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not enable DHCP snooping Option 82"
            )

def disable_dhcp_snooping(device):
    """ Disable DHCP snooping globally
        Args:
            device ('obj'): device to use
        Returns:
            None
        Raises:
            SubCommandFailure: Failed disabling DHCP snooping globally
    """
    log.info("Disabling DHCP snooping globally")
    try:
        device.configure(["no ip dhcp snooping"])
    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not disable DHCP snooping globally"
            )


def configure_ip_dhcp_snooping_database(device, image='', write_delay=False, delay_time=10):

    """ Configuring ip dhcp snooping database
        Args:
            device ('obj'): device to use
            image ('str',optional): image to use ,defaut is empty string
            write_delay ('bool',optional): True or False ,default is False
            delay_time ('int',optional): delay time ,default is 10
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to configure ip dhcp snooping database
    """

    log.info("Configuring ip dhcp snooping database")

    cmd = "ip dhcp snooping database "

    if write_delay:

        cmd += f"write-delay {delay_time}"

    else:
        cmd += f"{image}"
    try:
        device.configure(
            [
                cmd
            ]
        )

    except SubCommandFailure as e:
        log.error(e)
        raise SubCommandFailure(
            "Failed to configure ip dhcp snooping database")


def unconfigure_ip_dhcp_snooping_database(device, image='', write_delay=False, delay_time=10):

    """ Unconfiguring ip dhcp snooping database
        Args:
            device ('obj'): device to use
            image ('str',optional): image to use ,default is empty string
            write_delay ('bool',optional): True or False ,default is False
            delay_time ('int',optional): time interval ,default is 10
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to configure ip dhcp snooping database
    """

    log.info("Unconfiguring ip dhcp snooping database")

    cmd = f"no ip dhcp snooping database "
    if write_delay:
        cmd += f"write-delay {delay_time}"
    else:
        cmd += f"{image}"
    try:
        device.configure(
            [
                cmd
            ]
        )

    except SubCommandFailure as e:
        log.error(e)
        raise SubCommandFailure(
            "Failed to unconfigure ip dhcp snooping database")


def create_dhcp_pool_withoutrouter(
    device, pool_name, network, mask, lease_days,lease_hrs,lease_mins
):

    """ Create DHCP pool
        Args:
            device ('obj'): device to use
            pool_name ('str'): name of the pool to be created
            network ('str'): IP of the network pool
            mask ('str'): Subnet mask of the network pool
            lease_days ('int'):Parameters for lease days config
            lease_hrs ('int'):Parameters for lease hrs config
            lease_mins ('int'): Parameters for lease mins config
        Returns:
            None
        Raises:
            SubCommandFailure: Failed creating dhcp pool
    """

    log.info(
        "Configuring DHCP pool with name={}, network={}, mask={}, and "
        "Lease Time days={},hrs={},mins={}".format(pool_name, network, mask, lease_days,lease_hrs,lease_mins)
    )

    try:
        device.configure(
            [
            f"ip dhcp pool {pool_name}",
            f"network  {network} {mask}",
            f"lease {lease_days} {lease_hrs} {lease_mins}"
            ]
        )

    except SubCommandFailure as e:

        log.error(e)
        raise SubCommandFailure(
            "Could not configure DHCP pool {pool_name}".format(
                pool_name=pool_name
            )
        )

def unconfigure_ip_dhcp_snooping_verify(device, verify_type):
    """ unconfigure ip dhcp scooping verify on device
        Args:
            device (`obj`): Device object
            verify_type (`str`): verify type (i.e mac-address , no-relay-agent-address)
        Returns:
            None
        Raises:
            SubCommandFailure: Failed unconfiguring dhcp snooping verify on device
    """
    log.debug("unconfiguring ip dhcp scooping verify on device")

    try:
        device.configure(f"no ip dhcp snooping verify {verify_type}")

    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Could not unconfigure ip dhcp scooping verify. Error:\n{e}"
        )

def configure_ip_dhcp_client(device, dhcp_client_type):
    """ Configure ip dhcp client on device
        Args:
            device (`obj`): Device object
            dhcp_client_type (`str`): DHCP client type (i.e broadcast-flag, default-router, forcerenew, network-discovery, update)
        Returns:
            None
        Raises:
            SubCommandFailure : ip dhcp client is not configured
    """
    log.debug("configuring DHCP client on device")

    try:
        device.configure(f"ip dhcp-client {dhcp_client_type}")

    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Could not configure ip DHCP client. Error:\n{e}"
        )
def enable_ip_dhcp_auto_broadcast(device):
    """ Enable ip dhcp auto-broadcast on device
        Args:
            device ('obj'): device to run on
        Returns:
            None
        Raises:
            SubCommandFailure : Failed enabling ip dhcp auto-broadcast on device
    """
    log.debug("Enabling DHCP auto-broadcast on device")

    try:
        device.configure("ip dhcp auto-broadcast")

    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Could not enable DHCP auto-broadcast on device. Error:\n{e}"
        )

def disable_ip_dhcp_auto_broadcast(device):
    """ Disable ip dhcp auto-broadcast on device
        Args:
            device ('obj'): device to run on
        Returns:
            None
        Raises:
            SubCommandFailure : Failed disabling ip dhcp auto-broadcast on device
    """
    log.debug("Disabling DHCP auto-broadcast on device")

    try:
        device.configure("no ip dhcp auto-broadcast")
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Could not disable DHCP auto-broadcast on device. Error:\n{e}"
            )

def configure_ip_dhcp_client_vendor_class(
        device,
        interface,
        type,
        string=None):
    """ Configure IP DHCP Client Vendor-class on interface:
        Args:
            device ('obj'): device to use
            interface ('str'): Interface to configure
            type('str'): vendor-class type (i.e. mac-address, ascii, hex, disable)
            string('str', optional): The value string when type set to ascii or hex
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to configure ip dhcp vendor-class
    """
    log.info(f"Configure ip dhcp client vendor-class {type} on {interface}")
    if type in ['mac-address', 'disable']:
        cmd = f'ip dhcp client vendor-class {type}'

    elif type in ['ascii', 'hex'] and string:
        cmd = f'ip dhcp client vendor-class {type} {string}'

    else:
        raise SubCommandFailure("Invalid vendor-class type or string missing")

    try:
        device.configure([f"interface {interface}", cmd])

    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Failed to configure ip dhcp vendor-class on {interface}. Error:\n{e}")


def unconfigure_ip_dhcp_client_vendor_class(
        device,
        interface,
        type):
    """ Unconfigure IP DHCP Client Vendor-class on interface:
        Args:
            device ('obj'): device to use
            interface ('str'): Interface to configure
            type('str'): vendor-class type (i.e. mac-address, ascii, hex, disable)
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to unconfigure ip dhcp vendor-class
    """
    log.info(f"Unconfigure ip dhcp client vendor-class {type} on {interface}")
    cmd = f'no ip dhcp client vendor-class {type}'
    try:
        device.configure([f"interface {interface}", cmd])

    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Failed to unconfigure ip dhcp vendor-class on {interface}. Error:\n{e}")

def enable_dhcp_smart_relay(device):
    """ Enable dhcp smart-relay on device
        Args:
            device ('obj'): device to run on
        Returns:
            None
        Raises:
            SubCommandFailure : Failed enabling smart-relay on device
    """
    log.debug("Enabling DHCP smart-relay on device")
    try:
        device.configure("ip dhcp smart-relay")
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Could not enable DHCP smart-relay on device. Error:\n{e}"
            )

def disable_dhcp_smart_relay(device):
    """ Disable ip dhcp auto-broadcast on device
        Args:
            device ('obj'): device to run on
        Returns:
            None
        Raises:
            SubCommandFailure : Failed disabling smart-relay on device
    """
    log.debug("Disabling DHCP smart-relay on device")
    try:
        device.configure("no ip dhcp smart-relay")
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Could not disable DHCP smart-relay on device. Error:\n{e}"
            )


def configure_dhcp_relay_information(device):

    """ Enable dhcp relay information on device
        Args:
            device ('obj'): device to run on

        Returns:
            None

        Raises:
            SubCommandFailure : Failed enabling relay information on device
    """
    log.debug("Enabling DHCP relay information on device")
    try:
        device.configure("ip dhcp relay information trust-all")
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Could not enable DHCP relay information on device. Error:\n{e}"
            )

def unconfigure_dhcp_relay_information(device):

    """ Disable dhcp relay information on device
        Args:
            device ('obj'): device to run on

        Returns:
            None

        Raises:
            SubCommandFailure : Failed disabling relay information on device
    """
    log.debug("Disabling DHCP relay information on device")
    try:
        device.configure("no ip dhcp relay information trust-all")
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Could not disable DHCP relay information on device. Error:\n{e}"
            )

def enable_dhcp_relay_information_option(device, vpn=False):
    """ Enable DHCP relay information option
        Args:
            device ('obj'): device to use
            vpn ('str',optional): vpn option ,defaut is empty string
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to enable dhcp relay information option
    """

    cmd = "ip dhcp relay information option"

    if vpn:
        cmd = "ip dhcp relay information option vpn"

    log.info("Enabling ip dhcp relay information option")
    try:
        device.configure(cmd)
    except SubCommandFailure:
        raise SubCommandFailure(
            "Failed to enable ip dhcp relay information option"
        )

def disable_dhcp_relay_information_option(device, vpn=False):
    """ Disable DHCP relay information option
        Args:
            device ('obj'): device to use
            vpn ('str',optional): vpn option ,defaut is empty string
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to disable dhcp relay information option
    """

    cmd = "no ip dhcp relay information option"
    if vpn:

        cmd = "no ip dhcp relay information option vpn"

    log.info("Disabling ip dhcp relay information option")
    try:
        device.configure(cmd)
    except SubCommandFailure:
        raise SubCommandFailure(
            "Failed disable ip dhcp relay information option"
        )

def configure_dhcp_relay_short_lease(device, lease_time, interface=False):
    """ Configure DHCP relay short lease
        Args:
            device ('obj'): device to use
            lease_time ('int'): dhcp lease time
            interface ('str',optional): interface name ,defaut is empty string
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to configure dhcp relay short lease
    """

    cmd = []
    if interface:
        cmd.append(f"interface {interface}")
        cmd.append(f"ip dhcp relay short-lease {lease_time}")
    else:
        cmd.append(f"ip dhcp-relay short-lease {lease_time}")

    log.info("Configuring dhcp relay short lease")
    try:
        device.configure(cmd)
    except SubCommandFailure:
        raise SubCommandFailure(
            "Failed to configure dhcp relay short lease"
        )

def unconfigure_dhcp_relay_short_lease(device, lease_time, interface=False):
    """ Unconfigure DHCP relay short lease
        Args:
            device ('obj'): device to use
            lease_time ('int'): dhcp lease time
            interface ('str',optional): interface name ,defaut is empty string
            lease_time ('int'): dhcp lease time
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to disable dhcp relay short lease
    """

    cmd = []
    if interface:
        cmd.append(f"interface {interface}")
        cmd.append(f"no ip dhcp relay short-lease {lease_time}")
    else:
        cmd.append(f"no ip dhcp-relay short-lease {lease_time}")

    log.info("Unconfiguring dhcp relay short lease")
    try:
        device.configure(cmd)
    except SubCommandFailure:
        raise SubCommandFailure(
            "Failed to unconfigure dhcp relay short lease"
        )


def configure_ip_dhcp_snooping_information_option_allow_untrusted(device, interface):
    """configure ip dhcp snooping information option allow-untrusted on device
        Args:
            device (`obj`): Device object
            interface ('str'): interface to configure
        Returns:
            None
        Raises:
            SubCommandFailure: Failed configuring dhcp snooping information option allow-untrusted on device
    """
    log.info(f"configuring ip dhcp snooping information option allow-untrusted on {interface}")

    config_list = []
    config_list.append(f"interface {interface}")
    config_list.append("ip dhcp snooping information option allow-untrusted")

    try:
        device.configure(config_list)

    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not configure ip dhcp snooping information option allow-untrusted. Error:\n{e}"
        )


def unconfigure_ip_dhcp_snooping_information_option_allow_untrusted(device, interface):
    """ unconfigure ip dhcp snooping information option allow-untrusted on device
        Args:
            device (`obj`): Device object
            interface ('str'): interface to configure
        Returns:
            None
        Raises:
            SubCommandFailure: Failed unconfiguring dhcp snooping information option allow-untrusted on device
    """
    log.info(f"unconfiguring ip dhcp snooping information option allow-untrusted on {interface}")

    config_list = []
    config_list.append(f"interface {interface}")
    config_list.append("no ip dhcp snooping information option allow-untrusted")
    try:
        device.configure(config_list)

    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not unconfigure dhcp snooping information option allow-untrusted. Error:\n{e}"
        )

def configure_ip_dhcp_snooping_information_option(device):
    """Configures dhcp snooping information option on device
       Example: ip dhcp snooping information option

       Args:
            device ('obj'): device object

       Return:
            None

       Raises:
            SubCommandFailure
    """
    log.info("Configuring dhcp snooping information option")
    try:
        device.configure("ip dhcp snooping information option")
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f'Failed to configure dhcp snooping information option on {device.name}\n{e}'
        )

def unconfigure_ip_dhcp_snooping_information_option(device):
    """Unconfigures dhcp snooping information option on device
       Example: no ip dhcp snooping information option

       Args:
            device ('obj'): device object

       Return:
            None

       Raises:
            SubCommandFailure
    """
    log.info("Unconfiguring dhcp snooping information option")
    try:
        device.configure("no ip dhcp snooping information option")
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f'Failed to unconfigure dhcp snooping information option on {device.name}\n{e}'
        )

def configure_ip_dhcp_pool(device, name):
    """Configures dhcp pool on device
       Example: ip dhcp pool POOL_88

       Args:
            device ('obj'): device object
            name ('str'): name of the pool (eg. POOL_88, testpool)

       Return:
            None

       Raises:
            SubCommandFailure
    """
    log.info(f"Configuring dhcp pool {name}")
    try:
        device.configure(f"ip dhcp pool {name}")
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f'Failed to configure dhcp pool {name} on {device.name}\n{e}'
        )

def unconfigure_ip_dhcp_pool(device, name):
    """Unconfigures dhcp pool on device
       Example: no ip dhcp pool POOL_88

       Args:
            device ('obj'): device object
            name ('str'): name of the pool (eg. POOL_88, testpool)

       Return:
            None

       Raises:
            SubCommandFailure
    """
    log.info(f"Unconfiguring dhcp pool {name}")
    try:
        device.configure(f"no ip dhcp pool {name}")
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f'Failed to unconfigure dhcp pool {name} on {device.name}\n{e}'
        )

def configure_dhcp_channel_group_mode(device, interface, group, mode):
    """Configures Ethernet port to an EtherChannel group
       Example: channel-group 120 mode active

       Args:
            device ('obj'): device object
            interface ('str): interface to configure (eg. Gig1/0/1)
            group ('int'): Channel group number. The range is 1 to 128
            mode ('str'): EtherChannel mode (eg. active, passive, auto)

       Return:
            None

       Raises:
            SubCommandFailure
    """
    log.info(f"Configuring DHCP EtherChannel group mode {mode} on {interface}")
    config= [
        f'interface {interface}',
        f'channel-group {group} mode {mode}'
    ]
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f'Failed to configure DHCP channel-group mode {mode} on {interface}\n{e}'
        )

def unconfigure_dhcp_channel_group_mode(device, interface, group, mode):
    """Unconfigures Ethernet port to an EtherChannel group
       Example: no channel-group 120 mode active

       Args:
            device ('obj'): device object
            interface ('str): interface to configure (eg. Gig1/0/1)
            group ('int'): Channel group number. The range is 1 to 128
            mode ('str'): EtherChannel mode (eg. active, passive, auto)

       Return:
            None

       Raises:
            SubCommandFailure
    """
    log.info(f"Unconfiguring DHCP EtherChannel group mode {mode} on {interface}")
    config= [
        f'interface {interface}',
        f'no channel-group {group} mode {mode}'
    ]
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f'Failed to unconfigure DHCP channel-group mode {mode} on {interface}\n{e}'
        )

def configure_cts_manual(device, interface):
    """Configures cts manual on the interface
       Example: cts manual

       Args:
            device ('obj'): device object
            interface ('str): interface to configure (eg. Gig1/0/1, Te1/0/10)

       Return:
            None

       Raises:
            SubCommandFailure
    """
    log.info(f"Configuring cts manual on {interface}")
    config= [
        f'interface {interface}',
        f'cts manual'
    ]
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f'Failed to configure cts manual on {interface} on {device.name}\n{e}'
        )

def unconfigure_ip_dhcp_snooping_trust(device, interface):
    """Unconfigures ip dhcp snooping trust

       Args:
            device ('obj'): device object
            interface ('str'): name of interface

       Return:
            None

       Raises:
            SubCommandFailure
    """
    cmd = [
        f"interface {interface}",
        "no ip dhcp snooping trust"
    ]
    try:
        device.configure(cmd)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f'Failed to unconfigure no ip dhcp snooping trust on {device.name}\n{e}'
        )

def configure_ip_dhcp_pool_host(device, pool_name, host, client_identifier=None,
                                hardware_address=None, client_name=None, **kwargs):
    """ Configure DHCP host pool
        Args:
            device ('obj'): device to use
            pool_name ('str'): name of the pool to be configured
            host ('str'): IP and subnet mask of the DHCP client
            client_identifier ('str'): Unique identifier for client
            hardware_address ('str'): Hardware address of the client
            client_name ('str'): Name of the client
        Returns:
            str: Response of command
        Raises:
            SubCommandFailure: Failed to configure dhcp host pool
    """
    log.info(f"Configuring DHCP host pool {pool_name} for {host}")

    cmd_list = [f"ip dhcp pool {pool_name}",
                f"host {host}"]

    if client_identifier:
        cmd_list.append(f"client-identifier {client_identifier}")
    if hardware_address:
        cmd_list.append(f"hardware-address {hardware_address}")
    if client_name:
        cmd_list.append(f"client-name {client_name}")
    try:
        device.configure(cmd_list, **kwargs)

    except SubCommandFailure as e:
        log.error(e)
        raise SubCommandFailure(
            f"Failed to configure DHCP host pool {pool_name}"
        )

def unconfigure_ip_dhcp_pool_host(device, pool_name, host, client_identifier=None,
                                hardware_address=None, client_name=None, **kwargs):
    """ Unconfigure host from DHCP pool
        Args:
            device ('obj'): device to use
            pool_name ('str'): name of the DHCP pool
            host ('str'): IP and subnet mask of the DHCP client
            client_identifier ('str'): Unique identifier for client
            hardware_address ('str'): Hardware address of the client
            client_name ('str'): Name of the client
        Returns:
            str: Response of command
        Raises:
            SubCommandFailure: Failed to unconfigure host from dhcp pool
    """
    log.info(f"Unconfiguring host {host} from DHCP pool {pool_name}")

    cmd_list = [f"ip dhcp pool {pool_name}",
                f"no host {host}"]

    if client_identifier:
        cmd_list.append(f"no client-identifier {client_identifier}")
    if hardware_address:
        cmd_list.append(f"no hardware-address {hardware_address}")
    if client_name:
        cmd_list.append(f"no client-name {client_name}")
    try:
        device.configure(cmd_list, **kwargs)

    except SubCommandFailure as e:
        log.error(e)
        raise SubCommandFailure(
            f"Failed to uniconfigure host from DHCP pool {pool_name}")

def configure_ip_dhcp_exclude_vrf(device, vrf_name, low_ip_address, high_ip_address):
    """ Configure ip dhcp exclude vrf
        Args:
            device ('obj'): device to use
            vrf_name ('str'): VPN Routing/Forwarding instance name
            low_ip_address ('str'): Low IP address
            high_ip_address ('str'): High IP address
        Returns:
            None
        Raises:
            SubCommandFailure: Failed excluding IP in DHCP config
    """
    log.info("configuring ip dhcp exclude vrf")
    cmd = [f'ip dhcp excluded-address vrf {vrf_name} {low_ip_address} {high_ip_address}']
    try:
        device.configure(cmd)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not exclude ip in DHCP config. Error:\n{e}".format(
                error=e
            )
        )
def configure_ip_dhcp_restrict_next_hop(device, interface, restrict_method):
    """ configure ip dhcp restrict-next-hop on interface
        Configure 'ip dhcp restrict-next-hop' on interface
        Args:
            device ('obj'): device to use
            interface ('str'): interface to configure
            restrict_method('str'): restrict method 'both|cdp|lldp'
        Returns:
            None
        Raises:
            SubCommandFailure: Failed configure ip dhcp restrict-next-hop on interface
    """
    log.info("configure ip dhcp restrict-next-hop on interface")
    try:
        device.configure(
            [
             'interface {}'.format(interface),
             'ip dhcp restrict-next-hop {}'.format(restrict_method),
            ]
        )
    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not configure ip dhcp restrict-next-hop on interface {}".format(interface)
        )
def unconfigure_ip_dhcp_restrict_next_hop(device, interface):
    """ unconfigure ip dhcp restrict-next-hop on interface
        unConfigure 'ip dhcp restrict-next-hop' on interface
        Args:
            device ('obj'): device to use
            interface ('str'): interface to configure
        Returns:
            None
        Raises:
            SubCommandFailure: Failed unconfigure ip dhcp restrict-next-hop on interface
    """
    log.info("unconfigure ip dhcp restrict-next-hop on interface")
    try:
        device.configure(
            [
             "interface {}".format(interface),
	         "no ip dhcp restrict-next-hop",
            ]
        )
    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not unconfigure ip dhcp restrict-next-hop on interface {interface}".format(
                interface=interface
            )
        )
def configure_ip_dhcp_snooping_limit(device, interface, rate_limit):
    """ Configure DHCP snooping limit on interface
        Configure 'ip dhcp snooping limit' on interface
        Args:
            device ('obj'): device to use
            interface ('str'): interface to configure
            rate_limit('int'): DHCP snooping rate limit
        Returns:
            None
        Raises:
            SubCommandFailure: Failed configuring DHCP snooping limit rate on interface
    """
    log.info("Configure DHCP snooping limit rate on interface")
    config = [
             f"interface {interface}",
             f"ip dhcp snooping limit rate {rate_limit}",
            ]
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Could not configure DHCP snooping limit on interface {interface}. Error\n{e}"
            )

def configure_interface_ip_dhcp_relay_information_option_vpn_id(device, interface):
    """ Configure ip dhcp relay information option vpn-id on the interface 
        Args:
            device ('obj'): device to use
            interface ('str'): name of the interface to be configured # example  "interface vlan 100" "ip dhcp relay information option vpn-id"
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to ip dhcp relay information option vpn-id
    """
    log.info("Configuring ip dhcp relay information option vpn-id on the interface")
    config =  ["interface {}".format(interface),
                "ip dhcp relay information option vpn-id"]
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Failed to configure ip dhcp relay information option vpn-id on the interface {interface}. Error\n{e}"
        )

def unconfigure_interface_ip_dhcp_relay_information_option_vpn_id(device, interface):
    """ Unconfigure ip dhcp relay information option vpn-id on the interface # example  "interface vlan 100" "ip dhcp relay information option vpn-id"
        Args:
            device ('obj'): device to use
            interface ('str'): name of the interface to be configured # example  "interface vlan 100" "ip dhcp relay information option vpn-id"
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to enable dhcp relay information option
    """
    log.info("Unconfiguring ip dhcp relay information option vpn-id on the interface")
    config =  ["interface {}".format(interface),
               "no ip dhcp relay information option vpn-id"]
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Failed to unconfigure ip dhcp relay information option vpn-id on the interface {interface}. Error\n{e}"
        )

def configure_interface_ip_dhcp_relay_source_interface_intf_id(device, interface, intf_id):
    """ Configure interface ip dhcp relay source interface intf_id 
        Args:
            device ('obj'): device to use
            interface ('str'): name of the interface to be configured # example  "interface vlan 100" "ip dhcp relay source-interface Loopback1"
            intf_id ('str'): Set source interface for relayed messages for interface ex: Loopback1 interface
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to configure ip dhcp relay source-interface intf_id
    """
    log.info("Configuring ip dhcp relay source-interface intf_id on the interface")
    config = [
                "interface {}".format(interface),
                "ip dhcp relay source-interface {}".format(intf_id)]
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Failed to configure ip dhcp relay source interface intf_id {interface}. Error\n{e}"
        )

def unconfigure_interface_ip_dhcp_relay_source_interface_intf_id(device, interface, intf_id):
    """ UnConfigure interface ip dhcp relay source interface intf_id 
        Args:
            device ('obj'): device to use
            interface ('str'): name of the interface to be configured # example  "interface vlan 100" "no ip dhcp relay source-interface Loopback1"
            intf_id ('str'): Set source interface for relayed messages for interface ex: Loopback1 interface
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to unconfigure ip dhcp relay source-interface intf_id
    """
    log.info("Unconfiguring ip dhcp relay source-interface intf_id on the interface")
    config = [
                "interface {}".format(interface),
                "no ip dhcp relay source-interface {}".format(intf_id)]
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f"Failed to unconfigure ip dhcp relay source interface intf_id {interface}. Error\n{e}"
        )

def configure_dhcp_pool(device, pool_name, router_id=None, network=None, mask=None):
    """ Configure DHCP pool
        Args:
            device ('obj'): device to use
            pool_name ('str'): name of the pool to be created
            router_id ('str', optional): router id to configure default-router. Default is None
            network ('str', optional): IP of the network pool. Default is None
            mask ('str', optional): Subnet mask of the network pool. Default is None
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to configure dhcp pool
    """

    config = [f'ip dhcp pool {pool_name}']
    if router_id:
        config.append(f'default-router {router_id}')
    if network and mask:
        config.append(f'network {network} {mask}')
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(f'Could not configure dhcp pool. Error: {e}')


def unconfigure_dhcp_pool(device, pool_name, router_id=None, network=None, mask=None):
    """ Unconfigure DHCP pool
        Args:
            device ('obj'): device to use
            pool_name ('str'): name of the pool to be created
            router_id ('str', optional): router id to configure default-router. Default is None
            network ('str', optional): IP of the network pool. Default is None
            mask ('str', optional): Subnet mask of the network pool. Default is None
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to configure dhcp pool
    """

    config = [f'ip dhcp pool {pool_name}']
    if router_id:
        config.append(f'no default-router {router_id}')
    if network and mask:
        config.append(f'no network {network} {mask}')

    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(f'Could not unconfigure dhcp pool. Error: {e}')


def configure_service_dhcp(device):
    """ Configure DHCP pool
        Args:
            device ('obj'): device to use
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to configure service dhcp
    """

    config = 'service dhcp'
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(f'Could not configure service dhcp. Error: {e}')


def unconfigure_service_dhcp(device):
    """ Unconfigure DHCP pool
        Args:
            device ('obj'): device to use
        Returns:
            None
        Raises:
            SubCommandFailure: Failed to unconfigure service dhcp
    """

    config = 'no service dhcp'
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(f'Could not unconfigure service dhcp. Error: {e}')


def unconfigure_exclude_ip_dhcp(device, ip, high_ip=None):
    """ Unconfigure Exclude IP in DHCP
        Args:
            device ('obj'): device to use
            ip ('str'): ip to exclude
            high_ip ('str', optional): high ip range. Default is None
        Returns:
            None
        Raises:
            SubCommandFailure: Failed unconfigure exclude IP in DHCP config
    """
    try:
        device.configure([f"no ip dhcp excluded-address {ip}{f' {high_ip}' if high_ip else ''}"])
    except SubCommandFailure:
        raise SubCommandFailure(f"Could not unconfigure exclude {ip} in DHCP config")

def enable_dhcp_compatibility_suboption(device, suboption, value):
    """ Enable DHCP compatibility suboption
        Args:
            device ('obj'): device to use
            suboption ('str'): Link-Selection or Server-id override suboption
            value ('str'): cisco or standard value
        Returns:
            None
        Raises:
            SubCommandFailure
    """

    config = f"ip dhcp compatibility suboption {suboption} {value}"
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(f"Failed to enable DHCP compatibility suboption. Error:\n{e}")

def disable_dhcp_compatibility_suboption(device, suboption):
    """ Disable DHCP compatibility suboption
        Args:
            device ('obj'): device to use
            suboption ('str'): Link-Selection or Server-id override suboption
        Returns:
            None
        Raises:
            SubCommandFailure
    """

    config = f"no ip dhcp compatibility suboption {suboption}"
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(f"Failed to disable DHCP compatibility suboption. Error:\n{e}")

def unconfigure_propagate_sgt(device, interface, type, cts_type):
    """ UnConfigure propagate sgt
       Args:
            device ('obj'): device object
            interface ('str'): interface to configure (eg. Gig1/0/1, Te1/0/10)
            type ('str'):  manual      Supply local configuration for CTS parameters
                           role-based  Role-based Access Control per-port config commands
            cts_type ('str'): policy     CTS policy for manual mode
                              propagate  CTS SGT Propagation configuration for manual mode
                              sap        CTS SAP configuration for manual mode              
       Return:
            None
       Raises:
            SubCommandFailure
    """
    log.info(f"unconfigure propagate sgt on interface")
    config= [
              f'interface {interface}',
              f'cts {type}',
              f'no {cts_type} sgt'
            ]
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f'Failed to unconfigure propagate sgt {interface} on {device.name}\n{e}'
        ) 

def unconfigure_cts_role_based_sgt_map_vlan_list(device, Vlan_id, Tag_value):
    """UnConfigure cts role-based sgt-map vlan-list 300 sgt 300
       Args:
            device ('obj'): device object
            Vlan_list ('int'): <1-4094>  VLAN id
            Tag_value ('int'): <2-65521>  Security Group Tag value
       Return:
            None
       Raises:
            SubCommandFailure
    """
    log.info(f"UnConfigure cts role-based sgt-map vlan-list 300 sgt 300")
    config= [
               f'no cts role-based sgt-map vlan-list {Vlan_id} sgt {Tag_value}'
             ]
    try:
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            f'Failed to unconfigure cts role-based sgt-map vlan-list 300 sgt 300 on {device.name}\n{e}'
        ) 