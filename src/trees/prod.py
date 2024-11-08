from src.models import (
    AttemptEdge,
    FixAttemptConfig,
    FixPromptConfig,
    KTopConfig,
    LLMConfig,
    Model,
    PoolingConfig,
    Prompt,
    RootAttemptConfig,
    RootPromptConfig,
)

# C reasoning 50
# C reasoning 200
# - fix C reasoning 100
# -- fix C reasoning 100
# --- fix C reasoning 100
# ---- fix C reasoning 50
# - fix C reasoning POOL 25
# -- fix C reasoning POOL 25
# --- fix C reasoning POOL 25
# C COT 100
# - fix COT 100
# 4o reasoning 200
# - fix 4o reasoning 50
# -- fix 4o reasoning 50

# MAX: 1175

big_claude_tree: list[RootAttemptConfig] = [
    RootAttemptConfig(
        attempts=50,
        llm_config=LLMConfig(
            model=Model.claude_3_5_sonnet,
            temperature=0.95,
        ),
        prompt_config=RootPromptConfig(
            base_prompt=Prompt.REASONING,
            use_examples=True,
            use_diffs=True,
            use_images=True,
            use_ascii=True,
            use_array=True,
            use_image=True,
        ),
        fixes=[],
    ),
    RootAttemptConfig(
        attempts=200,
        llm_config=LLMConfig(
            model=Model.claude_3_5_sonnet,
            temperature=0.95,
        ),
        prompt_config=RootPromptConfig(
            base_prompt=Prompt.REASONING,
            use_examples=True,
            use_diffs=True,
            use_images=True,
            use_ascii=True,
            use_array=True,
            use_image=True,
        ),
        fixes=[
            AttemptEdge(
                k_top_config=KTopConfig(
                    k_top=10, unique_code=False, unique_output=False
                ),
                configs=[
                    FixAttemptConfig(
                        attempts=10,
                        llm_config=LLMConfig(
                            model=Model.claude_3_5_sonnet,
                            temperature=0.95,
                        ),
                        prompt_config=FixPromptConfig(
                            base_prompt=Prompt.REASONING,
                            use_ascii=True,
                            use_array=True,
                            use_image=True,
                            use_fix_reasoning_tags=True,
                            use_fix_fail_line=True,
                            use_typical_issue_text=True,
                            include_diffs=True,
                        ),
                        fixes=[
                            AttemptEdge(
                                k_top_config=KTopConfig(
                                    k_top=10, unique_code=False, unique_output=False
                                ),
                                configs=[
                                    FixAttemptConfig(
                                        attempts=10,
                                        llm_config=LLMConfig(
                                            model=Model.claude_3_5_sonnet,
                                            temperature=0.95,
                                        ),
                                        prompt_config=FixPromptConfig(
                                            base_prompt=Prompt.REASONING,
                                            use_ascii=True,
                                            use_array=True,
                                            use_image=True,
                                            use_fix_reasoning_tags=True,
                                            use_fix_fail_line=True,
                                            use_typical_issue_text=True,
                                            include_diffs=True,
                                        ),
                                        fixes=[
                                            AttemptEdge(
                                                k_top_config=KTopConfig(
                                                    k_top=10,
                                                    unique_code=False,
                                                    unique_output=False,
                                                ),
                                                configs=[
                                                    FixAttemptConfig(
                                                        attempts=10,
                                                        llm_config=LLMConfig(
                                                            model=Model.claude_3_5_sonnet,
                                                            temperature=0.95,
                                                        ),
                                                        prompt_config=FixPromptConfig(
                                                            base_prompt=Prompt.REASONING,
                                                            use_ascii=True,
                                                            use_array=True,
                                                            use_image=True,
                                                            use_fix_reasoning_tags=True,
                                                            use_fix_fail_line=True,
                                                            use_typical_issue_text=True,
                                                            include_diffs=True,
                                                        ),
                                                        fixes=[
                                                            AttemptEdge(
                                                                k_top_config=KTopConfig(
                                                                    k_top=5,
                                                                    unique_code=False,
                                                                    unique_output=False,
                                                                ),
                                                                configs=[
                                                                    FixAttemptConfig(
                                                                        attempts=10,
                                                                        llm_config=LLMConfig(
                                                                            model=Model.claude_3_5_sonnet,
                                                                            temperature=0.95,
                                                                        ),
                                                                        prompt_config=FixPromptConfig(
                                                                            base_prompt=Prompt.REASONING,
                                                                            use_ascii=True,
                                                                            use_array=True,
                                                                            use_image=True,
                                                                            use_fix_reasoning_tags=True,
                                                                            use_fix_fail_line=True,
                                                                            use_typical_issue_text=True,
                                                                            include_diffs=True,
                                                                        ),
                                                                        fixes=[],
                                                                    )
                                                                ],
                                                            )
                                                        ],
                                                    )
                                                ],
                                            )
                                        ],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            ),
            AttemptEdge(
                pooling=(PoolingConfig(size=4)),
                k_top_config=KTopConfig(
                    k_top=5, unique_code=False, unique_output=False
                ),
                configs=[
                    FixAttemptConfig(
                        attempts=5,
                        llm_config=LLMConfig(
                            model=Model.claude_3_5_sonnet,
                            temperature=0.95,
                        ),
                        prompt_config=FixPromptConfig(
                            base_prompt=Prompt.REASONING,
                            use_ascii=True,
                            use_array=True,
                            use_image=True,
                            use_fix_reasoning_tags=True,
                            use_fix_fail_line=True,
                            use_typical_issue_text=True,
                            include_diffs=True,
                        ),
                        fixes=[
                            AttemptEdge(
                                pooling=(PoolingConfig(size=3)),
                                k_top_config=KTopConfig(
                                    k_top=5, unique_code=False, unique_output=False
                                ),
                                configs=[
                                    FixAttemptConfig(
                                        attempts=5,
                                        llm_config=LLMConfig(
                                            model=Model.claude_3_5_sonnet,
                                            temperature=0.95,
                                        ),
                                        prompt_config=FixPromptConfig(
                                            base_prompt=Prompt.REASONING,
                                            use_ascii=True,
                                            use_array=True,
                                            use_image=True,
                                            use_fix_reasoning_tags=True,
                                            use_fix_fail_line=True,
                                            use_typical_issue_text=True,
                                            include_diffs=True,
                                        ),
                                        fixes=[
                                            AttemptEdge(
                                                pooling=(PoolingConfig(size=3)),
                                                k_top_config=KTopConfig(
                                                    k_top=5,
                                                    unique_code=False,
                                                    unique_output=False,
                                                ),
                                                configs=[
                                                    FixAttemptConfig(
                                                        attempts=5,
                                                        llm_config=LLMConfig(
                                                            model=Model.claude_3_5_sonnet,
                                                            temperature=0.95,
                                                        ),
                                                        prompt_config=FixPromptConfig(
                                                            base_prompt=Prompt.REASONING,
                                                            use_ascii=True,
                                                            use_array=True,
                                                            use_image=True,
                                                            use_fix_reasoning_tags=True,
                                                            use_fix_fail_line=True,
                                                            use_typical_issue_text=True,
                                                            include_diffs=True,
                                                        ),
                                                        fixes=[],
                                                    )
                                                ],
                                            )
                                        ],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            ),
        ],
    ),
    RootAttemptConfig(
        attempts=200,
        llm_config=LLMConfig(
            model=Model.claude_3_5_sonnet,
            temperature=0.95,
        ),
        prompt_config=RootPromptConfig(
            base_prompt=Prompt.COT,
            use_examples=True,
            use_diffs=True,
            use_images=True,
            use_ascii=True,
            use_array=True,
            use_image=True,
        ),
        fixes=[
            AttemptEdge(
                k_top_config=KTopConfig(
                    k_top=10, unique_code=False, unique_output=False
                ),
                configs=[
                    FixAttemptConfig(
                        attempts=10,
                        llm_config=LLMConfig(
                            model=Model.claude_3_5_sonnet,
                            temperature=0.95,
                        ),
                        prompt_config=FixPromptConfig(
                            base_prompt=Prompt.COT,
                            use_ascii=True,
                            use_array=True,
                            use_image=True,
                            use_fix_reasoning_tags=True,
                            use_fix_fail_line=True,
                            use_typical_issue_text=True,
                            include_diffs=True,
                        ),
                        fixes=[],
                    )
                ],
            ),
        ],
    ),
    RootAttemptConfig(
        attempts=200,
        llm_config=LLMConfig(
            model=Model.gpt_4o,
            temperature=0.95,
        ),
        prompt_config=RootPromptConfig(
            base_prompt=Prompt.REASONING,
            use_examples=True,
            use_diffs=True,
            use_images=True,
            use_ascii=True,
            use_array=True,
            use_image=True,
        ),
        fixes=[
            AttemptEdge(
                k_top_config=KTopConfig(
                    k_top=10, unique_code=False, unique_output=False
                ),
                configs=[
                    FixAttemptConfig(
                        attempts=5,
                        llm_config=LLMConfig(
                            model=Model.gpt_4o,
                            temperature=0.95,
                        ),
                        prompt_config=FixPromptConfig(
                            base_prompt=Prompt.REASONING,
                            use_ascii=True,
                            use_array=True,
                            use_image=True,
                            use_fix_reasoning_tags=True,
                            use_fix_fail_line=True,
                            use_typical_issue_text=True,
                            include_diffs=True,
                        ),
                        fixes=[
                            AttemptEdge(
                                k_top_config=KTopConfig(
                                    k_top=10, unique_code=False, unique_output=False
                                ),
                                configs=[
                                    FixAttemptConfig(
                                        attempts=5,
                                        llm_config=LLMConfig(
                                            model=Model.gpt_4o,
                                            temperature=0.95,
                                        ),
                                        prompt_config=FixPromptConfig(
                                            base_prompt=Prompt.REASONING,
                                            use_ascii=True,
                                            use_array=True,
                                            use_image=True,
                                            use_fix_reasoning_tags=True,
                                            use_fix_fail_line=True,
                                            use_typical_issue_text=True,
                                            include_diffs=True,
                                        ),
                                        fixes=[],
                                    )
                                ],
                            ),
                        ],
                    )
                ],
            ),
        ],
    ),
]

# max attempts: 350
small_claude_tree: list[RootAttemptConfig] = [
    RootAttemptConfig(
        attempts=10,
        llm_config=LLMConfig(
            model=Model.claude_3_5_sonnet,
            temperature=0.95,
        ),
        prompt_config=RootPromptConfig(
            base_prompt=Prompt.REASONING,
            use_examples=True,
            use_diffs=True,
            use_images=True,
            use_ascii=True,
            use_array=True,
            use_image=True,
        ),
        fixes=[],
    ),
    RootAttemptConfig(
        attempts=100,
        llm_config=LLMConfig(
            model=Model.claude_3_5_sonnet,
            temperature=0.95,
        ),
        prompt_config=RootPromptConfig(
            base_prompt=Prompt.REASONING,
            use_examples=True,
            use_diffs=True,
            use_images=True,
            use_ascii=True,
            use_array=True,
            use_image=True,
        ),
        fixes=[
            AttemptEdge(
                pooling=(PoolingConfig(size=4)),
                k_top_config=KTopConfig(
                    k_top=10, unique_code=False, unique_output=False
                ),
                configs=[
                    FixAttemptConfig(
                        attempts=3,
                        llm_config=LLMConfig(
                            model=Model.claude_3_5_sonnet,
                            temperature=0.95,
                        ),
                        prompt_config=FixPromptConfig(
                            base_prompt=Prompt.REASONING,
                            use_ascii=True,
                            use_array=True,
                            use_image=True,
                            use_fix_reasoning_tags=True,
                            use_fix_fail_line=True,
                            use_typical_issue_text=True,
                            include_diffs=True,
                        ),
                        fixes=[
                            AttemptEdge(
                                pooling=(PoolingConfig(size=4)),
                                k_top_config=KTopConfig(
                                    k_top=10, unique_code=False, unique_output=False
                                ),
                                configs=[
                                    FixAttemptConfig(
                                        attempts=3,
                                        llm_config=LLMConfig(
                                            model=Model.claude_3_5_sonnet,
                                            temperature=0.95,
                                        ),
                                        prompt_config=FixPromptConfig(
                                            base_prompt=Prompt.REASONING,
                                            use_ascii=True,
                                            use_array=True,
                                            use_image=True,
                                            use_fix_reasoning_tags=True,
                                            use_fix_fail_line=True,
                                            use_typical_issue_text=True,
                                            include_diffs=True,
                                        ),
                                        fixes=[
                                            AttemptEdge(
                                                pooling=(PoolingConfig(size=4)),
                                                k_top_config=KTopConfig(
                                                    k_top=10,
                                                    unique_code=False,
                                                    unique_output=False,
                                                ),
                                                configs=[
                                                    FixAttemptConfig(
                                                        attempts=3,
                                                        llm_config=LLMConfig(
                                                            model=Model.claude_3_5_sonnet,
                                                            temperature=0.95,
                                                        ),
                                                        prompt_config=FixPromptConfig(
                                                            base_prompt=Prompt.REASONING,
                                                            use_ascii=True,
                                                            use_array=True,
                                                            use_image=True,
                                                            use_fix_reasoning_tags=True,
                                                            use_fix_fail_line=True,
                                                            use_typical_issue_text=True,
                                                            include_diffs=True,
                                                        ),
                                                        fixes=[],
                                                    )
                                                ],
                                            )
                                        ],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            ),
            AttemptEdge(
                k_top_config=KTopConfig(
                    k_top=10, unique_code=False, unique_output=False
                ),
                configs=[
                    FixAttemptConfig(
                        attempts=3,
                        llm_config=LLMConfig(
                            model=Model.claude_3_5_sonnet,
                            temperature=0.95,
                        ),
                        prompt_config=FixPromptConfig(
                            base_prompt=Prompt.REASONING,
                            use_ascii=True,
                            use_array=True,
                            use_image=True,
                            use_fix_reasoning_tags=True,
                            use_fix_fail_line=True,
                            use_typical_issue_text=True,
                            include_diffs=True,
                        ),
                        fixes=[
                            AttemptEdge(
                                k_top_config=KTopConfig(
                                    k_top=10, unique_code=False, unique_output=False
                                ),
                                configs=[
                                    FixAttemptConfig(
                                        attempts=3,
                                        llm_config=LLMConfig(
                                            model=Model.claude_3_5_sonnet,
                                            temperature=0.95,
                                        ),
                                        prompt_config=FixPromptConfig(
                                            base_prompt=Prompt.REASONING,
                                            use_ascii=True,
                                            use_array=True,
                                            use_image=True,
                                            use_fix_reasoning_tags=True,
                                            use_fix_fail_line=True,
                                            use_typical_issue_text=True,
                                            include_diffs=True,
                                        ),
                                        fixes=[
                                            AttemptEdge(
                                                k_top_config=KTopConfig(
                                                    k_top=10,
                                                    unique_code=False,
                                                    unique_output=False,
                                                ),
                                                configs=[
                                                    FixAttemptConfig(
                                                        attempts=3,
                                                        llm_config=LLMConfig(
                                                            model=Model.claude_3_5_sonnet,
                                                            temperature=0.95,
                                                        ),
                                                        prompt_config=FixPromptConfig(
                                                            base_prompt=Prompt.REASONING,
                                                            use_ascii=True,
                                                            use_array=True,
                                                            use_image=True,
                                                            use_fix_reasoning_tags=True,
                                                            use_fix_fail_line=True,
                                                            use_typical_issue_text=True,
                                                            include_diffs=True,
                                                        ),
                                                        fixes=[],
                                                    )
                                                ],
                                            )
                                        ],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            ),
        ],
    ),
    RootAttemptConfig(
        attempts=50,
        llm_config=LLMConfig(
            model=Model.claude_3_5_sonnet,
            temperature=0.95,
        ),
        prompt_config=RootPromptConfig(
            base_prompt=Prompt.COT,
            use_examples=True,
            use_diffs=True,
            use_images=True,
            use_ascii=True,
            use_array=True,
            use_image=True,
        ),
        fixes=[
            AttemptEdge(
                k_top_config=KTopConfig(
                    k_top=10, unique_code=False, unique_output=False
                ),
                configs=[
                    FixAttemptConfig(
                        attempts=3,
                        llm_config=LLMConfig(
                            model=Model.claude_3_5_sonnet,
                            temperature=0.95,
                        ),
                        prompt_config=FixPromptConfig(
                            base_prompt=Prompt.COT,
                            use_ascii=True,
                            use_array=True,
                            use_image=True,
                            use_fix_reasoning_tags=True,
                            use_fix_fail_line=True,
                            use_typical_issue_text=True,
                            include_diffs=True,
                        ),
                        fixes=[
                            AttemptEdge(
                                k_top_config=KTopConfig(
                                    k_top=10, unique_code=False, unique_output=False
                                ),
                                configs=[
                                    FixAttemptConfig(
                                        attempts=3,
                                        llm_config=LLMConfig(
                                            model=Model.claude_3_5_sonnet,
                                            temperature=0.95,
                                        ),
                                        prompt_config=FixPromptConfig(
                                            base_prompt=Prompt.REASONING,
                                            use_ascii=True,
                                            use_array=True,
                                            use_image=True,
                                            use_fix_reasoning_tags=True,
                                            use_fix_fail_line=True,
                                            use_typical_issue_text=True,
                                            include_diffs=True,
                                        ),
                                        fixes=[],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            ),
        ],
    ),
]
