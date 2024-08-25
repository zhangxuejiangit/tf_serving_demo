curl -d '{"instances": [1.0, 2.0, 5.0]}'  -X POST http://localhost:8501/v1/models/zxj_half_plus_two:predict

curl -d '{"instances": [1.0, 2.0, 5.0]}'  -X POST http://localhost:8501/v1/models/zxj_half_plus_three:predict
