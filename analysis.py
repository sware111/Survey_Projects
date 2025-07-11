import re

def generate_report(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT rate, recommend, opinion FROM responses")
        results = cur.fetchall()

    total = len(results)
    if total == 0:
        print("There is no answer.")
        return

    avg_rate = sum(row[0] for row in results) / total
    recommend_yes = sum(1 for row in results if row[1])
    all_text = " ".join(row[2] for row in results if row[2])

    words = re.findall(r'\b\w+\b', all_text.lower())
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]

    print("\n📊 Report:")
    print(f"Number of responses: {total}")
    print(f"Average score: {avg_rate:.2f}")
    print(f"Number of bidders: {recommend_yes}")
    print("Most frequent words:", top_words)

