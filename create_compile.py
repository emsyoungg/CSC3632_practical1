import os

def compile_attacks(directory, output_file):
    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    with open(os.path.join(root, file), 'r') as infile:
                        outfile.write(infile.read() + '\n\n')

if __name__ == "__main__":
    directory = '/home/student/CSC3632_practical1'  # Replace with the path to your repository
    output_file = 'Compile.md'
    compile_attacks(directory, output_file)
    print(f"All attack descriptions have been compiled into {output_file}")
