### Documentation

This code generates synthetic textual data in the form of request-response pairs using ChatGPT API. The data is in a JSON for consistency and ease of processing.

### Use case

For some use cases, using synthetic data is a perfectly valid approach for finetuning/training a model. Most recently Nous Hermes 2 - Yi-34B  is an open source LLM trained on 1 million data pairs generated with GPT-4. With this approach you can use your API to generate data at a massive scale, automatically, for training/finetuning your own model.

### Functions

**generate_data()**: Runs a single iteration of the data generation, which you may want to do to check prior to generating at a massive scale.

**generate_many_data()**: Runs n number of iterations, allowing you to generate many data in a single run. At the end of the code, the generated data will be appended to a .txt file of your specified name.


### Customizations

You can easily edit the system instruction if you want to specify the format or number of pairs to generate in a single iteration. Alternatively, you may try this form of code:

```
biology = ['animal', 'plant', 'marine', 'evolutionary', 'cellular']
for idx, word in enumerate(biology):
    question = f'Generate data where  R1 is a question about {word} biology.'
    print(f'Running for: {word}')
    generate_many_data(question, 5, f'Biology_{word}.txt')
```
This would generate 10×5 question-answer pairs for each biology keywords. The accumulated pairs from each keywords would then be saved in separate .txt files.
