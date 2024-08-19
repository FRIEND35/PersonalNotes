mkdir /rescue
echo "Disk:"
read disk

mount $disk /rescue
mount -t proc proc /rescue/proc
mount -t sysfs sys /rescue/sys
mount -o bind /dev /rescue/dev
mount -t devpts pts /rescue/dev/pts
chroot /rescue

