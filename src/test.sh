#!/bin/bash

$expected_output = "Hello, Ahmed1!"

$output=$(python ./src/main.py)

if [ "$output" == "$expected_output" ]; then
    echo "Test passed!"
else
    echo "Test failed! Expected '$expected_output' but got '$output'."
    exit 1
fi