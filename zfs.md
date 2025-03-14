# ZFS

## Tags

#zfs #filesystem

## Notes

```sh
lsblk -o NAME,WWN

zpool create -f tank \
  mirror \
    ata-Hitachi_HDS5C3020ALA632_ML4220F316DDPK \
    ata-Hitachi_HDS5C3020ALA632_ML4220F317KSSK \
  mirror \
    ata-HGST_HUS724040ALA640_PN1334PBJWZZGS \
    ata-HGST_HDN724040ALE640_PK2338P4H4Y7AC

zfs create tank/parent1 [-m /path/to/mountpoint -o quota=<num>G]
zfs create tank/parent1/child1

zpool list
zpool status
```

### Replace Disk

```sh
zpool status <POOL>
zpool offline <POOL> <WWN>

parted -s /dev/sdX mklabel GPT
parted -s /dev/sdX mkpart 0% 100%

lsblk -o NAME,WWN
zpool replace <POOL> <OLD-WWN> <NEW-WWN>
```
