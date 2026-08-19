# Build a Blog Writing Crew with CrewAI

**Author:** Anami James A 
**Email:** 22iot-anamijames4168@yit.edu.in

---

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_h6t9b3y7)

---

## Introducing Today's Project!

In this project, I'm going to build A Blog Writing Crew using CrewAi: a team of three AI agents configured with distinct roles, goals, and backstories that work together in sequence to research, draft, and edit a complete blog post. 

### Key tools and concepts

The key tools I used include CrewAI, uv package installer, Gemini API Key, CrewAI CLI... Key concepts I learnt include how to make use of uv to install crewai, how to link a model in crewai , change the files in the folder as per the user's need and get a blog done by crewai.

### Challenges and wins

This project took me approximately 50 minutes... The most challenging part was making the CrewAI able to use the API Key without any failure

### Personal reflection

I did this project today to learn how to make use of CrewAI and also use the API Key. 

---

## Installing Python and CrewAI

In this step, I am setting up the environment and tools to be installed in the computer. So for the CrewAI project we need uv python package installer, CrewAI CLI and API key from Google because our CrewAI project needs to connect to an AI model that powers their thinking.

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_v8bn4x1w)

### Understanding the uv package manager

I learned that uv is an extremely fast, all-in-one Python package and project manager written in Rust. It aims to replace tools like pip and pip-tools, offering significant speed improvements for dependency resolution and package installation, and also includes Python version management. CrewAI uses it under the hood. 

---

## Scaffolding the CrewAI Project

In this step, I am creating the CrewAI project using the CLI, exploring the project structure and at last configure the API Key and model settings.

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_v4nt8wf6)

### Key project files

Two key files are crew.py and main.py. crew.py which is used for wiring everything together and orchestrates the crew and main.py which is used as the entry point that kicks off the crew when you run the project.

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_w2dc5nq8)

---

## Configuring AI Agents

In this step, I'm going to replace the default agents with three custom agents. Also I am going to configure each agent with a roal, goal, and a backstory.

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_j3x8n1v6)

### How agent configuration shapes AI behavior

I configured three agents Researcher, Writer and Editor with role, goal and backstory defined for each. The role tells the agent what job title it has. The goal tells it what outcome to aim for. The backstory gives it a persona and expertise to draw from when generating responses. Together, they guide the large language model to produce output that matches the agent's specialty. ... The {topic} variable is used because once the crew runs it will automatically swaps {topic} for that value. This means the crew can write about any subject without changing the configuration.

---

## Defining the Task Pipeline

In this step, I'm defining three sequential tasks in the tasks.yaml and connect each task to its responsible agent. These tasks are important because these tells the agent exactly what job to complete and what the finished work should look like. So we will create three tasks that chain together : first research the topic, then write a blog post from that research, then edit and polish the final draft.

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_p3n8v5w1)

### How the tasks chain together

The tasks chain together by first the researcher agent produces a research brief. The writer agent takes that brief and turns it into a blog post. The editor agent polishes the final post and saves it to output/blog_post.md. Only the editing task has output_file because earlier outputs are passed directly to the next agent in memory.

---

## Connecting YAML Configuration to Python

I'm connecting my agents and tasks into a crew by updating crew.py file and also I am passing a topic to the crew by updating main.py file.

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_p3n8v2q6)

### Why method names must match YAML keys

The method names need to match because if the method names in crew.py do not match the keys in the YAML configuration files (agents.yaml and tasks.yaml), the crew will fail to run correctly

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_h8f4d6a2)

---

## Running the Blog Writing Crew

In this step, I'm going to install dependencies, run the crew, watch the agents collaborate to produce a blog post and then experiment with different topic to understand the output variations.

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_p4n8v1q6)

### How the agents collaborated

I ran my crew and the agents collaborated in the manner that each agent receives the output of the previous agent's task as context. The Researcher's brief feeds into the Writer's draft, and the Writer's draft feeds into the Editor's final polish. This is multi-agent collaboration in action.

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_h6t9b3y7)

---

## Adding a Social Media Manager Agent

In this project extension, I'm adding a social media manager agent to the crew. The project will make use of the new agent to generate social media contents because this will mirror a real-world content workflow and I will be able to understand how to scale multli-agent systems by introducing new agents and tasks without changing the existing ones

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_w3f8j1v6)

### Extending the crew with new agents and tasks

I added the social media manager by creating new agent named Social Media Manager in agents.yaml, Social Media Task task in tasks.yaml and also wired them together in the crew.py. 

![Image](http://nextwork.ai/secure_beige_smart_jujube/uploads/ai-crewai-blog-writing-crew_t6c1g4q8)

### Social media output

In this project extension, my social media agent generated a social media type content basically for Twitter/X. The Twitter thread has a roadmap from scratch basically for the topic mentioned in the main.py... The LinkedIn post a two paragraph summary giving a shorthand summary of what it has understood.

### Experimenting with agent backstories

When I changed the backstory to Genz social media native the output changed accordingly. The output changed by mentioning the section and also the way each points were shown. This showed me that the depending on the backstory the output also varies.

---

## Important Project Files

This project is made up of a few main files that control the behavior of the crew. These are the most important ones to know:

- `pyproject.toml` - Project metadata, dependency setup, and CrewAI configuration.
- `.env` - Stores the Gemini API key and model name used by the project.
- `crew.jsonc` - JSON-based crew definition used by the CrewAI CLI to know which agents and tasks are part of the project.
- `blog_writing_crew/crew.py` - The Python file that wires together agents, tasks, and the crew lifecycle.
- `blog_writing_crew/main.py` - The entry point that starts the crew and passes the main topic input.
- `blog_writing_crew/config/agents.yaml` - Defines the role, goal, and backstory of each agent.
- `blog_writing_crew/config/tasks.yaml` - Defines the workflow of the project, including the task sequence and expected output.
- `agents/` - Folder containing agent JSON definitions used by the CrewAI JSON project format.
- `output/` - Folder where generated content is saved, such as blog posts and social media outputs.
- `knowledge/` - Optional knowledge files that can help give the agents extra context.
- `README.md` - Project documentation and learning notes.

### Files most likely to be edited

- `blog_writing_crew/config/agents.yaml` - Update agent personas, goals, or backstories.
- `blog_writing_crew/config/tasks.yaml` - Modify task instructions or expected outputs.
- `blog_writing_crew/crew.py` - Connect new agents and tasks to the CrewAI project.
- `.env` - Update the Gemini API key and chosen model.
- `blog_writing_crew/main.py` - Change the topic or startup input for the crew.
- `crew.jsonc` - Ensure the JSON crew definition matches the YAML/Python configuration.

### Notes for running the project

1. Install dependencies with the project environment.
2. Make sure the Gemini API key is valid in `.env`.
3. Run the project using CrewAI CLI.
4. Check the generated output in the `output/` folder.

