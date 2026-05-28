from llm.chain import Groq_client
from llm.prompt import info_extraction_template
from langchain_core.output_parsers import PydanticOutputParser, JsonOutputParser
from llm.schema import passport_info

 
def generate_response(ocr_text: str) -> str:
    """Generate a response from the LLM based on the given prompt."""
    try:

        parser = PydanticOutputParser(pydantic_object=passport_info)
        format_instructions = parser.get_format_instructions()

        message = info_extraction_template.format_messages(
            ocr_text=ocr_text,
            format_instructions=format_instructions
        )
        response = Groq_client.invoke(message)
        return response.content
    except Exception as e:
        print(f"Error occurred while generating response: {e}")
        return None

        # llm_chain = info_extraction_template | Groq_client  | JsonOutputParser()