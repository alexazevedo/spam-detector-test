## New logic
Check `check_spam_refactored.py` - it is the start point for the new solution 


## What changed

- Format/prepare the messages removing html, whitespaces, etc, before processing to optimize the performance and don't waste resources with content that won't be useful for the analysis;

- Added a simple/basic pre-filter using scikit-learn before using LLM to classify spam messages. This might not be the best solution, if going through this approach, but it's just an example of a prefilter step that can be cost-saving if we aim to classify a large number of messages. The idea behind it is to catch obvious spam cases using ML and leave the 'uncertain' cases to be checked by the LLM. This can be a bit tricky to set up and train, we would need to add samples in different languages, for example, but depending on the number of messages being processed it might be worth having a pre-filter before. In my example the T_LOW threshold is a bit high, but because I don't have enough trained data; See `prefilter.py` for the specifics;

- Using Responses API instead of Chat Completitions, it's a newer approach, and we can also use the other tools like images/web search/etc, and it seems to have a more structured way to be used, but not actually needed in this case. Chat Chat Completions can be used there as well.

- Forced an structured output with a defined JSON schema using Pydantic model;

- Added a "SYSTEM" message (aka instructions parameter in the Responses API) to set boundaries on what's going to be sent to OpenAI and ensure we won't be sending malicious commands/prompts in the email message;

- Reduced a little bit the number of max output tokens, since we would want a one-line sentence with the reason;

- Adjusted the temperature, setting a low temperature for a more consistent/reliable responses since this is a classifier and we don't want very ramdom responses everytime;
