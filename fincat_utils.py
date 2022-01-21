import pandas as pd
import numpy as np
import pickle
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertModel
from transformers import AutoTokenizer, AutoModel
import nltk

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased', output_hidden_states = True,)

def extract_context_words(x, window = 6):
  paragraph, offset_start, offset_end = x['paragraph'], x['offset_start'], x['offset_end']
  target_word = paragraph[offset_start : offset_end]
  paragraph = ' ' + paragraph + ' '
  offset_start = offset_start + 1
  offset_end = offset_end + 1
  prev_space_posn = (paragraph[:offset_start].rindex(' ') + 1)
  end_space_posn = (offset_end + paragraph[offset_end:].index(' '))
  full_word = paragraph[prev_space_posn : end_space_posn]

  prev_words = nltk.word_tokenize(paragraph[0:prev_space_posn])
  next_words = nltk.word_tokenize(paragraph[end_space_posn:])
  words_in_context_window = prev_words[-1*window:] + [full_word] + next_words[:window]
  context_text = ' '.join(words_in_context_window)
  return context_text

"""The following functions have been created with inspiration from https://github.com/arushiprakash/MachineLearning/blob/main/BERT%20Word%20Embeddings.ipynb"""

def bert_text_preparation(text, tokenizer):
    """Preparing the input for BERT
    
    Takes a string argument and performs
    pre-processing like adding special tokens,
    tokenization, tokens to ids, and tokens to
    segment ids. All tokens are mapped to seg-
    ment id = 1.
    
    Args:
        text (str): Text to be converted
        tokenizer (obj): Tokenizer object
            to convert text into BERT-re-
            adable tokens and ids
        
    Returns:
        list: List of BERT-readable tokens
        obj: Torch tensor with token ids
        obj: Torch tensor segment ids
    
    """
    marked_text = "[CLS] " + text + " [SEP]"
    tokenized_text = tokenizer.tokenize(marked_text)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    segments_ids = [1]*len(indexed_tokens)

    # Convert inputs to PyTorch tensors
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])

    return tokenized_text, tokens_tensor, segments_tensors
    
def get_bert_embeddings(tokens_tensor, segments_tensors, model):
    """Get embeddings from an embedding model
    
    Args:
        tokens_tensor (obj): Torch tensor size [n_tokens]
            with token ids for each token in text
        segments_tensors (obj): Torch tensor size [n_tokens]
            with segment ids for each token in text
        model (obj): Embedding model to generate embeddings
            from token and segment ids
    
    Returns:
        list: List of list of floats of size
            [n_tokens, n_embedding_dimensions]
            containing embeddings for each token
    """
    
    # Gradient calculation id disabled
    # Model is in inference mode
    with torch.no_grad():
        outputs = model(tokens_tensor, segments_tensors)
        # Removing the first hidden state
        # The first state is the input state
        hidden_states = outputs[2][1:]

    # Getting embeddings from the final BERT layer
    token_embeddings = hidden_states[-1]
    # Collapsing the tensor into 1-dimension
    token_embeddings = torch.squeeze(token_embeddings, dim=0)
    # Converting torchtensors to lists
    list_token_embeddings = [token_embed.tolist() for token_embed in token_embeddings]

    return list_token_embeddings

def bert_embedding_extract(context_text, word):
  tokenized_text, tokens_tensor, segments_tensors = bert_text_preparation(context_text, tokenizer)
  list_token_embeddings = get_bert_embeddings(tokens_tensor, segments_tensors, model)
  word_tokens,tt,st = bert_text_preparation(word, tokenizer)
  word_embedding_all = []
  for word_tk in word_tokens:
    word_index = tokenized_text.index(word_tk)
    word_embedding = list_token_embeddings[word_index]
    word_embedding_all.append(word_embedding)
  word_embedding_mean = np.array(word_embedding_all).mean(axis=0)
  return word_embedding_mean

