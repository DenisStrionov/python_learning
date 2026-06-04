scores = [50, 75, 90, 40, 100, 65]

good_scores = list(filter(lambda x: x >= 60, scores))

print("Хорошие результаты: ")
print(good_scores)