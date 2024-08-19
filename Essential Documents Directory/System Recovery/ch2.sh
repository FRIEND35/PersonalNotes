echo "Disk:"
read disk

mount $disk /mnt
mount --rbind /proc /mnt/proc
mount --rbind /sys /mnt/sys
mount --rbind /dev /mnt/dev
chroot /mnt


