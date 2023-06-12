# Yamorous Hearts: A Root Vegetable Romance (p5) by Yammers

Overview: This is a Dating simulator with yours truly, powered by chatgpt.
Uses the gpt turbo 3.5 API and long bios about our personality in order to mimic our speech and behavior. A user will be able to select which chatbot (characters listed below) to talk to, and the chatbot will respond in the style of the person. You can talk with multiple characters and date as many as you like. Poly rights! All four devo characters have the goal of seducing the user, so they are extremely flirty. MykolykGPT has the goal of increasing the learnination quotient of the user, and will use the same phrases and acronyms as real Mr. Mykolyk. 

# Launch Codes
The website is up at [newsify.social:5000](newsify.social:5000), but please do not abuse it without our consent - the free trial of the openai API will run out rather quickly. 

Also shoutout to Slam because this websocket stuff is nonsensical

To run it locally with your own API key (we would prefer this):

First, clone the repo into a folder
`git clone git@github.com:mayanelson/p5.git`
cd into the repo
`cd p5`
Create a virtual environment (optional)
`python3 -m venv <venvName>`
`source <venvName>/bin/activate`
Install dependencies (this takes a long time)
`pip install -r requirements.txt`
Procure API key at https://platform.openai.com/account/api-keys
You may need to create an account or sign in to proceed. 
Each new account comes with $5 of free API credit which is more than enough to try out Yamorous Hearts, but if you have an account older than ~3 months your credit will have already expired. 
Each account is connected to a unique (and not virtual) phone number, which makes getting a second account difficult
`nano app/keys/key_openai.txt`
paste in your API key. Make sure to store it somewhere else too, since openai only shows it you once. Just don't push it to github
Now, you're ready to run the program
`cd app`
`python3 __init__.py`



Note: Requirements.txt may change a lot as we figure out the compatibility of different llm libraries
