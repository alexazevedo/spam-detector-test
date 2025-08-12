# Thought process
## Considerations

### Performance x costs
- is it worth having a function pre-filtering the messages, to avoid wasting resources using OpenAI with email messages that can possibly be characterized as HAMs? Maybe having a basic machine-learning feature that could be trained with some basic examples that would be able to easily identify good and bad e-mails and leave just the `uncertain` messages to be analysed by the LLM model? 
- What would be the best cost x benefit model to be used by this application ? Is gpt-4o-mini the best one ? 
- Adjust the temperature, low temperature for a consistent/ more reliable response?
- is the max_tokens value enough ? Isn't it to much, are the "reason" going to be more than 100 tokens by any chance? 


### Security 
- Add "system" prompt to limit/define the boundaries on what's going to be sent to OpenAI and ensure we won't be sending malicious commands/prompts in the email message
- limit the length of the email body ?!
- remove or escape pottentially dangerous characters? 
- make sure the API response returns a valid json. How?



