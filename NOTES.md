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
- https://www.stainless.com/
- https://github.com/openai/openai-python?tab=readme-ov-file#using-types
  - https://pypi.org/project/openai/
  - https://github.com/openai/openai-python/blob/v1.97.0/src/openai/types/chat/chat_completion_message_param.py
  - https://github.com/openai/openai-python/blob/v1.97.0/src/openai/types/chat/chat_completion_user_message_param.py
  - https://github.com/openai/openai-python/blob/v1.97.0/src/openai/types/chat/chat_completion_content_part_image_param.py
  - [Add GPT-4.1 support](https://github.com/openai/tiktoken/issues/395) issue
  - https://huggingface.co/datasets/openai/mrcr#how-to-run: `MODEL= "gpt-4.1"` + `enc = tiktoken.get_encoding("o200k_base")`
  - https://community.openai.com/t/whats-the-tokenization-algorithm-gpt-4-1-uses/1245758: "GPT-4.1 uses the same tokenizer as 4o; same encoding."
  - https://github.com/openai/openai-python/blob/v1.97.0/src/openai/types/chat/completion_create_params.py#L37: `messages: Required[Iterable[ChatCompletionMessageParam]]`
  - https://github.com/openai/openai-python/blob/v1.97.0/api.md?plain=1#L42
- https://mypy.readthedocs.io/en/stable/typed_dict.html:
  - "Since TypedDicts are really just regular dicts at runtime, it is not possible to use `isinstance` checks to distinguish between different variants of a Union of TypedDict in the same way you can with regular objects."
  - https://mypy.readthedocs.io/en/stable/literal_types.html#tagged-unions

## Commands

```bash
python scripts/generate_images.py
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/ dist/ src/praicing/__pycache__/
```
