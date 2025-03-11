import streamlit as st
from rag_pipline import get_rag_response

# Page title and configuration
st.set_page_config(page_title="Dyslexia Diagnosis Assistant", layout="wide")
st.title("Dyslexia Diagnosis Assistant(Parents Portal)")

# Create two columns
left_col, right_col = st.columns(2)
user_input=""
# Left column - User input
with left_col:
    st.subheader("Dyslexia Assessment Inputs")
    
    # Three slider questions
    st.write("Please rate the following on a scale of 0-10:")
    
    reading_difficulty = st.slider(
        "Q1: Does your child struggle to recognize letters even after repeated exposure?",
        min_value=0,
        max_value=10,
        value=5,
        help="0 = No difficulty, 10 = Extreme difficulty"
    )
    
    reading_difficulty1 = st.slider(
        "Q2: Does your child mix up similar-looking letters (e.g., b and d, p and q)?",
        min_value=0,
        max_value=10,
        value=5,
        help="0 = No issues, 10 = Severe issues"
    )
    phonic_difficulty = st.slider(
        "Q3: Does your child struggle to match letters with their sounds? (e.g., knowing that b sounds like buh)?",
        min_value=0,
        max_value=10,
        value=5,
        help="0 = No issues, 10 = Severe issues"
    )
    phonic_difficulty1 = st.slider(
        "Q4: Does your child have difficulty pronouncing new or unfamiliar words?",
        min_value=0,
        max_value=10,
        value=5,
        help="0 = No issues, 10 = Severe issues"
    )
    visual_speed = st.slider(
        "Q5: Does your child have trouble tracking words while reading (e.g., skipping lines, losing place)?",
        min_value=0,
        max_value=10,
        value=5,
        help="0 = Very fast, 10 = Very slow"
    )
    visual_speed1 = st.slider(
        "Q6: Does your child struggle with distinguishing between similar-looking words (e.g., was vs. saw)?",
        min_value=0,
        max_value=10,
        value=5,
        help="0 = Very fast, 10 = Very slow"
    )
    memory_speed = st.slider(
        "Q7:Does your child forget words they just learned?",
        min_value=0,
        max_value=10,
        value=5,
        help="0 = Very fast, 10 = Very slow"
    )
    memory_speed1 = st.slider(
        "Q8: Does your child have difficulty remembering the correct sequence of letters in a word?",
        min_value=0,
        max_value=10,
        value=5,
        help="0 = Very fast, 10 = Very slow"
    )
    
    # Additional context (optional)
    additional_context = st.text_area(
        "Additional context or observations (optional):",
        height=100
    )
    
    # Generate query based on slider values
    if st.button("Generate Assessment"):
        # Formulate the input for the model based on slider values
        user_input = f"""
        Assessment request for potential dyslexia:


        Q1: Difficulty recognizing letters after repeated exposure: {reading_difficulty}/10

        Q2: Mixing up similar-looking letters (e.g., b and d, p and q): {reading_difficulty1}/10

        Q3: Difficulty matching letters with their sounds: {phonic_difficulty}/10

        Q4: Struggles with pronouncing new or unfamiliar words: {phonic_difficulty1}/10

        

        Q5: Trouble tracking words while reading (e.g., skipping lines, losing place): {visual_speed}/10

        Q6: Difficulty distinguishing between similar-looking words (e.g., was vs. saw): {visual_speed1}/10

        Q7: Forgetting words they just learned: {memory_speed}/10

        Q8: Difficulty remembering the correct sequence of letters in a word: {memory_speed1}/10

        Additional observations:
        {additional_context}

        Please provide an assessment based on these indicators.
        """

# Right column - Response area (creates the area before the button is clicked)
with right_col:
    st.subheader("AI Powered Doctor Suggession")
    response_container = st.empty()


# Process the request when button is clicked
if user_input:
        # Initialize the response container with a "thinking" message
        response_container.write("Generating response...")
        
        # Get the full response from your RAG pipeline
        full_response = get_rag_response(user_input)
        
        # Simulate streaming by displaying chunks of the response
        # (since Streamlit doesn't have built-in streaming like Gradio)
        response_text = ""
        for i in range(len(full_response)):
            # Add one character at a time to simulate streaming
            response_text += full_response[i]
            # Update the response container with current text
            response_container.write(response_text)
            # Small delay to make the streaming visible
            if i % 3 == 0:  # Only add delay every few characters for performance
                import time
                time.sleep(0.01)
else:
        response_container.warning("Please Provide Assessment details for AI-Powered Solution")