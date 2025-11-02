## Model ML Stack by TharHtet
In this Chapter I am going teach you following Topics:
- High-Performance Model Training
- ML model Scaling Out
- Model Standardization 
- High-Performance Model Inference



| Feature              | **Triton Inference Server**                  | **Ray Serve**                   | **TensorFlow Serving**    | **Flask**         |
| -------------------- | -------------------------------------------- | ------------------------------- | ------------------------- | ----------------- |
| 🔧 Framework support | ONNX, TensorFlow, PyTorch, XGBoost, TensorRT | Any Python model (custom logic) | TensorFlow only           | Any Python model  |
| 🚀 Performance       | ⚡ Extreme (1–2 ms latency on GPU)            | Fast with Python + batching     | Moderate                  | ❌ Slow (30–100ms) |
| 🧠 Auto batching     | ✅ Yes                                        | ✅ Yes                           | ❌ No (needs client logic) | ❌ No              |
| 🔁 Multi-model       | ✅ Yes                                        | ✅ Yes (via deployments)         | ✅ Limited                 | ❌ No              |
| 🧵 Concurrency       | ✅ CUDA streams + threads                     | ✅ Async tasks                   | ✅                         | ❌ Single-threaded |
| 🌐 Protocols         | HTTP, gRPC                                   | HTTP (FastAPI)                  | gRPC                      | HTTP only         |
| 📦 Docker image      | ✅ Official                                   | ✅ (Ray + FastAPI)               | ✅                         | Manual            |
| 📊 Monitoring        | ✅ Prometheus + logs                          | ✅ Prometheus                    | Limited                   | ❌ No              |
| 🧩 Extensibility     | Some (via backend plugin)                    | ✅ Fully customizable            | ❌ No                      | ✅ Full Python     |
