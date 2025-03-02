# SummarizeDocsProject Crew  

Welcome to **SummarizeDocsProject Crew**, developed by **Matheus Borges** using [crewAI](https://crewai.com). This project leverages a multi-agent AI system to efficiently read and summarize documents using a **custom tool** powered by the **Docling** library.  

## 🚀 Project Overview  

The **SummarizeDocsProject Crew** consists of three key agents working in sequence:  

1. **Reading Agent** 📖  
   - Uses a **custom tool** built with the **Docling** library to read and process the document.  
   - Extracts the full text from the document for further processing.  

2. **Summarization Agent** ✍️  
   - Receives the extracted text from the **Reading Agent**.  
   - Identifies and condenses the main points of the document.  

3. **Writing Agent** 📝  
   - Takes the summarized content from the **Summarization Agent**.  
   - Generates a well-structured and refined summary for the final output.  

## ⚙️ Technologies Used  

- **crewAI** – Multi-agent framework for AI-powered task automation.  
- **Docling** – Library for document reading and processing.  
- **Custom Tool** – Designed to integrate **Docling** with the **Reading Agent**.  

## 🎯 Goal  

The goal of this project is to automate document analysis by enabling AI agents to read, summarize, and generate structured summaries with high accuracy.  

Stay tuned for updates and improvements! 🚀  

## 📂 Project Structure
    summarize_docs_project/
    ├── .gitignore
    ├── pyproject.toml
    ├── README.md
    ├── .env
    └── src/
        └── summarize_docs_project/
            ├── __init__.py
            ├── main.py
            ├── crew.py
            ├── tools/
            │   ├── custom_tool.py
            │   └── __init__.py
            └── config/
                ├── agents.yaml
                └── tasks.yaml

## 🛠 Installation  

1. **Clone the repository**  
   ```sh
   git clone https://github.com/your-username/SummarizeDocsProject.git
   cd SummarizeDocsProject
   
Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/summarize_docs_project/config/agents.yaml` to define your agents
- Modify `src/summarize_docs_project/config/tasks.yaml` to define your tasks
- Modify `src/summarize_docs_project/crew.py` to add your own logic, tools and specific args
- Modify `src/summarize_docs_project/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the summarize_docs_project Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `summarize.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The summarize_docs_project Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.


## **📜 Licença**

Este projeto é de código aberto sob a licença **MIT**.

## **💬 Contato**

📧 **Email:** borgesmatheus1201@email.com  
🐍 **GitHub:** [borges12matheus](https://github.com/borges12matheus)  
🔗 **LinkedIn:** [matheusborges12](https://www.linkedin.com/in/matheusborges12/)  

