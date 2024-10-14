{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPTR5hJX4p1nm8VQy+agHva",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kalimriaz/test_qa/blob/main/test_qa.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "c4RhaRBipbJH"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "\n",
        "# Define the quiz questions and options as a list of dictionaries\n",
        "quiz = [\n",
        "    {\n",
        "        \"question\": \"1. What is the primary goal of software testing?\",\n",
        "        \"options\": [\"To find defects\", \"To improve the software's performance\", \"To meet user requirements\", \"To ensure compatibility with other systems\"],\n",
        "        \"answer\": \"To find defects\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"2. Which of the following is a non-functional testing type?\",\n",
        "        \"options\": [\"Unit testing\", \"System testing\", \"Load testing\", \"Integration testing\"],\n",
        "        \"answer\": \"Load testing\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"3. What does SDLC stand for?\",\n",
        "        \"options\": [\"Software Design Life Cycle\", \"System Development Life Cycle\", \"Software Development Life Cycle\", \"System Design Life Cycle\"],\n",
        "        \"answer\": \"Software Development Life Cycle\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"4. In which phase of SDLC is testing typically performed?\",\n",
        "        \"options\": [\"Planning\", \"Implementation\", \"Maintenance\", \"Testing\"],\n",
        "        \"answer\": \"Testing\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"5. What is a test case?\",\n",
        "        \"options\": [\"A document describing how to test a system\",\n",
        "                    \"A set of conditions under which a tester will determine if a feature works as expected\",\n",
        "                    \"A test plan\", \"A user manual\"],\n",
        "        \"answer\": \"A set of conditions under which a tester will determine if a feature works as expected\"\n",
        "    }\n",
        "]\n",
        "\n",
        "def run_quiz():\n",
        "    # Initialize score to 5\n",
        "    score = 5\n",
        "    st.title(\"Software Testing Basics Quiz\")\n",
        "    st.write(\"You start with 5 marks. Each correct answer gives you 1 mark. Each wrong answer deducts 1 mark.\\n\")\n",
        "\n",
        "    # Use a session state to track the score and quiz progress\n",
        "    if \"score\" not in st.session_state:\n",
        "        st.session_state.score = score\n",
        "\n",
        "    # Iterate through each question in the quiz\n",
        "    for idx, q in enumerate(quiz):\n",
        "        # Display question\n",
        "        st.write(q[\"question\"])\n",
        "\n",
        "        # Let user select an option\n",
        "        user_answer = st.radio(f\"Select your answer for Question {idx + 1}: \", q[\"options\"], key=f\"q{idx}\")\n",
        "\n",
        "        # Check if the answer is correct (only when the button is pressed)\n",
        "        if st.button(f\"Submit Answer for Question {idx + 1}\", key=f\"submit{idx}\"):\n",
        "            if user_answer == q[\"answer\"]:\n",
        "                st.success(\"Correct! You gain 1 mark.\")\n",
        "                st.session_state.score += 1\n",
        "            else:\n",
        "                st.error(f\"Wrong! The correct answer is {q['answer']}. You lose 1 mark.\")\n",
        "                st.session_state.score -= 1\n",
        "\n",
        "    # Show the final score\n",
        "    if st.button(\"Finish Quiz\"):\n",
        "        st.write(f\"Quiz finished! Your final score is {st.session_state.score} out of {5 + len(quiz)}.\")\n",
        "\n",
        "# Run the quiz\n",
        "run_quiz()\n"
      ]
    }
  ]
}