cd ..

# taskset -ca 0-35 python run.py \
#     --dir /data2/alessandro/pgpe/ \
#     --ite 1250 \
#     --alg pgpe \
#     --var 1 \
#     --pol linear \
#     --env ip \
#     --horizon 200 \
#     --gamma 1.0 \
#     --lr 0.01 \
#     --lr_strategy adam \
#     --n_workers 36 \
#     --batch 100 \
#     --clip 0 \
#     --n_trials 5

taskset -ca 0-35 python run.py \
    --dir /data2/alessandro/pgpe/ \
    --ite 5000 \
    --alg pgpe \
    --var 0.25 \
    --pol linear \
    --env swimmer \
    --horizon 200 \
    --gamma 1.0 \
    --lr 0.01 \
    --lr_strategy adam \
    --n_workers 36 \
    --batch 100 \
    --clip 0 \
    --n_trials 5

# taskset -ca 0-35 python run.py \
#     --dir /data2/alessandro/pgpe/ \
#     --ite 1250 \
#     --alg pgpe \
#     --var 0.0016 \
#     --pol linear \
#     --env ip \
#     --horizon 200 \
#     --gamma 1.0 \
#     --lr 0.01 \
#     --lr_strategy adam \
#     --n_workers 36 \
#     --batch 100 \
#     --clip 0 \
#     --n_trials 5

# taskset -ca 0-35 python run.py \
#     --dir /data2/alessandro/pg/ \
#     --ite 5000 \
#     --alg pg \
#     --var 1 \
#     --pol linear \
#     --env swimmer \
#     --horizon 200 \
#     --gamma 1.0 \
#     --lr 0.01 \
#     --lr_strategy adam \
#     --n_workers 36 \
#     --batch 100 \
#     --clip 0 \
#     --n_trials 5

taskset -ca 0-35 python run.py \
    --dir /data2/alessandro/pg/ \
    --ite 5000 \
    --alg pg \
    --var 0.25 \
    --pol linear \
    --env swimmer \
    --horizon 200 \
    --gamma 1.0 \
    --lr 0.003 \
    --lr_strategy adam \
    --n_workers 36 \
    --batch 100 \
    --clip 0 \
    --n_trials 5

taskset -ca 0-35 python run.py \
    --dir /data2/alessandro/pg/ \
    --ite 5000 \
    --alg pg \
    --var 0.0016 \
    --pol linear \
    --env swimmer \
    --horizon 200 \
    --gamma 1.0 \
    --lr 0.003 \
    --lr_strategy adam \
    --n_workers 36 \
    --batch 100 \
    --clip 0 \
    --n_trials 5