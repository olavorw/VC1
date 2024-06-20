import pyaudio

def query_device_info(device_index):
    p = pyaudio.PyAudio()
    device_info = p.get_device_info_by_index(device_index)
    print(device_info)
    p.terminate()

# Example usage
query_device_info(73)
