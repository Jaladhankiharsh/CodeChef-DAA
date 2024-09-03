def max_pairs(s):
    n = len(s)
    pairs = 0
    i = 0
    while i < n - 1:
        if (s[i] == 'x' and s[i + 1] == 'y') or (s[i] == 'y' and s[i + 1] == 'x'):
            pairs += 1
            i += 2  # Skip the next character as it's already paired
        else:
            i += 1
    return pairs

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        s = data[i]
        results.append(max_pairs(s))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
