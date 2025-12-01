import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import pyttsx3
import speech_recognition as sr
import requests
import hashlib
from .advanced_language_engine import AdvancedLanguageEngine

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.RequestError:
            return "Speech recognition service unavailable."

def share_data(data, server_url="https://httpbin.org/post"):  # Placeholder server
    # Anonymize data
    hashed = hashlib.sha256(json.dumps(data).encode()).hexdigest()
    payload = {"hash": hashed, "type": "agi_processing"}
    try:
        response = requests.post(server_url, json=payload)
        print(f"Shared data: {response.status_code}")
    except Exception as e:
        print(f"Share failed: {e}")

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/process':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                body = json.loads(post_data.decode('utf-8'))
                input_text = body.get('input', '')
                opts = body.get('options', {})
                engine = AdvancedLanguageEngine()
                result = engine.process_language(input_text, opts)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(result).encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def serve(port: int = 8080):
    server = HTTPServer(('localhost', port), RequestHandler)
    print(f'[Seraphina AGI] HTTP API listening on {port} (POST /process)')
    server.serve_forever()

def main():
    parser = argparse.ArgumentParser(description='Seraphina AGI Companion')
    parser.add_argument('command', choices=['serve', 'process', 'voice'], help='Command to run')
    parser.add_argument('--port', type=int, default=8080, help='Port for serve')
    parser.add_argument('--input', help='Input text for process')
    parser.add_argument('--voice', action='store_true', help='Use voice for input/output')
    parser.add_argument('--share', action='store_true', help='Share anonymized data for collective learning')

    args = parser.parse_args()

    if args.command == 'serve':
        serve(args.port)
    elif args.command == 'process':
        if args.voice:
            input_text = listen()
            print(f"You said: {input_text}")
        elif not args.input:
            print('Error: --input required for process (or use --voice)')
            return
        else:
            input_text = args.input
        
        engine = AdvancedLanguageEngine()
        result = engine.process_language(input_text)
        output_text = json.dumps(result, indent=2)
        print(output_text)
        if args.voice:
            speak(f"Processed: {result.get('translated_content', 'Done')}")
        if args.share:
            share_data(result)
    elif args.command == 'voice':
        print("Voice chat mode. Say 'exit' to quit.")
        while True:
            input_text = listen()
            print(f"You: {input_text}")
            if 'exit' in input_text.lower():
                speak("Goodbye!")
                break
            engine = AdvancedLanguageEngine()
            result = engine.process_language(input_text)
            response = result.get('translated_content', 'Processed')
            print(f"AGI: {response}")
            speak(response)
            if args.share:
                share_data(result)

if __name__ == '__main__':
    main()