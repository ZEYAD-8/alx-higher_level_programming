#!/bin/bash

directory="./"

base_name="-answer"

start_number=0
end_number=28

for ((i=start_number; i<=end_number; i++)); do
    file_name="${directory}${i}${base_name}.txt"
    touch "$file_name"
done

echo "$((end_number - start_number + 1)) files have been created."
