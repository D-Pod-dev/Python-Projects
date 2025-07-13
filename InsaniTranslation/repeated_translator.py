import os
import googletrans as gt
from random import shuffle

def select_file_name(original_text: str):
    file_name = original_text.lower()
    file_name = ''.join(c for c in file_name if c.isalnum() or c.isspace())
    file_name = file_name.replace(" ", "_")
    
    file_instance = 0
    while os.path.exists(f"{file_name}.translation_chain({file_instance}).txt"):
        file_instance += 1
    
    return f"{file_name}.translation_chain({file_instance}).txt"

def run_translation_chain(original_text: str):
    text = original_text
    langs = list(gt.LANGUAGES.keys())
    shuffle(langs)
    langs += ['en']
    progress = 0.0

    translation_chain = select_file_name(original_text)

    with open(f"{translation_chain}", "w", encoding="utf-8") as translation_chain:
        translation_chain.write(f"Original text: '{original_text}'\n")

        for l in range(len(langs)):
            lang = gt.LANGUAGES[langs[l]]
            lang = lang.capitalize()
            text = gt.Translator().translate(text, dest=lang).text # type: ignore
            meaning = gt.Translator().translate(text, dest='en').text # type: ignore
            
            translation_chain.write(
                f"\n({progress:05.2f}%) {lang}{' ' * (21 - len(lang))}: '{meaning}' | ('{text}')")
            translation_chain.flush()

            progress = round((l+1)/len(langs)*100, 2)
            remaining = 100 - progress
            print(f"{progress:05.2f}% done | "
                f"[{'█'*(round(progress/5))+'░'*(round(remaining/5))}]", end="\r")
#            print(f"{progress:05.2f}% done | "
#               f"[{'='*(round(progress/5))+'-'*(round(remaining/5))}]", end="\r")

        translation_chain.write(f"'{original_text}' = '{text}'")

    return text

os.system('cls')
print("Welcome to InsaniTranslation!")
print("-"*40)
original_text = input("Enter text to crazy-translate: ")
print("Hold tight, this may take a minute...")
print()
text = run_translation_chain(original_text)
print("\a")
print("\n"
      "According to the translation:"
      "\n\n"
      f'"{original_text}" = "{text}"'
      "\n")
