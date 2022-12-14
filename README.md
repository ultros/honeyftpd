# ftpdhoney.py
### Simple FTPD Honeypot for Capturing Credentials

####
    $ sudo python3 ftpdhoney.py
####
    $ cat credentials.txt
    127.0.0.1:user:password
    127.0.0.1:user:user
    127.0.0.1:user:test


### Daemon Skeleton

    [Unit]
    Description=ftpdhoney.py
    After=network.target
    
    [Service]
    Type=simple
    WorkingDirectory=/path/to/ftpdhoney/
    ExecStart=python3.11 ftpdhoney.py
    Restart=always
    
    [Install]
    WantedBy=multi-user.target

### Daemon Setup (Debian)
    # vim /etc/systemd/system/honeyftpd.service (Daemon Skeleton)
    # systemctl daemon-reload
    # systemctl enable honeyftpd.service
    # systemctl start honeyftpd.service
    # systemctl status honeyftpd.service