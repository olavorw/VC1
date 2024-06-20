import pyaudio

def list_audio_devices():
    p = pyaudio.PyAudio()
    device_count = p.get_device_count()
    for i in range(device_count):
        device_info = p.get_device_info_by_index(i)
        print(f"Device {i}: {device_info['name']} (Input channels: {device_info['maxInputChannels']}, Output channels: {device_info['maxOutputChannels']})")
    p.terminate()

# List all audio devices
list_audio_devices()
