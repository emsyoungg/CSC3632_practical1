#!/bin/bash
output_file="Compile.md"
echo "# Compiled Cyber Attacks" > $output_file
for file in $(find . -name "*.md"); do
    cat $file >> $output_file
    echo -e "\n" >> $output_file
done
