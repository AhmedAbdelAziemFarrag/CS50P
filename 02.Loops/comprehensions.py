def main():
    counts = {}
    words = get_words("address.txt")
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1 
            
    save_counts(counts)
    

def get_words(text):
    

def save_counts(n):
    
    

main()