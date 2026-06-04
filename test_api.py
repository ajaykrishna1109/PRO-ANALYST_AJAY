from api import ask_llm

print("Starting test...")

answer = ask_llm(
    "OAuth access token TTL is 24 hours.",
    "How long is the access token valid?"
)

print("Response:")
print(answer)