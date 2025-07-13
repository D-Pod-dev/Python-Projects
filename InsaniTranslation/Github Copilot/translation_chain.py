from googletrans import Translator
import time
import random

def chain_translate(text, num_translations=5):
    translator = Translator()
    
    # List of language codes to choose from
    languages = ['fr', 'es', 'de', 'it', 'ja', 'ko', 'ru', 'nl', 'pt', 'ar', 'hi']
    current_text = text
    translation_path = ['en']  # Start with English
    
    print(f"Original text: {text}\n")
    print("Translation path:")
    
    for i in range(num_translations):
        # Choose a random language that's different from the last one
        target_lang = random.choice([lang for lang in languages if lang != translation_path[-1]])
        translation_path.append(target_lang)
        
        try:
            # Add a small delay to avoid hitting rate limits
            time.sleep(1)
            translation = translator.translate(current_text, dest=target_lang)
            current_text = translation.text
            print(f"{i + 1}. {translation.src} -> {target_lang}: {current_text}")
        except Exception as e:
            print(f"Error during translation: {e}")
            return None
    
    # Translate back to English
    try:
        time.sleep(1)
        final_translation = translator.translate(current_text, dest='en')
        print(f"\nFinal translation back to English: {final_translation.text}")
        return final_translation.text
    except Exception as e:
        print(f"Error during final translation: {e}")
        return None

def main():
    print("Welcome to the Chain Translator!")
    print("This program will translate your text through multiple languages and back to English.")
    
    while True:
        text = input("\nEnter the text you want to translate (or 'quit' to exit): ")
        if text.lower() == 'quit':
            break
            
        num_translations = input("Enter the number of intermediate translations (default is 5): ")
        num_translations = int(num_translations) if num_translations.isdigit() else 5
        
        result = chain_translate(text, num_translations)
        if result:
            print("\nTranslation chain completed!")

if __name__ == "__main__":
    main()