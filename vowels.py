def count_vowels(word):

	if not isinstance(word, str):
		print("please provide a valid word")

	else:
		count = 0
		vowels = ["a","e","i","o","u"]

		for char in word:
			if char in vowels:
				count += 1

		return count


