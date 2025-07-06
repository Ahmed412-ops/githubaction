#!/bin/bash

expected_output="Hello, Ahmed3!"
output=$(python ./src/main.py | tr -d '\n')

if [ "$output" = "$expected_output" ]; then
    echo "Test passed!"
else
    echo "Test failed! Expected '$expected_output' but got '$output'."
    exit 1
fi
