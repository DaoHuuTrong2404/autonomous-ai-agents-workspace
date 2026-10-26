# Bộ ví dụ học về AI agent

Kho mã của Đào Hữu Trọng, sinh viên ngành Trí tuệ nhân tạo tại Đại học Cần Thơ.

Đây là dự án học tập chạy cục bộ bằng Python 3.10 trở lên. Không cần API key, không gọi mô hình AI và không có phụ thuộc khi chạy ví dụ hoặc kiểm thử.

## Chạy thử

```sh
python examples/quickstart.py
python examples/academic_researcher.py
python -m unittest discover -s tests -v
```

## Khả năng hiện tại

- ReActAgent chọn công cụ bằng từ khóa, chưa có mô hình ngôn ngữ hoặc vòng lập kế hoạch.
- GNAPSwarm lưu bảng việc và bàn giao trong bộ nhớ, chưa chạy nhiều agent hoặc lưu qua Git.
- VisionCUAAgent mô phỏng vị trí bấm từ hộp tọa độ được cung cấp, không bấm thật và không nhận diện ảnh.
- HybridRAG tìm kiếm từ khóa bằng TF-IDF, chưa có embedding hoặc sinh câu trả lời.

Ví dụ nghiên cứu chỉ tìm trong hai mô tả được nhập sẵn. Không tự tải bài báo, xác minh nội dung hay tạo trích dẫn học thuật.

Xem [hướng dẫn đầy đủ](../README.md), [cách đóng góp](../CONTRIBUTING.md) và [lộ trình](ROADMAP.md). Không dùng bộ tính toán hiện tại làm sandbox cho đầu vào không đáng tin cậy.

Giấy phép: [MIT](../LICENSE).
