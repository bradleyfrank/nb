# rsyncnet

#zfs #freebsd #pkg

```
zfs create -o encryption=on -o keyformat=passphrase data1/backups  # make a new encrypted dataset
chsh -s /bin/sh root  # allows compatibility with syncoid output
```

```
pkg update
pkg upgrade
pkg install bash
```


Here is an example zfs command that should give you a starting point:

(from your local zfs system)

```
zfs snapshot pool/name@dump
zfs send pool/name@dump | ssh root@de3481b.rsync.net \
"zfs receive -s data1/newname; zfs destroy data1/newname@dump"
zfs destroy pool/name@dump
```

The first command creates the snapshot you will send to your rsync.net zpool (optional if you already have a snapshot)

The 2nd command sends the snapshot over ssh. Note, the zpool we have created for you is called "data1" so use that and any name you like for your filesystem (we used "newname" above). Also note, we are immediately removing the snapshot on the new filesystem, but you can keep that if you wish.

The 3rd command optionally removes the snapshot you just made for the purposes of sending. If you do not want to or need to remove that snapshot (again, maybe you already had one) you can skip over this step.

AS ALWAYS, you can ask us to write example commands for you or debug your existing commands, etc. - don't spend your time debugging, just have us do it for you.

Some notes:

- Your initial upload of data may be large and time consuming. If your connection breaks you may want the option to resume the transfer. Be sure to use the -s option with your zfs receive to make your upload resume-able. Please contact us if you need help resuming your send.

- You may or may not want to enable filesystem snapshots on your interior zpool - you can do this yourself, or you can just tell us in plain english what you want and we will implement them.

- It is possible that you want NO snapshots enabled on your zpool, since it is possible that snapshots are what you are actually sending us.

- You should ONLY use this interior zpool/login for your zfs send/recv operations. If you have normal "plain old files" data to back up to rsync.net, please contact us to setup a plain storage account for you. You should not store data in your VM outside the zpool.

- No snapshots will be created for the VM or the datastore backing your zpool.

- This email has been sent in clear text, so you should immediately change your password. You can do this from the shell within your account:

passwd root

(and also for Linux: passwd user)

- Your home directory contains a .ssh directory that you can place an authorized_keys (RSA or DSA) file in, which will allow you to interact with your zpool in an automated fashion. There is a detailed HOWTO on this topic here:

https://rsync.net/resources/howto/ssh_keys.html

- Your zpool supports encryption. Even if your sending side is not encrypted, you can encrypt the data you send here. You can read more about that here: https://wiki.archlinux.org/title/ZFS#Native_encryption or feel free to contact us if you want more specific directions.

- If you're sending snapshots from a FreeNAS system using the replication task in the GUI, you will need to symlink the zfs binary in your VM so the replication task will operate properly. Here's the command you will need to run once as root from the shell in your VM:

ln -s /usr/local/sbin/zfs /sbin/zfs

- We are happy to update your OS anytime, please contact us. If you would like to update yourself, please contact us so we can provide specific update instructions.


Again, we are very happy to have you as a customer and look forward to serving you in any way that we can.

Let us know early and often how we can help you get this up and running and off of your to-do list.
