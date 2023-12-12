# Mercedes-Benz AI 

## Overview
This chatbot serves as a resource for addressing issues related to Mercedes vehicles.
It utilizes a database of information collected from the MBworld blog, where Mercedes owners have shared their experiences and insights.
By tapping into this collective knowledge, the chatbot can offer you valuable solutions based on real-world experiences from the Mercedes community.
It functions as a virtual advisor, providing well-informed and practical responses to your Mercedes-related questions and problems.

This is based on [Tembo](https://tembo.io/) as the database which holds the data is being hosted by them,
and it's using [pg_vectorize](https://github.com/tembo-io/pg_vectorize) which one of their implementations (LLM-backed vector search on Postgres).

## Features
- Problem Diagnosis
- Maintenance Reminders
- DIY Repairs

## Demo
![Video Demo](mb-solutions-demo.mp4)
  
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- pip
- langchain
- openai
- streamlit
- huggingface-hub

### Installing

1. Clone the repository
> git clone https://github.com/olsihoxha/mb-solutions.git


2. Change into the project directory
> cd mb-solutions


3. Install the required packages
> pip install -r requirements.txt

4. Run the project 
>streamlit run main.py


### Constants 
To run this you have to replace the values of the variables below(found in `constants.py`) with your own keys:
```
OPEN_AI_API_KEY = '<your-key>'
HUGGING_FACE_API_KEY = '<your-key>'
```
