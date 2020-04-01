import random

'''
    1024 * 1024 * 1024 / 12 
'''

LINES = 1024 * 1024 * 1024 / 12
print(int(LINES))


def generate_data(file_obj):
    for _ in range(0, int(LINES)):
        data = "{} {} {} \n".format(''.join(random.sample("abcdefghijklmnopqrstuvwxyxz", 5)),
                                    random.randint(10, 99),
                                    random.randint(10000, 99999))
        file_obj.write(data)


if __name__ == "__main__":
    with open("/tmp/prac_for_sort.txt", "w+") as f:
        generate_data(f)
