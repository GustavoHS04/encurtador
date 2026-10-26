
import ipaddress


NOMES_PROIBIDOS = {"localhost"}

def host_proibido(host: str) -> bool:
    host = host.lower().strip().strip("[]").rstrip(".")

    if host in NOMES_PROIBIDOS:
        return True

    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return False

    return ip.is_loopback or ip.is_unspecified
