cd ..
python3 run.py --dir /home/paxmile/results/dpg/ --ite 2000 --alg dpg --var $1 --pol linear --env half_cheetah --horizon 100 --gamma 1 --lr 1e-5 --lr_strategy constant --batch 100 --n_workers 15 --clip 1 --n_trials 5
# python3 run.py --dir /Users/ale/Desktop/dpg/ --ite 2000 --alg dpg --var $1 --pol linear --env half_cheetah --horizon 100 --gamma 1 --lr 1e-5 --lr_strategy constant --batch 100 --n_workers 8 --clip 1 --n_trials 1