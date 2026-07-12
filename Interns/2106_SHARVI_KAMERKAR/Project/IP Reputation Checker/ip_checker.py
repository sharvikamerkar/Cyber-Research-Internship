import ipaddress

def check_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)

        ip_type = "Private" if ip_obj.is_private else "Public"

        report = f"""
IP Reputation Report
--------------------
IP Address : {ip}
Type       : {ip_type}
Version    : IPv{ip_obj.version}
"""

        print(report)

        with open("report.txt", "w") as file:
            file.write(report)

        print("Report generated successfully: report.txt")

    except ValueError:
        print("Invalid IP Address")


# Main Program
ip = input("Enter IP Address: ")
check_ip(ip)