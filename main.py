import gifos

t = gifos.Terminal(width=750, height=500, xpad=5, ypad=5)
t.toggle_show_cursor(False)
t.gen_text(text="   Booting `Debian GNU/Linux`", row_num=1)
t.gen_text(text="Loading Linux 6.1.0-21-amd64 ...", row_num=2)
t.gen_text(text="Loading initial ramdisk ...", row_num=3)
t.gen_text("", 1, count=5)
t.clear_frame()
t.gen_text(text="[  \x1b[32mOK\x1b[0m  ] Started github.service - GitHub Service.", row_num=2)
t.gen_text(text="[  \x1b[32mOK\x1b[0m  ] Started polkit.service - Authorization Service.", row_num=3)
t.gen_text(text="[  \x1b[32mOK\x1b[0m  ] Started accounts-daemon.service - Accounts Service.", row_num=4)
t.gen_text(text="[      ] Starting mr00k3.service - mr00k3 Service...", row_num=5, count=5)
t.gen_text(text="[  \x1b[32mOK\x1b[0m  ] Started power-profiles-daemon.service - Power Profiles daemon", row_num=6)
t.gen_text(text="[  \x1b[32mOK\x1b[0m  ] Started udisks2.service - Disk Manager.", row_num=7)
t.gen_text(text="[  \x1b[32mOK\x1b[0m  ] Started NetworkManager.service - Network Manager.", row_num=8)
t.gen_text(text="[  \x1b[32mOK\x1b[0m  ] Reached target network.target - Network.", row_num=9)
t.gen_text(text="[  \x1b[32mOK\x1b[0m  ] Finished openvpn.service - OpenVPN service.", row_num=10)
t.gen_text(text="[  \x1b[32mOK\x1b[0m  ] Finished systemd-user-sessions.service - Permit User Sessions.", row_num=11)
t.gen_text(text="[  \x1b[32mOK\x1b[0m  ] Started apache2.service - Apache2 Service.", row_num=12)
t.gen_text(text="[  \x1b[32mOK\x1b[0m  ] Finished mr00k3.service - mr00k3 Service.", row_num=13, count=5)
t.clear_frame()
t.gen_text(text="Welcome to Debian GNU/Linux 12", row_num=1, count=1)
t.gen_text(text="Kernel 6.1.0-21 on an x86_64 (/dev/tty1)", row_num=2, count=1)
t.toggle_show_cursor(True)
t.gen_text(text="localhost login: ", row_num=4, count=5)
t.gen_typing_text("mr00k3", 4, contin=True)
t.gen_text("", 4, count=10)
t.gen_text(text="Password: ", row_num=5, count=5)
t.gen_text("", 5, count=20)
t.gen_text(text="\x1b[32mmr00k3@localhost\x1b[0m:\x1b[34m~\x1b[0m$ ", row_num=6, count=5)
t.gen_typing_text("python3 mr00k3fetch.py", 6, contin=True)
t.gen_text("", 6, count=10)
t.clear_frame()
t.toggle_show_cursor(False)
t.gen_text(text="    \x1b[30;43m mr00k3@github.com \x1b[0m", row_num=1)
t.gen_text(text="    --------------", row_num=2)
t.gen_text(text="    \x1b[34mOS: \x1b[31mDebian/Ubuntu/Arch/FreeBSD/macOS, Windows 11, Android, iOS\x1b[0m", row_num=3)
t.gen_text(text="    \x1b[34mProjects: \x1b[31mFew opencore efi's, kali dwm, trollsshrd, kde/gnome things, python things\x1b[0m", row_num=4)
t.gen_text(text="    \x1b[34mLanguages: \x1b[31mPython, Shell, a litte of C# and C, HTML/CSS\x1b[0m", row_num=5)
t.gen_text(text="    \x1b[34mIDE: \x1b[31mVSCodium, PyCharm CE, Visual Studio CE, nano\x1b[0m", row_num=6)
t.gen_text(text="    \x1b[34mInterests: \x1b[31mLinux, iOS jailbreak, Android Kernels\ROMs, Cybersecurity, Patodeweloperka\x1b[0m", row_num=7)
t.gen_text(text="", row_num=8)
t.gen_text(text="    \x1b[30;43m Contact: \x1b[0m", row_num=9)
t.gen_text(text="    --------------", row_num=10)
t.gen_text(text="    \x1b[34memail: \x1b[31mmr00k3ziks@protonmail.com\x1b[0m", row_num=11)
t.gen_text(text="    \x1b[34mdiscord: \x1b[31m@mr00k3_dev\x1b[0m", row_num=12)
t.gen_text(text="    \x1b[34mtelegram: \x1b[31m@mr00k3\x1b[0m", row_num=13)
t.gen_text(text="", row_num=14)
t.gen_text(text="    \x1b[30;43m SocialMedia: \x1b[0m", row_num=15)
t.gen_text(text="    --------------", row_num=16)
t.gen_text(text="    \x1b[34mtwitter: \x1b[31m@mr00k3\x1b[0m", row_num=17)
t.gen_text(text="    \x1b[34mmastadon: \x1b[31m@mr00k3@infosec.exchange\x1b[0m", row_num=18)
t.gen_text(text="    \x1b[34minstagram: \x1b[31m@mr00k3\x1b[0m", row_num=19)
t.gen_text(text="    \x1b[34mreddit: \x1b[31mu/mr00k3\x1b[0m", row_num=20)
t.gen_text(text="", row_num=20, count=200)
t.gen_text(text="[3448015.307991] [<ffffffffa0145c3b>] ? :ext3:ext3_ordered_write_end +0x73/0x110", row_num=1, count=4, contin=True)
t.gen_text(text="[3448015.307991] [<ffffffff80265486>] ? generic_file_buffered_write +0x1c0/0x63c", row_num=2, count=4, contin=True)
t.gen_text(text="[3448015.307991] [<ffffffff80231409>] ? current_fs_time +0x1e/0x24", row_num=3, contin=True)
t.clear_frame()
t.gen_text(text="[3448015.307991] [<ffffffffa0145c3b>] ? :ext3:ext3_ordered_write_end +0x73/0x110", row_num=1, count=4)
t.gen_text(text="[3448015.307991] [<ffffffff80265486>] ? generic_file_buffered_write +0x1c0/0x63c", row_num=2, count=4)
t.gen_text(text="[3448015.307991] [<ffffffff80231409>] ? current_fs_time +0x1e/0x24", row_num=3)
t.gen_text(text="[3448015.307991] [<ffffffff80265c41>] ? __generic_file_aio_write_nolock +0x33f/0", row_num=4)
t.gen_text(text="x3a9", row_num=5)
t.gen_text(text="[3448015.307991] [<ffffffff802419a1>] ? hrtimer_wakeup +0x0/0x22", row_num=6)
t.gen_text(text="[3448015.307991] [<ffffffff80265d0c>] ? generic_file_aio_write +0x61/0xc1", row_num=7)
t.gen_text(text="[3448015.307991] [<ffffffffa01422fe>] ? :ext3:ext3_file_write +0x16/0x94", row_num=8)
t.gen_text(text="[3448015.307991] [<ffffffff8028a12f>] ? do_sync_write +0xc9/0x10c", row_num=9)
t.gen_text(text="[3448015.307991] [<ffffffff8023f699>] ? autoremove_wake_function +0x0/0x2e", row_num=10)
t.gen_text(text="[3448015.307991] [<ffffffff80242079>] ? ktime_get_ts +0x22/0x4b", row_num=11)
t.gen_text(text="[3448015.307991] [<ffffffff8028a8d9>] ? vfs_write +0xad/0x156", row_num=12)
t.gen_text(text="[3448015.307991] [<ffffffff8028af64>] ? sys_pwrite64 +0x50/0x70", row_num=13)
t.gen_text(text="[3448015.307991] [<ffffffff8020b528>] ? system_call +0x68/0x6d", row_num=14)
t.gen_text(text="[3448015.307991] [<ffffffff8020b4c0>] ? system_call +0x0/0x6d", row_num=15)
t.gen_text(text="[3448015.307991]", row_num=16)
t.gen_text(text="[3448015.307991]", row_num=17)
t.gen_text(text="[3448015.307991] Code: 30 fa 58 88 4c 39 2c 88 75 84 8f Ob eb fe 48 c7 c8 48 fa ", row_num=18)
t.gen_text(text="58 88 eb 1f 65 48 8b 84 25 18 88 88 88 66 f7 88 44 e8 ff ff 08 ff 75 84 <0f> 0b ", row_num=19)
t.gen_text(text="eb fe 48 c7 c0 30 fa 58 80 48 8d 1c 08 48 83 3b 00 74 04", row_num=20, count=7)
t.gen_text(text="[3448015.307991] RIP  [<ffffffff8037fc7c>] xen_spin_wait+0x90/0x139", row_num=21)
t.gen_text(text="[3448015.307991]  RSP <ffffffff80595e28>", row_num=22)
t.gen_text(text="[3448015.307991] ---[ end trace 604fbc4ae1a5e660 ]---", row_num=23)
t.gen_text(text="[3448015.307991] Kernel panic - not syncing: Aiee, killing interrupt handler!", row_num=24, count=100)
t.gen_gif()