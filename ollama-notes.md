1. Is Ollama production ready?
    
    Short answer is no. It has no real support for concurrency, so all your queries need to be executed sequentualy. If you load multiple copies then you take the hit of needing big memory for each copy. It does not really support loading a model once and then allowing multiple threads to process requests simultaniously. [Source.](https://www.reddit.com/r/ollama/comments/1cbmrbr/how_to_make_ollama_production_ready/)

    It’s not for production. Ollama’s documentation explicitly warns you not to use the API in production. It’s for messing around and experimenting with LLMs and different models.
    If you don’t see the use of it, I recommend you use something else that suits your tastes more. [Source.](https://news.ycombinator.com/item?id=39311747#:~:text=It's%20not%20for%20production.,that%20suits%20your%20tastes%20more.)

2. Processing more than 1 request at a time

    It's still experimental.

    1. There's no prioritization between requests processed or models
    2. I can't say if I just want to use some percentage of my ram
    3. No option to orchestrate different machines at processing request time. There's no option to use many machines working together to serve quicker