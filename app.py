import pywifi 
from pywifi import const


def get_wifi_signal_strength():
    # Create a Wi-Fi object
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Use the first Wi-Fi interface

    # Scan for available Wi-Fi networks
    iface.scan()
    scan_results = iface.scan_results()

    print(f"{'SSID':<30}{'Signal Strength (dBm)':<20}")
    print("-" * 50)

    for network in scan_results:
        ssid = network.ssid
        signal_strength = network.signal
        print(f"{ssid:<30}{signal_strength:<20}")

if __name__ == "__main__":
    get_wifi_signal_strength()
