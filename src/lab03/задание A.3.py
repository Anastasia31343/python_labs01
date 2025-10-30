from collections import Counter

def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not freq:
        return []
    
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_items[:n]


    
tokens1 = ["a", "b", "a", "c", "b", "a"]
freq1 = count_freq(tokens1)
print(freq1)
    
top2 = top_n(freq1, n=2)
print(top2)
    
tokens3 = ["bb", "aa", "bb", "aa", "cc"]
freq3 = count_freq(tokens3)
print(freq3)
    
top4 = top_n(freq3, n=2)
print(top4)
    
top5 = top_n(freq1, n=10)
print(top5)
    
freq6 = count_freq([])
print(freq6)
    
top7 = top_n({}, n=5)
print(top7)
    
top8 = top_n(freq1, n=0)
print(top8)
    
tokens = ["привет", "мир", "привет", "всем", "мир", "прекрасен"]
print(tokens)
    
freq = count_freq(tokens)
print(freq)
    
top_words = top_n(freq, n=3)
print(top_words)
