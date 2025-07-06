# 🧬Latex Homework Generator

This Python script leverages the **LLaMA 3.2** model (via a local Ollama server) to generate a **LaTeX-formatted biology homework assignment** based on a lecture transcript. The output is compiled into a clean, printable PDF using `pdflatex`.

---

## 📁 Features

- **Input**: Processes a biology lecture transcript provided in the script’s prompt.
- **Output**: Generates a LaTeX document (`homework.tex`) with 20 open-ended and fill-in-the-blank questions, compiled into `homework.pdf`.
- **Question Format**: Uses LaTeX’s `enumerate` environment for a numbered list of questions, each \~100 words.
- **Dependencies**: Requires Python, `pdflatex`, and a local Ollama server with LLaMA 3.2.

---

## 📦 Requirements

Before running the script, ensure the following are installed:

### 🧠 Model Infrastructure

- Ollama with the LLaMA 3.2 model:

  ```bash
  ollama pull llama3.2
  ollama run llama3.2
  ```

### 🐍 Python Libraries

Install required packages:

```bash
pip install requests pdflatex
```

### 📄 LaTeX

A LaTeX distribution is needed for `pdflatex`:

- **Windows**: MiKTeX
- **macOS**: MacTeX
- **Linux**:

  ```bash
  sudo apt install texlive-full
  ```

Ensure `pdflatex` is in your system’s PATH.

---

## 🚀 Usage

1. Start the Ollama server locally on `http://localhost:11434`.
2. Insert your biology lecture transcript into the `prompt` field in the script (replace `{transcript}`).
3. Run the script:

   ```bash
   python homework_generator.py
   ```

The script will:

- Query LLaMA 3.2 to generate a LaTeX document.
- Save the output as `homework.tex`.
- Compile it into `homework.pdf` using `pdflatex`.

---

## 📄 Output

- `homework.tex`: Raw LaTeX code with 20 formatted questions.
- `homework.pdf`: Compiled PDF with a clean, wide-spaced layout.

### 🧬 Example LaTeX Snippet

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\geometry{legalpaper, margin=1in}
\begin{document}
\section*{Biology Homework Assignment}
\begin{enumerate}
  \item Describe the role of enzymes in cellular metabolism.
  \item What is the significance of the Krebs cycle in energy production?
\end{enumerate}
\end{document}
```

---

## 🛠️ Notes

- Replace `{transcript}` in the script with a valid biology lecture transcript.
- The LaTeX output uses the `article` document class with `geometry` for wide margins and `enumerate` for question formatting.
- Avoids `//` in LaTeX code to ensure compatibility.
- The script streams LLaMA’s response to handle large outputs efficiently.
- Customize the LaTeX template in the prompt for styling or additional packages.

---

## 🔧 Troubleshooting

- **Ollama Error**: Confirm the Ollama server is running and LLaMA 3.2 is installed.
- **pdflatex Error**: Verify `pdflatex` is installed and in your system’s PATH.
- **LaTeX Syntax Issues**: Check `homework.tex` for errors if compilation fails, as LLaMA’s output may require manual correction.

---

## 📜 License

MIT License. See `LICENSE` file for details.

---
