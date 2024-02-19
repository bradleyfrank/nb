# Linux

#cron #desktop #filesystem #firewall #mounts #networking #packages #selinux

## Notes

```sh
# extract initrd files
lz4 -d initrd.img initrd.cpio
mkdir initrd
cp initrd.cpio initrd/
cd initrd/
cpio -id < initrd.cpio
```

### cron

```sh
run-parts --report --test /etc/cron.daily  # test cronjobs
```

### Desktop

```sh
gvfs-mime --set x-scheme-handler/https google-chrome.desktop  # set default app

# show desktop session (wayland/x11)
loginctl show-session $(awk '/tty/ {print $1}' <(loginctl)) -p Type | awk -F= '{print $2}'
echo $XDG_SESSION_TYPE

# nVidia "night mode" fix for Linux
cat << EOL >> /etc/X11/xorg.conf.d/20-nvidia.conf
Section "Device"
  Option "UseNvKmsCompositionPipeline" "false"
EndSection
EOL
```

### Filesystems

```sh
parted -s /dev/sdX mklabel GPT  # new partition table
parted -s /dev/sdX mkpart primary 1M 100%  # ensures partition is properly aligned (1M = 2048s)
parted -s /dev/sdX set 1 [raid|lvm] on  # mark partition for raid (mdadm) or lvm

mdadm -Cv /dev/md/<name> /dev/sdX1 /dev/sdY1 --level=1 --raid-devices=2  # create new array

pvcreate /path/to/device  # create physical volume on array or disk partition
vgcreate <vg> /dev/md/<name>  # create volume group
lvcreate -L <num>G -n <lv> <vg>  # create logical volume with specific size
lvcreate -l 100%FREE -n <lv> <vg>  # create logical volume with percent size
vgextend <vg> /path/to/disk  # extend volume group
lvextend -L +<num>G /dev/mapper/<lv>  # extend logical volume

mkfs -t xfs -n ftype=1 /path/to/volume  # format for Docker
mkfs -t xfs /dev/mapper/<vg>-<lv>  # format logical volume

# extend & grow
resize2fs /dev/device
xfs_growfs /dev/device

# repair filesystem
xfs_repair -L /dev/device

# remove filesystem
wipefs -a /dev/device
```

### Firewall

```sh
systemctl enable --now firewalld
firewall-cmd --permanent --add-service=http --add-service=https --add-service=ssh
firewall-cmd --permanent --add-port=2222/tcp
firewall-cmd --reload
```

### Mounts

```sh
mount -t nfs -o options server:/remote/export /local/directory
mount -o loop /path/to/image.iso /local/directory
systemd-escape --path --suffix=mount /nfs/Media  # nfs-Media.mount
```

### Networking

```sh
# find ip address
ip -4 -o addr show | grep -Ev '\blo\b' | grep -Po 'inet \K[\d.]+'
ip -4 -o addr show | grep -Po 'inet \K[\d.]+'
```

```sh
# Remove pre-existing configs
sudo rm /etc/netplan/00-installer-config*

# Install static config
cat << EOF | sudo tee /etc/netplan/00-home.conf
network:
  ethernets:
    $(ip --brief -4 address show | grep -E '^e[n|m]' | awk '{print $1}'):
      dhcp4: no
      addresses: [192.168.1.10/24]
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses: [192.168.1.1]
  version: 2
  renderer: NetworkManager
EOF
```

### Package Management

```sh
yum repository-packages <repo> list installed  # list installed pkgs from repo
yum --disablerepo="*" --enablerepo="<repo>" list available  # query available pkgs from repo
needs-restarting | grep -E '^[0-9]+'  # list services that need restarting
yum install -y --downloadonly <package> --downloaddir=/root/  # download pkgs to directory
yum check-update  # list pkgs that need updating

# Red Hat Subscription Manager
subscription-manager clean
subscription-manager register --org=<org_id> --activationkey=<key_name> --force
subscription-manager config --rhsm.manage_repos=0
subscription-manager status

# firmware updates
fwupdmgr get-updates
fwupdmgr update

# remove snap packages and prevent snap installations
apt-get install gnome-software
apt-get remove gnome-software-plugin-snap
apt-get remove --purge snapd
apt-mark hold snap
apt-mark hold snapd

# upgrade Fedora
dnf upgrade --refresh
dnf install dnf-plugin-system-upgrade
dnf system-upgrade download --releasever=<version>
dnf system-upgrade reboot

# nix
nix-env -f channel:nixpkgs-unstable -iA <package>
```

### SELinux

```sh
getenforce  # show status
getsebool [-a|$boolean]
sestatus

setenforce [enforcing|permissive]  # enable/disable
semanage boolean -l  # list all booleans
semanage boolean -m --off httpd_ssi_exec  # enable/disable
semanage fcontext -l  # list contexts
semanage fcontext -a -t sshd_key_t '/etc/ssh/keys(/.*)?'
restorecon -r /etc/ssh/keys
semanage port -l  # list ports
semanage port -a -t http_cache_port_t -p tcp <port>
semanage port -a -t ssh_port_t -p tcp <port>
```
