sudo nohup docker run --rm \
    -p 8501:8501 \
    -p 8500:8500 \
    --mount type=bind,source=/tf_serving,target=/tfs \
    -t tensorflow/serving \
    --model_config_file=/tfs/config/models.config \
    --model_config_file_poll_wait_seconds=60 \
    --allow_version_labels_for_unavailable_models=true \
    --batching_parameters_file=/tfs/config/batch.config \
    --enable_batching=true \
    >> /tf_serving/logs/tf_serving.log 2>&1 &
