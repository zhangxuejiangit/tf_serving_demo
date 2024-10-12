import time
import grpc
import tensorflow as tf

from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc

# 第一步建立通信
channel = grpc.insecure_channel('{host}:{port}'.format(host="127.0.0.1", port=8500))
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

# 第二步生成请求
request = predict_pb2.PredictRequest()
request.model_spec.name = "ple"
request.model_spec.signature_name = "serving_default"
# 第三步调用模型服务
input_data = {}
input_data["feedback_num_7d"] = [0.0]
input_data["uv_rate_15d"] = [0.0]
input_data["ctr_7d"] = [0.0]
input_data["uv_rate_7d"] = [0.0]
input_data["view_num_sqrt"] = [0.0]
input_data["user_genres_7d"] = [1, 1, 1]
input_data["user_directors_7d"] = [1, 1, 1]
input_data["item_languages"] = [1, 1]
input_data["user_publishers_7d"] = [1, 1, 1]
input_data["view_num_square"] = [0.0]
input_data["uv_rate_30d"] = [0.0]
input_data["view_num_norm"] = [0.0]
input_data["download_num_30d"] = [0.0]
input_data["view_num_15d"] = [0.0]
input_data["streaming_num_15d"] = [0.0]
input_data["feedback_rate_1d"] = [0.0]
input_data["download_rate_1d"] = [0.0]
input_data["item_publisher"] = [1]
input_data["ctr_30d"] = [0.0]
input_data["item_directors"] = [1, 1, 1]
input_data["user_actors_7d"] = [1, 1, 1]
input_data["phone_brand"] = [1]
input_data["feedback_num_1d"] = [0.0]
input_data["ctr_15d"] = [0.0]
input_data["user_languages_7d"] = [1, 1]
input_data["item_id"] = [1]
input_data["view_num_7d"] = [0.0]
input_data["item_actors"] = [1, 1, 1]
input_data["feedback_rate_7d"] = [0.0]
input_data["release_at_log"] = [0.0]
input_data["category"] = [1]
input_data["release_at_sqrt"] = [0.0]
input_data["release_at_norm"] = [0.0]
input_data["avg_playtime_7d"] = [0.0]
input_data["feedback_num_15d"] = [0.0]
input_data["view_num_log"] = [0.0]
input_data["ip_city"] = [1]
input_data["streaming_num_7d"] = [0.0]
input_data["download_num_7d"] = [0.0]
input_data["item_genres"] = [1, 1, 1]
input_data["download_num_1d"] = [0.0]
input_data["user_source"] = [1]
input_data["release_at_square"] = [0.0]
input_data["view_num_30d"] = [0.0]
input_data["streaming_num_1d"] = [0.0]
input_data["avg_playtime_15d"] = [0.0]
input_data["avg_playtime_30d"] = [0.0]
input_data["feedback_rate_30d"] = [0.0]
input_data["phone_model"] = [1]
input_data["ip_state"] = [1]
input_data["entrance"] = [1]
input_data["streaming_num_30d"] = [0.0]
input_data["download_rate_30d"] = [0.0]
input_data["download_rate_7d"] = [0.0]
input_data["ctr_1d"] = [0.0]
input_data["download_num_15d"] = [0.0]
input_data["view_num_1d"] = [0.0]
input_data["feedback_rate_15d"] = [0.0]
input_data["feedback_num_30d"] = [0.0]
input_data["avg_playtime_1d"] = [0.0]
input_data["user_id"] = [1]
input_data["download_rate_15d"] = [0.0]
input_data["uv_rate_1d"] = [0.0]


data_grpc = []
for f, v in input_data.items():
    #v = [[i] for i in v]
    request.inputs[f].CopyFrom(tf.make_tensor_proto([v]))
    print(v)
#print(request)
data_grpc.append(request)
# 测试 耗时
start_ts = time.time()
for _ in range(1000):
    result = stub.Predict(request, 10)
   # print(result)
print((time.time() - start_ts) / 1000)


