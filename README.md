# marco
Simple Python ping checker. Useful when waiting for devices to become online/offline.

Provide 1 or more hostnames as arguments when running:
```
./marco.py hostname1 hostname2
```

Script will ping hosts every second. If a host goes offline it will log time it was last online.
When a host comes back online, it will log when last offline.
```
bilgtit11: UP Last Offline:NEVER
melba: UP Last Offline:NEVER
```
