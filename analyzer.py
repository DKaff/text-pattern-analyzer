import re
import sys

def analyze_morphological_density(text_input):
    """Calculates basic token-to-character and affix density metrics for structured text."""
    tokens = re.findall(r'\b\w+\b', text_input)
    total_chars = sum(len(t) for t in tokens)
    token_count = len(tokens)
    
    density_score = total_chars / token_count if token_count > 0 else 0
    return {
        "token_count": token_count,
        "total_characters": total_chars,
        "morphological_density": round(density_score, 4)
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text_data = f.read()
            print(f"--- Analysis for: {file_path} ---")
            print(analyze_morphological_density(text_data))
        except FileNotFoundError:
            print(f"Error: Could not find file '{file_path}'.")
    else:
        user_input = input("Enter text to analyze: ")
        print(analyze_morphological_density(user_input))