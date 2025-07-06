import requests
import json
import os
from pdflatex import PDFLaTeX
import subprocess



# === LLaMA API Configuration ===
url = 'http://localhost:11434/api/generate'


##Could use some training to make sure it pastes error-less code without the direct input of an example
data = {
    'model': 'llama3.2',
    'prompt': 'Given this lecture transcript {transcript}, create a 20 question, open ended homework assignment/reading guide to complement the lecture. Make sure it is in a LaTeX document. All open ended questions, and a few fill in the blanks. Make each question a small paragraph 100 words long. Make the horizontal spacing wide.'
              r"""Do not explain the output or how to use the output, only give the code and that is it. Do not contain any gibberish and only runnable LaTeX code that I can copy and paste to LaTeXOnline API. No explaination or intro. No images or diagrams. double check for missing characters and LaTeX syntax errors. Never use //. Use enumerate functionality to make questions in list format. Here is an example on how to correctly format Latex: 
              \documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{float} % For [H] placement of figures
\usepackage{geometry}
\geometry{legalpaper, margin=1in}
\begin{document}

\section*{Homework Assignment: Cell Mitosis}

\begin{enumerate}
  \item 
  \item 
  \item 
  \item 
  \item 
  \item 
\end{enumerate}

\end{document}
""",
    'stream': True  # streaming output
}

# === Call LLaMA and collect the LaTeX code ===
print("Generating LateX w/ Llama 3.2")
response = requests.post(url, json=data, stream=True)

if response.status_code == 200:
    latex_code = ""
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode("utf-8")
            result = json.loads(decoded_line)
            chunk = result.get("response", "")
            print(chunk, end="", flush=True)
            latex_code += chunk  # append the LaTeX content
    print("\n\nDone generating LaTeX. Now compiling to PDF...")
else:
    print("Error:", response.status_code, response.text)
    latex_code = None



texfile = open("homework.tex", "w")
texfile.write(latex_code)
texfile.close()

subprocess.run(["pdflatex", "homework.tex"], check=True)










r"""
def tex_to_pdf(tex_file):
    if not os.path.isfile(tex_file):
        print("There is no such file in your directory, try again")
        return

    subprocess.run(['pdflatex', tex_file], check=True)
    print("pdf compiled")
    ##except subprocess.CalledProcessError as e:
        ##print(f"Error during the converion: {e}")
    
##pdfl = PDFLaTeX.from_texfile('test3.tex')
##pdfl.set_interaction_mode()  # setting interaction mode to None.
##pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)

tex_file = 'test4.tex'
tex_to_pdf(tex_file)


"""


# === Function to convert LaTeX code to PDF ===
r"""
def latex_to_pdf(latex_code, output_file="document.pdf"):
    if not file:
        print("No LaTeX code provided.")
        return

    url = "https://latexonline.cc/data"
    payload = {
        "code": latex_code,
        "compiler": "pdflatex",
        "format": "pdf"
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        pdfFile = open(output_file, 'w')
        pdfFile.write(response.content)
        print(f"PDF saved to: {output_file}")
    else:
        print("Failed to compile LaTeX. Status code:", response.status_code)




# === Compile the generated LaTeX into a PDF ===
latex_to_pdf(latex_code, output_file="cell_mitosis_lesson_plan.pdf")

"""


