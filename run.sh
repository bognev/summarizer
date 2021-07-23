#!/bin/bash


#. C:/Users/bognev/Anaconda3/etc/profile.d/conda.sh
# python -m build
#  conda install -c anaconda openpyxl
# pip install openpyxl
# python -m pip install ./waveaccess/dist/summarizer_package-0.1.0.tar.gz


report=0
out="report"
output_type="markdown"

echo "python -u main.py  --report=$report --out=$out --output_type=$output_type"
python -u main.py  --report=$report --out=$out --output_type=$output_type
