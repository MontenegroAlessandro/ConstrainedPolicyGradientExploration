cd ..
python3 run.py --dir /Users/ale/PyProjects/results/lqr/pg/ --ite 3000 --alg pg --var 0.0001 --pol linear --env lqr --horizon 50 --gamma 1 --lr 1e-2 --lr_strategy adam --n_workers 8 --batch 100 --lqr_state_dim 7 --lqr_action_dim 7 --n_trials 3
python3 run.py --dir /Users/ale/PyProjects/results/lqr/pgpe/ --ite 3000 --alg pgpe --var 0.001 --pol linear --env lqr --horizon 50 --gamma 1 --lr 1e-2 --lr_strategy adam --n_workers 8 --batch 100 --lqr_state_dim 7 --lqr_action_dim 7 --n_trials 3