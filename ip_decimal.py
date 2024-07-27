import sys

def banner():
    print("IP Address to Decimal Converter")
    print("Converts an IPv4 address to its decimal representation.")
    print("Usage: python script.py <IP_ADDRESS>")
    print("Example: python script.py 152.199.21.175")

def ip_to_decimal(ip):
    octets = ip.split('.')
    decimal = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])
    return decimal

if __name__ == "__main__":
    if len(sys.argv) != 2:
        banner()
        sys.exit(1)

    ip_address = sys.argv[1]
    decimal_representation = ip_to_decimal(ip_address)
    print(decimal_representation)





