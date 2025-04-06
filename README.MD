# RAG System for Colombian Geographic Data

This project implements a Retrieval Augmented Generation (RAG) system to provide information about Colombian geography, specifically departments and their capitals. This README explains how to run the application, the development process, important considerations, and a proposed cloud deployment strategy using Azure.

## Table of Contents

* [How to Run](#how-to-run)
* [Project Description](#project-description)
* [Development Process](#development-process)
* [Important Considerations](#important-considerations)
* [Pylint and Prettier](#pylint-and-prettier)
* [Proposed Cloud Deployment (Azure)](#proposed-cloud-deployment-azure)
* [Git Workflow](#git-workflow)

## How to Run

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/VictorManuelRodriguezDelahoz-IA/LLM-Wikipedia-search-region.git

    cd LLM-Wikipedia-search-region
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv .venv
    # Or, if you use conda:
    # conda create -n .venv python=3.13
    ```

3.  **Activate the virtual environment:**

    ```bash
    # On Windows:
    .venv\Scripts\activate
    # On macOS and Linux:
    source .venv/bin/activate
    ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the main script:**

    ```bash
    python main.py "¿Cuál es la capital de Antioquia?"
    ```

    **Note:** **Note:** The query should be passed as a command-line argument.

## Project Description

This project aims to create a system that can answer user queries about Colombian geography using a RAG approach. The system works by:

1.  **Scraping data** from a Wikipedia page.
2.  **Processing the extracted data.**
3.  **Generating embeddings** (vector representations) of the processed data.
4.  **Storing the embeddings** in a vector database.
5.  **Retrieving relevant data** from the vector database based on a user query.
6.  **Generating a response** (in this implementation, a simple extraction of relevant information) using the retrieved data.

## Development Process

The development of this RAG system followed these steps:

1.  **Data Acquisition (Scraping):**
    * Scraped data from the specified Wikipedia page using `requests` and `BeautifulSoup`.
    * Extracted the relevant table containing department and capital information.

2.  **Data Processing:**
    * Cleaned and transformed the extracted data using `pandas`.
    * Formatted the data into a list of strings, where each string represents a "document" for embedding.

3.  **Embedding Generation:**
    * Utilized the `sentence-transformers` library and a pre-trained model ('all-MiniLM-L6-v2') to generate embeddings for the prepared data.

4.  **Vector Database Storage:**
    * Employed ChromaDB to store the generated embeddings along with their corresponding text data.
    * ChromaDB was configured to store the database on disk for persistence during development.

5.  **Retrieval Function:**
    * Implemented a function to:
        * Generate an embedding for a user query.
        * Query the ChromaDB vector database for the most similar embeddings.
        * Retrieve the corresponding text data (documents).

6.  **RAG Agent (Simple Generation):**
    * Created a simple "generation" function to present the retrieved documents as context for the user's query.
    * This implementation focuses on presenting the retrieved information rather than generating a complex, synthesized answer.

7.  **Code Modularization:**
    * Refactored the code into a modular structure with separate `.py` files for each component (data loading, embedding, vector database interaction, retrieval, and generation).
    * This improved code organization, readability, and maintainability.

8.  **Code Linting and Formatting:**
    * Integrated Pylint for code linting and Prettier for code formatting.
    * Ensured code quality and consistency.

9.  **Dockerization:**
    * Created a Dockerfile to package the application and its dependencies into a container.
    * This facilitates easy deployment and ensures consistent execution across different environments.

10. **Web Exposure (Considerations):**
    * The current implementation is designed for command-line execution.
    * To expose this as a web service, a framework like Flask or FastAPI would be needed to create an API endpoint.

11. **Git Workflow:**
    * Used Git for version control.
    * Organized changes into logical commits.
    * (In a team environment) would use branching strategies (e.g., Gitflow) for collaborative development.

## Important Considerations

* **Data Source Reliability:** The accuracy and completeness of the RAG system depend heavily on the Wikipedia page. Future improvements could involve using multiple data sources and validation techniques.
* **Query Complexity:** The current retrieval and generation methods are limited in their ability to handle complex or nuanced queries. More advanced retrieval algorithms and language models would be needed for more sophisticated queries.
* **Scalability:** The current ChromaDB implementation stores the database locally. For production use, a scalable vector database service (e.g., Pinecone, Milvus) would be necessary.
* **Context Window Limits:** When using more advanced language models for response generation, it's crucial to consider the context window limits of those models and implement strategies for handling long documents or conversations.

## Pylint and Prettier

* **Pylint:**
    * Used for static code analysis to identify potential errors, stylistic issues, and code quality concerns.
    * Enforces coding standards and best practices.
    * Requires manual code modifications to address the reported issues.
* **Prettier:**
    * Used for automatic code formatting to ensure consistent code style (e.g., line length, indentation, quotes).
    * Improves code readability and maintainability.
    * Automatically formats the code according to predefined rules.

## Proposed Cloud Deployment (Azure)

To deploy this RAG system in the cloud using Azure, the following architecture and services could be considered:

1.  **Azure Container Registry (ACR):**
    * Store the Docker image of the application.

2.  **Azure Kubernetes Service (AKS):**
    * Orchestrate and scale the application containers.
    * AKS provides a managed Kubernetes environment, simplifying deployment and management.

3.  **Azure Cognitive Search (or Azure Cosmos DB for vector search):**
    * Replace the local ChromaDB database with a scalable and managed vector search solution.
    * Azure Cognitive Search has vector search capabilities, or you could use a Cosmos DB database with vector search extensions. This would provide the necessary performance and scalability for production.

4.  **Azure App Service or Azure Functions:**
    * Provide a web API endpoint for user queries.
    * Flask or FastAPI applications can be deployed to Azure App Service or Azure Functions to handle HTTP requests and interact with the RAG system.

5.  **Azure Monitor:**
    * Monitor the application's performance, health, and logs.


## Git Workflow

A typical Git workflow for this project (especially in a collaborative setting) would involve:

* **Branching:**
    * Using a branching strategy like Gitflow (e.g., `main`, `develop`, feature branches).
    * Creating feature branches for new features or bug fixes.
* **Committing:**
    * Writing clear and concise commit messages.
    * Grouping related changes into logical commits.
* **Pull Requests:**
    * Using pull requests for code review and merging changes into the `develop` or `main` branch.
* **Code Review:**
    * Reviewing code for correctness, style, and potential issues.
    * Ensuring that the code adheres to the defined linting and formatting rules.

This README provides a comprehensive overview of the RAG system, its development, and a proposed cloud deployment strategy. It should be helpful for understanding the project and its architecture.