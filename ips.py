import ipaddress

ip = '192.168.0.1'
endereço = ipaddress.ip_address(ip)
print(endereço)

ip = '192.168.0.100/32'
network = ipaddress.ip_network(ip, strict=False)
print(network)

# imprime todos os ips da rede
for ip in network:
    print(ip)