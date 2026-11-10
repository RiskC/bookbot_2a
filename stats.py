def word_counter(file_contents):
	book = file_contents.split()
	book_word_count = len(book)
	return book_word_count

def char_counter(file_contents):
	chars = {}
	book_lc = file_contents.lower()
	
	for char in book_lc:
		if char not in chars:
			chars[char] = 0
		chars[char] += 1

	return chars

def sort_on(char_count: tuple[str, int]) -> int:
	return char_count[1]


def chars_dict_to_sorted_list(chars: dict[str, int]) -> list[tuple[str,int]]:
	char_list = []
	
	for char in chars:
		char_list.append((char, chars[char]))
	
	return sorted(char_list, reverse=True, key=sort_on)

	
	
