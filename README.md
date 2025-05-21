# 🗂️ Organizador de Arquivos em Python

Um script simples que **organiza automaticamente seus arquivos** com base no tipo (extensão).  
Feito com 💻 Python puro, para ajudar a manter suas pastas organizadas sem esforço.

---

## 🚀 Como funciona?

1. O programa verifica a pasta `bagunça/`
2. Ele identifica todos os arquivos lá dentro
3. Separa por tipo (PDF, JPG, TXT, etc.)
4. Cria pastas com base nas extensões
5. Move cada arquivo para sua devida pasta

---

## 📁 Exemplo visual

**ANTES:**
bagunça/
├── foto.jpg
├── nota.txt
├── relatorio.pdf


**DEPOIS:**

bagunça/
├── JPG/
│ └── foto.jpg
├── TXT/
│ └── nota.txt



---

## ▶️ Como usar

1. Crie uma pasta chamada `bagunça` e coloque os arquivos dentro
2. Execute o script:

```bash
python organizador.py
Pronto! Seus arquivos estarão organizados em subpastas!

🧠 Tecnologias usadas
Python 3.x

os e shutil (módulos padrão do Python)

📌 Aprendizados
Este projeto me ajudou a:

Entender como percorrer pastas com Python

Manipular arquivos e criar subpastas

Automatizar tarefas do dia a dia

👤 Autor
Wagner Teixeira
Desenvolvedor em formação, aprendendo passo a passo 💪

⭐ Curtiu?
Deixa uma ⭐ lá no repositório pra apoiar esse projeto simples e útil!


---

### ✅ Próximo passo:

1. Abre o projeto no VS Code ou no Bloco de Notas
2. Cria o arquivo `README.md`
3. Cola esse conteúdo
4. Salva
5. Depois, no Git Bash, roda:

```bash
git add README.md
git commit -m "Adiciona README bonito com emojis"
git push origin main

