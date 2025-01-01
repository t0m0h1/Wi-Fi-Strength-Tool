import pywifi
from pywifi import const
import time

# Only available on Windows

def get_wifi_signal_strength():
    try:
        # Create a Wi-Fi object
        wifi = pywifi.PyWiFi()
        interfaces = wifi.interfaces()
        if not interfaces:
            print("No Wi-Fi interfaces found.")
            return
        
        iface = interfaces[0]  # Use the first Wi-Fi interface
        iface.scan()  # Start a scan
        
        # Wait for the scan to complete
        time.sleep(2)
        
        # Get scan results
        scan_results = iface.scan_results()
        
        if not scan_results:
            print("No Wi-Fi networks found.")
            return

        print(f"{'SSID':<30}{'Signal Strength (dBm)':<20}")
        print("-" * 50)

        for network in scan_results:
            ssid = network.ssid or "Hidden Network"
            signal_strength = network.signal
            print(f"{ssid:<30}{signal_strength:<20}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_wifi_signal_strength()
