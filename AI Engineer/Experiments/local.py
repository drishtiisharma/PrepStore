from transformers import pipeline

model = pipeline(
    "text-generation",
    model = "Qwen/Qwen2.5-1.5B-Instruct"
)

response = model(
    "explain quantum computing",
    max_new_tokens = 100
)

print(response[0])