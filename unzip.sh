for file in *; do
    if [ -f "$file" ]; then
        if [[ "$file" == *".zip" ]]; then
            unzip $file
        fi
    fi
done