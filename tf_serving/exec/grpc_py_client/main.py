import time
import grpc
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc

# 第一步建立通信
channel = grpc.insecure_channel('{host}:{port}'.format(host="127.0.0.1", port=8500))
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

# 第二步生成请求
request = predict_pb2.PredictRequest()
request.model_spec.name = "model"
request.model_spec.signature_name = "serving_default"
# 第三步调用模型服务
input_data = df.to_dict(orient='list')

data_grpc = []
for f, v in input_data.items():
    v = [[i] for i in v]
    request.inputs[f].CopyFrom(tf.make_tensor_proto(v))
data_grpc.append(request)
# 测试 耗时
start_ts = time.time()
for _ in range(1000):
    result = stub.Predict(request, 10)
    # print(result)
print((time.time() - start_ts) / 1000)


