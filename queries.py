from constants import JOB_NAME, OPEN_AI_API_KEY


def generate_search_query(user_problem, result_nums=3):
    query = f"""SELECT * FROM vectorize.search(
                job_name => '{JOB_NAME}',
                return_columns => ARRAY['title', 'question', 'responses'],
                query => '{user_problem}',
                api_key => '{OPEN_AI_API_KEY}',
                num_results => {result_nums}
                );"""
    return query


def create_queried_txt(db_responses):
    result = ""

    for index, (response, *other_values) in enumerate(db_responses):
        if isinstance(response, dict):
            result += f"Title {index + 1}: {response['title']}\n"
            result += f"Question {index + 1}: {response['question']}\n"

            for i, resp_text in enumerate(response['responses']):
                result += f"Response {i + 1}: {resp_text}\n"

            if index < len(db_responses) - 1:
                result += "\n\n\n"

    return result

