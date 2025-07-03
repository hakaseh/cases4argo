N=10 # to-do better to read from generate_ensemble_yaml.py
seq -f "%04g" 1 $N | parallel -j 8 'eat-gotm gotm_{}.yaml --output_id _{}'
