import os
import sys

print("Enter multiline text below. When you're done, start a new line and \
press Ctrl-Z if on Windows or Ctrl-D if on Mac/Linux, followed by Enter.\n")

text = sys.stdin.read()
os.system('cls')
print("\n".join(text.split("\n")[::-1])[1:])
print("-"*40)

"""
import sys

print("Paste your multiline text below and press Ctrl+D (Linux/macOS) or Ctrl+Z + Enter (Windows) when done:")
text = sys.stdin.read()  # Reads everything at once
reversed_text = "\n".join(text.splitlines()[::-1])  # Splits into lines & reverses

print("\nReversed Output:\n" + reversed_text)

"""
