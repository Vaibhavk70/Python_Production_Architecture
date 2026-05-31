from llm.chain import Groq_client
from llm.prompt import info_extraction_template
from langchain_core.output_parsers import PydanticOutputParser, JsonOutputParser
from llm.schema import passport_info
import json

 
def generate_response(ocr_text: str) -> str:
    """Generate a response from the LLM based on the given prompt."""
    try:
        # Create an output parser for the passport_info schema
        parser = PydanticOutputParser(pydantic_object=passport_info)
        format_instructions = parser.get_format_instructions()

        # Format the prompt with the OCR text and the format instructions
        prompt = info_extraction_template.format(
            ocr_text=ocr_text,
            format_instructions=format_instructions
        )

        # Invoke the LLM with the formatted prompt and parse the response
        response = Groq_client.invoke(prompt)
        
        # Validate response content
        if not response or not response.content or not response.content.strip():
            print("Error: Empty response from LLM")
            return None
        
        print(f"LLM Response: {response.content}")
        response_dict = json.loads(response.content)
        return response_dict
    
    except json.JSONDecodeError as je:
        print(f"Error decoding JSON response: {je}")
        return None
