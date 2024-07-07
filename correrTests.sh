#!/bin/bash

CONFIG_DIR="./tests"
OUTPUT_DIR="./outputs"

if [ ! -d "$OUTPUT_DIR" ]; then
    mkdir "$OUTPUT_DIR"
fi

CONFIG_FILES=("config1.txt" "config2.txt" "config3.txt" "config4.txt" "config5.txt" "config6.txt" "config7.txt" "config8.txt" "config9.txt" "config10.txt")

for config_file in "${CONFIG_FILES[@]}"; do
    input_file="${CONFIG_DIR}/${config_file}"
    output_file="${OUTPUT_DIR}/output_${config_file}"

    echo "Corriendo con: ${config_file}"
    python3 interface.py "${input_file}" > "${output_file}"
done

echo "Todas las pruebs fueron corridas, revisar directorio de outputs para los resultados"
