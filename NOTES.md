# Notes

- https://github.com/joaopalmeiro/template-python-uv-package
- https://openai.com/api/pricing/
  - https://platform.openai.com/docs/guides/images-vision?api-mode=chat#calculating-costs
- https://github.com/nerveband/token-vision
- https://docs.together.ai/docs/vision-overview#pricing
- https://github.com/AgentOps-AI/tokencost
- https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken
- https://github.com/huggingface/tokenizers
- https://docs.anthropic.com/en/docs/build-with-claude/token-counting
- https://docs.anthropic.com/en/docs/build-with-claude/vision
  - "Very small images under 200 pixels on any given edge may degrade performance."
- https://platform.openai.com/tokenizer

## Commands

```bash
python scripts/generate_images.py
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/ dist/ src/praicing/__pycache__/
```
