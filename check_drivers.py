import pyaudio
import wave

def play_sound(file_path, device_index):
    try:
        # Open the sound file
        wf = wave.open(file_path, 'rb')

        # Ensure the audio file has 1 channel (mono)
        if wf.getnchannels() != 1:
            print(f"Audio file is not mono. Converting to mono...")
            mono_wave_file = 'mono_' + file_path
            convert_to_mono(file_path, mono_wave_file)
            wf = wave.open(mono_wave_file, 'rb')

        # Instantiate PyAudio
        p = pyaudio.PyAudio()

        # Print device info for debugging
        device_info = p.get_device_info_by_index(device_index)
        print(fdevice_info)

        # Open a stream with the virtual microphone as the output device
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        output_device_index=device_index)

        # Read data in chunks and play
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        # Stop and close the stream
        stream.stop_stream()
        stream.close()

        # Close PyAudio
        p.terminate()
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_to_mono(input_file, output_file):
    with wave.open(input_file, 'rb') as infile:
        params = infile.getparams()
        frames = infile.readframes(params.nframes)

        with wave.open(output_file, 'wb') as outfile:
            outfile.setnchannels(1)
            outfile.setsampwidth(params.sampwidth)
            outfile.setframerate(params.framerate)
            # Average the two channels to create mono
            if params.nchannels == 2:
                mono_frames = bytearray()
                for i in range(0, len(frames), 2 * params.sampwidth):
                    left_channel = int.from_bytes(frames[i:i + params.sampwidth], 'little', signed=True)
                    right_channel = int.from_bytes(frames[i + params.sampwidth:i + 2 * params.sampwidth], 'little', signed=True)
                    mono_sample = ((left_channel + right_channel) // 2).to_bytes(params.sampwidth, 'little', signed=True)
                    mono_frames.extend(mono_sample)
                outfile.writeframes(mono_frames)
            else:
                outfile.writeframes(frames)

# Example usage
play_sound('test.wav', 63)  # Replace with the correct device index
