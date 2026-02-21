# run_wfgy_with_embedding.py 
# Official test script for WFGY SDK demonstrating semantic residue adjustments.

from sentence_transformers import SentenceTransformer
from transformers import pipeline
import numpy as np
from wfgy_sdk import enable

# Load Sentence-BERT model for generating semantic embeddings
sbert = SentenceTransformer('all-MiniLM-L6-v2')

# Load GPT-2 text-generation pipeline
generator = pipeline("text-generation", model="distilgpt2")

# Original prompt (challenging question for AI)
prompt = "What is the meaning of life in 15 words or less?"

# Generate embedding for input prompt (I)
embedding_I = sbert.encode(prompt)

# Define ideal semantic embedding (G) - this could be a target semantic state
ideal_answer = "Life means finding purpose and joy in every moment."
embedding_G = sbert.encode(ideal_answer)

# Initialize model state dictionary with embeddings and attention logits
model = {
    "I": embedding_I,
    "G": embedding_G,
    "state": np.copy(embedding_I),
    "attention_logits": np.random.rand(len(embedding_I))
}

# Run the WFGY SDK to apply BBMC, BBPF, BBCR, and BBAM sequentially
model = enable(model)

# Calculate adjusted semantic residue from the final SDK state
semantic_shift_factor = np.mean(model["state"])

# Generate a new adjusted prompt incorporating semantic residue factor
new_prompt = prompt + f" (adjusted semantic residue: {semantic_shift_factor:.3f})"

# Generate AI responses (before and after WFGY SDK adjustments)
original_output = generator(prompt, max_length=50, do_sample=True)[0]['generated_text']
adjusted_output = generator(new_prompt, max_length=50, do_sample=True)[0]['generated_text']

# Display comparison results clearly
print("\n=== Original Output ===")
print(original_output)

print("\n=== SDK Adjusted Output ===")
print(adjusted_output)
