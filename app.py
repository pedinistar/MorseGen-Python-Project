MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.',
    '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '!': '-.-.--', '@': '.--.-.', ' ': '/'
}

from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

def convert_to_text(code):
  # Reversing the dictionary to get morse code as keys and characters as values
  TEXT_TO_MORSE = {v: k for k, v in MORSE_CODE_DICT.items()}

  morse_words = code.split(' ')
  words_list = []

  for morse_word in morse_words:
    if morse_word in TEXT_TO_MORSE:
      words_list.append(TEXT_TO_MORSE[morse_word])

  return ''.join(words_list)


def convert_to_morse(txt):
  txt = txt.upper()
  morse_list = []

  for letter in txt:
    if letter in MORSE_CODE_DICT:
      morse_list.append(MORSE_CODE_DICT[letter])

  return ' '.join(morse_list)


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/generator', methods=['GET','POST'])
def generator():
  if request.method == 'POST':
    text = request.form.get('text')
    morse_code = convert_to_morse(text)
    return render_template('generator.html', code=morse_code)
  return render_template('generator.html')

@app.route('/translator', methods=['GET','POST'])
def translator():
  if request.method == 'POST':
    mcode = request.form.get('mcode')
    text = convert_to_text(mcode)
    return render_template('translator.html', text=text)
  return render_template('translator.html')


if __name__=="__main__":
  app.run(debug=True)
