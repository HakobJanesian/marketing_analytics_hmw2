#!/bin/bash

find . -type f -name "*.py" | while read file; do
    echo "Processing $file..."
    pyment "$file"
done

echo "All .py files processed."
