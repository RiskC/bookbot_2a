from stats import word_counter, char_counter, chars_dict_to_sorted_list
import sys

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

def print_report(file_path, word_count, char_list):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	
	for char in char_list:
		if char[0].isalpha():
			print(f"{char[0]}: {char[1]}")
	
	print("============= END ===============")





def main():
	
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)



	
	file_path = sys.argv[1] 	
	text = get_book_text(file_path)
	word_count = word_counter(text)
	char_count = char_counter(text)
	char_list = chars_dict_to_sorted_list(char_count)
	
	
		

	print_report(file_path, word_count, char_list)



main()
