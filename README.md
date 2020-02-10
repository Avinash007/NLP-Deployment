# NLP-Deployment
This is an NLP powered app deployed using Streamlit

#1: Create a heroku account. Github repo
#2: Install heroku CLI: Done: in cmd try: heroku --help
#3: Clone github repo
#4: Create a new environment
pipenv install streamlit pandas

#4: Required Files
setup.sh
Procfile
requirements.txt

#5. Copy this code in setup.sh
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

#6. Copy this code in Procfile
web: sh setup.sh && streamlit run nlp.py

#7: Activate the virtual environment
pipenv shell

#8: Create requirements.txt
pipenv run pip freeze > requirements.txt

#9. Create nlu.py and start writing logic

#10. Run the nlp.py file
pipenv run streamlit run nlp.py

