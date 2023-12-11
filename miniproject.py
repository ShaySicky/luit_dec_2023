import random
import string

def generate_unique_names(num_instances, department_name):
    unique_names = []
    for _ in range(num_instances):
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        unique_name = f"{department_name}_{random_chars}"
        unique_names.append(unique_name)
    return unique_names

if __name__ == "__main__":
    num_instances = int(input("Enter the number of EC2 instances you want names for: "))
    department_name = input("Enter the name of your department: ")

    unique_names = generate_unique_names(num_instances, department_name)

    print("\nGenerated Unique Names:")
    for name in unique_names:
        print(name)
