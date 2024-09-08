from transformers import pipeline

class AI_Chatter:
    def __init__(self):
        pass
    def generate_response(self, message):
        generator = pipeline('text-generation', model='gpt2')
        response = generator(message, max_length=20, num_return_sequences=1)
        processed_response = response[0]['generated_text']
        removed_lines_response = processed_response.replace('\n', ' ').replace('\r', '')
        return removed_lines_response