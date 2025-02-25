# nohup ./run.sh > output.log 2>&1 &

python dataProcess.py
python dataTrain.py
python dataAnalysis.py