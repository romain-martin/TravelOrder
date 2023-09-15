import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def transcribe_audio(path):
    # use the audio file as the audio source
    r = sr.Recognizer()
    #r.adjust_for_ambient_noise(source, duration=1)
    r.energy_threshold = 2000
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        # try converting it to text
        text = r.recognize_sphinx(audio_listened, "fr-FR")
    return text

def get_large_audio_transcription_on_silence(path):
    """Splitting the large audio file into chunks
        and apply speech recognition on each of these chunks"""
    # open the audio file using pydub
    sound = AudioSegment.from_file(path)
    # split audio sound where silence is 500 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=400,
                              # adjust this per requirement
                              silence_thresh=sound.dBFS -14,#- 14,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=400,
                              )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        try:
            text = transcribe_audio(chunk_filename)
        except sr.UnknownValueError as e:
            print("Error:", str(e))
        else:
            text = f"{text.capitalize()}. "
            print(chunk_filename, ":", text)
            whole_text += text
    # return the text for all chunks detected
    return whole_text

def get_text_from_mic(duration):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Recognizing...")
        audio_data = r.record(source, duration=duration)
        # convert speech to text
        text = r.recognize_sphinx(audio_data, "fr-FR")
        print(text)

def main (mode, input=None, duration=None):
    if (mode == "input"):
        if(input):
            _ = get_large_audio_transcription_on_silence(input)
        else:
            print("Missing input file")
    else:
        if(duration):
            get_text_from_mic(duration)
        else:
            print("Missing duration")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', default='all', nargs='?', choices=['input','mic'] , required=True,
                        help='mode to use')
    parser.add_argument('--input',
                        help='the path to audio file')
    parser.add_argument('--duration', type=float,
                        help='the duration of the recording')
    args = parser.parse_args()
    if args.mode is not None:
        main(args.mode, args.input, args.duration)
    else:
        print("Error: Missing argument")