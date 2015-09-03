dd if=/dev/zero of=/swap/swapfile bs=$((1024 * 1024)) count=3072
mkswap /swap/swapfile
swapon /swap/swapfile
