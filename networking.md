# Networking

## Notes

```sh
nc -zw1 ports.ubuntu.com 80  # test website/port

# get Apache web server status
curl -Is --max-time 5 https://<domain>/server-status | head -n 1

# capture packets
tcpdump --list-interfaces
tcpdump -i eth0
tcpdump -w my_packet_capture.pcap
```
