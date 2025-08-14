echo "Creating project structure..."
mkdir -p src
mkdir -p research
mkdir -p config
mkdir -p prompts

touch src/__init__.py 
touch src/schema_loader.py 
touch src/sql_generator.py 
touch src/query_executor.py 
touch src/visualizer.py
touch src/pipeline.py src/utils.py
touch config/__init__.py 
touch config/settings.py
touch prompts/sql_prompt.txt
touch research/experiments.ipynb 
touch research/trials.ipynb
touch .env 
touch app.py 
touch requirements.txt 
touch setup.py

echo "Project structure created successfully."
echo "Remember to fill in the necessary details in the .env, setup.py, and requirements.txt files."