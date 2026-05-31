from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from llm.schema import passport_info


info_extraction_template = ChatPromptTemplate.from_template(
    """
    you are a helpful assistant for extracting information from passport.

    OCR text:
    {ocr_text}

    Please extract the following information from the passport: {format_instructions}
    
    Rules:
    - Don't add anything before and after in JSON format give me **JSON format only**.
    - Do not **hallucinate or fabricate information**; only extract what is explicitly stated in the text.
    - Do not add any extra information or modify the schema.
    - If any of the required fields are missing in the OCR text, return None for those fields in the JSON output.
    """)

