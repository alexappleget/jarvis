import os

def create_file(filename: str):
  base_directory = r"C:\My Projects"
  file_name = f"{filename}.md"
  file_path = os.path.join(base_directory, file_name)
  hardcoded_content = "# This is a Markdown file created by Jarvis."

  try:
    with open(file_path, "w", encoding="utf-8") as file:
      file.write(hardcoded_content)
    
    return {"success": True, "message": f"File '{file_path}' created."}

  except Exception as error:
    print(f"Error in creating file: {error}")