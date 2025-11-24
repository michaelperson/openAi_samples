import hashlib
prompt_hash = hashlib.sha256(prompt.encode('utf-8')).hexdigest()
logger.info(f"API call - model: gpt-4o, prompt_hash: {prompt_hash}, status: 200")

