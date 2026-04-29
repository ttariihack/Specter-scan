import random

def generate_wordlist(domain: str, base_wordlist: str):
    with open(base_wordlist, "r") as f:
        words = [line.strip() for line in f if line.strip()]
    # Simple AI-like mutation: add domain-specific prefixes/suffixes
    mutations = [f"{w}-{domain.split('.')[0]}" for w in words[:50]]
    enhanced = words + mutations + random.sample(words, min(100, len(words)))
    tmp_file = "specterscan/wordlists/ai_generated.txt"
    with open(tmp_file, "w") as f:
        for w in enhanced:
            f.write(w + "\n")
    return tmp_file
