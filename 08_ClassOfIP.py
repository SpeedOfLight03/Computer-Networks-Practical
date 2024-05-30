def identify_ip_class(ip_address):
    first_octet = int(ip_address.split('.')[0])

    if 1 <= first_octet <= 126:
        return 'Class A'
    elif 128 <= first_octet <= 191:
        return 'Class B'
    elif 192 <= first_octet <= 223:
        return 'Class C'
    elif 224 <= first_octet <= 239:
        return 'Class D'
    elif 240 <= first_octet <= 255:
        return 'Class E'
    else:
        return 'Invalid IP Address'

def main():
    ip_address = input("Enter the IP address in dotted decimal format (e.g., 192.168.1.1): ")

    ip_class = identify_ip_class(ip_address)
    print(f"The IP address {ip_address} belongs to {ip_class}")

if __name__ == "__main__":
    main()