def file_statistics(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            
            if not path.lower().endswith('.txt'):
                raise ValueError(f"Path {path} is not a text file")

            line_count = 0
            word_count = 0
            characters_count = 0
            digit_count = 0

            for line in file:
                line_count += 1
                word_count += len(line.split())
                characters_count += len(line)
                digit_count += sum(c.isdigit() for c in line)
        
        print("--------------------")
        print(f"Statistics of file {path}:")
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {characters_count}")
        print(f"Number of digits: {digit_count}")
        print("--------------------")

    except FileNotFoundError:
        raise OSError(f"Path {path} does not exist")
    except Exception as e:
        raise e

file_statistics('ex1_2.txt')
