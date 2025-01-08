import pywifi
from pywifi import const
import time
import matplotlib.pyplot as plt

# Only available on Windows

def get_wifi_signal_strength():
    try:
        # Create a Wi-Fi object
        wifi = pywifi.PyWiFi()
        interfaces = wifi.interfaces()
        if not interfaces:
            print("No Wi-Fi interfaces found.")
            return None, None
        
        iface = interfaces[0]  # Use the first Wi-Fi interface
        iface.scan()  # Start a scan
        
        # Wait for the scan to complete
        time.sleep(2)
        
        # Get scan results
        scan_results = iface.scan_results()
        
        if not scan_results:
            print("No Wi-Fi networks found.")
            return None, None

        print(f"{'SSID':<30}{'Signal Strength (dBm)':<20}")
        print("-" * 50)
        print("\n")
        print("Lower the value of DBM, better the signal strength")
        print("\n")

        ssids = []
        signal_strengths = []

        for network in scan_results:
            ssid = network.ssid or "Hidden Network"
            signal_strength = network.signal
            print(f"{ssid:<30}{signal_strength:<20}")
            
            ssids.append(ssid)
            signal_strengths.append(signal_strength)
        
        return ssids, signal_strengths
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
    


def plot_signal_strength(ssids, signal_strengths, max_ssids=20):
    if not ssids or not signal_strengths:
        print("No data available to plot.")
        return

    # Sort by signal strength (optional)
    sorted_data = sorted(zip(ssids, signal_strengths), key=lambda x: x[1], reverse=True)
    sorted_ssids, sorted_strengths = zip(*sorted_data)

    # Limit the number of SSIDs to display
    limited_ssids = sorted_ssids[:max_ssids]
    limited_strengths = sorted_strengths[:max_ssids]

    plt.figure(figsize=(12, 8))
    plt.bar(limited_ssids, limited_strengths, color='skyblue')
    plt.xlabel('SSID')
    plt.ylabel('Signal Strength (dBm)')
    plt.title('Wi-Fi Signal Strength')
    plt.xticks(rotation=45, ha='right')  # Rotate SSID labels for readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()  # Adjust layout to fit labels
    plt.show()




if __name__ == "__main__":
    ssids, signal_strengths = get_wifi_signal_strength()
    plot_signal_strength(ssids, signal_strengths)

