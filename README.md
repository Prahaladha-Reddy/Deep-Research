# Deep Research

Deep Research is a powerful, AI-driven application that automatically generates comprehensive reports on any given topic. By leveraging a multi-agent system, it can plan, research, and write detailed reports with citations, providing a seamless experience for users who need in-depth information quickly.

## Best Features

- **Autonomous Report Generation**: Simply provide a topic, and Deep Research will handle the rest. It autonomously plans the report structure, conducts web research, and writes each section.
- **Multi-Agent Architecture**: The system is built on a sophisticated multi-agent architecture using `langgraph`. This allows for parallel processing of tasks, such as writing different sections of the report simultaneously, which significantly speeds up the report generation process.
- **Dynamic Report Structure**: The application dynamically generates a report plan based on the topic, ensuring that the final report is well-organized and covers all the necessary sub-topics.
- **Web-Sourced Information**: Deep Research uses the Tavily API to gather up-to-date information from the web, ensuring that the generated reports are based on the latest available data.
- **Extensible and Modular**: The project is designed with a modular architecture, making it easy to extend and customize. You can easily modify the prompts, add new agents, or change the report generation logic to suit your needs.

## How It Works

The application is built using FastAPI for the backend API and Streamlit for the user interface. Here's a high-level overview of the report generation process:

1.  **API Request**: The process starts when a user sends a POST request to the `/generate_report/` endpoint with a specific topic.
2.  **Report Planning**: The `PlannerAgent` receives the topic and generates a comprehensive plan for the report. This includes defining the sections, determining which sections require web research, and generating search queries.
3.  **Web Research**: For sections that require research, the system uses the Tavily API to search the web for relevant information. The search results are then formatted and used as context for writing the report.
4.  **Section Writing**: The system uses a combination of parallel and sequential processing to write the different sections of the report. Sections that require web research are written in parallel, while sections that don't (like the introduction and conclusion) are written sequentially using the content of the other sections as context.
5.  **Report Compilation**: Once all the sections are written, the system compiles them into a single, well-formatted Markdown report.
6.  **API Response**: The final report is returned in the API response.

## Getting Started

### Prerequisites

- Python 3.10+
- Docker

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Prahaladha-Reddy/Deep-Research.git
    cd Deep-Research
    ```

2.  Create a `.env` file in the root directory and add your API keys:

    ```
    GOOGLE_API_KEY="your-google-api-key"
    TAVILY_API_KEY="your-tavily-api-key"
    ```

3.  Build and run the Docker container:

    ```bash
    docker build -t deep-research .
    docker run -p 8000:8000 deep-research
    ```

### Usage

Once the Docker container is running, you can send a POST request to the `/generate_report/` endpoint to generate a report. Here's an example using `curl`:

```bash
curl -X POST "http://localhost:8000/generate_report/" -H "Content-Type: application/json" -d '{"topic": "The future of AI in healthcare"}'
```

You can also use the Streamlit interface to interact with the application. To run the Streamlit app, you'll need to install the dependencies and run the `streamlit_app.py` file:

```bash
# Install dependencies
uv sync

# Run the Streamlit app
streamlit run streamlit_app.py
```
