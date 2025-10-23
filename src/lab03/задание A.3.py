from collections import Counter

def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not freq:
        return []
    
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_items[:n]

def test_count_freq_top_n():
    
    tokens1 = ["a", "b", "a", "c", "b", "a"]
    freq1 = count_freq(tokens1)
    expected_freq1 = {"a": 3, "b": 2, "c": 1}
    print(f"Тест 1 (count_freq): {freq1} == {expected_freq1} -> {freq1 == expected_freq1}")
    
    top2 = top_n(freq1, n=2)
    expected_top2 = [("a", 3), ("b", 2)]
    print(f"Тест 2 (top_n): {top2} == {expected_top2} -> {top2 == expected_top2}")
    
    tokens3 = ["bb", "aa", "bb", "aa", "cc"]
    freq3 = count_freq(tokens3)
    expected_freq3 = {"aa": 2, "bb": 2, "cc": 1}
    print(f"Тест 3 (count_freq): {freq3} == {expected_freq3} -> {freq3 == expected_freq3}")
    
    top4 = top_n(freq3, n=2)
    expected_top4 = [("aa", 2), ("bb", 2)]  
    print(f"Тест 4 (top_n): {top4} == {expected_top4} -> {top4 == expected_top4}")
    
    top5 = top_n(freq1, n=10)
    expected_top5 = [("a", 3), ("b", 2), ("c", 1)]
    print(f"Тест 5 (top_n): {top5} == {expected_top5} -> {top5 == expected_top5}")
    
    freq6 = count_freq([])
    expected_freq6 = {}
    print(f"Тест 6 (count_freq): {freq6} == {expected_freq6} -> {freq6 == expected_freq6}")
    
    top7 = top_n({}, n=5)
    expected_top7 = []
    print(f"Тест 7 (top_n): {top7} == {expected_top7} -> {top7 == expected_top7}")
    
    top8 = top_n(freq1, n=0)
    expected_top8 = []
    print(f"Тест 8 (top_n): {top8} == {expected_top8} -> {top8 == expected_top8}")

def test_integration():

    print("\nИнтеграционный тест (полный pipeline):")
    
    tokens = ["привет", "мир", "привет", "всем", "мир", "прекрасен"]
    print(f"Токены: {tokens}")
    
    freq = count_freq(tokens)
    print(f"Частоты: {freq}")
    
    top_words = top_n(freq, n=3)
    print(f"Топ-3 слов: {top_words}")

if __name__ == "__main__":
    test_count_freq_top_n()
    test_integration()