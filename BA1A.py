#Compute the Number of Times a Pattern Appears in a Text

def compute (text, pattern):
    count = 0
    for i in range (len(text)-len(pattern)+1):
        if (text[i: i+len(pattern)]) == pattern:
            count += 1
    return count

if __name__ == '__main__':
    import sys
    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    text = inlines[0]
    pattern = inlines[1]

    result = compute(text, pattern)

    sys.stdout.write(str(result))