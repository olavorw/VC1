import pyaudio
import wave

# Define the parameters for the virtual microphone stream
sample_rate = 44100  # Sample rate in Hz
channels = 1         # Mono audio
frames_per_buffer = 1024  # Number of frames per buffer
output_file = 'output.wav'  # Output file path

# Create a PortAudio instance
p = pyaudio.PyAudio()

# Open a stream for the virtual microphone
stream = p.open(format=pyaudio.paInt16,
                 channels=channels,
                 rate=sample_rate,
                 input=True,
                 frames_per_buffer=frames_per_buffer)

# Open a WAV file for writing
wf = wave.open(output_file, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(sample_rate)

# Read audio from the stream and write it to the WAV file
try:
    while True:
        data = stream.read(frames_per_buffer)
        wf.writeframes(data)
except KeyboardInterrupt:
    pass

# Close the stream, WAV file, and terminate PortAudio
stream.stop_stream()
stream.close()
p.terminate()
wf.close()

print(f"Audio recorded and saved to {output_file}")
