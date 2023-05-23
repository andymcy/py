def check_id_valid(id_number):
    id_str = str(id_number)
    multiplied_digits = [int(id_str[i]) * (1 if i % 2 != 0 else 2) for i in range(len(id_str))]
    summed_digits = [sum(divmod(num, 10)) if num > 9 else num for num in multiplied_digits]
    total_sum = sum(summed_digits)
    return total_sum % 10 == 0

class IDIterator:
    def __init__(self, id_number):
        self.id_number = id_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.id_number == 999999999:
            raise StopIteration
        self.id_number += 1
        while not check_id_valid(self.id_number):
            self.id_number += 1
        return self.id_number

def id_generator(id_number):
    while id_number < 999999999:
        id_number += 1
        while not check_id_valid(id_number):
            id_number += 1
        yield id_number

def main():
    id_number = int(input("Enter ID: "))
    iterator_or_generator = input("Enter 'it' for iterator or 'gen' for generator: ")

    if iterator_or_generator == "it":
        iterator = IDIterator(id_number)
        for _ in range(10):
            try:
                print(next(iterator))
            except StopIteration:
                print("End of ID range.")
                break
    elif iterator_or_generator == "gen":
        generator = id_generator(id_number)
        for _ in range(10):
            try:
                print(next(generator))
            except StopIteration:
                print("End of ID range.")
                break
    else:
        print("Invalid input. Please enter 'it' or 'gen'.")

if __name__ == '__main__':
    main()
