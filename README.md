# English-to-Finnish Translator

This project is an English-to-Finnish translation Demo based on Flask and Hugging Face Transformers. Users can input English text via a simple web interface and get the corresponding Finnish translation.

## Installation and Execution

Follow these steps to install and run the project:

### 1. Clone the Project

```bash
git clone <your_project_url>
cd <project_directory>
```

### 2. Install Dependencies

Ensure your system has Python 3.7 or later installed, then run the following command:

```bash
pip install flask transformers torch
```

#### Dependency List and Installation Commands

- **Flask**: Used to create the backend server.

  ```bash
  pip install flask
  ```

- **Transformers**: Hugging Face library for loading the translation model.

  ```bash
  pip install transformers
  ```

- **Torch**: PyTorch support required for some Transformers models.

  ```bash
  pip install torch
  ```

- **Tokenizers** (optional): For efficient text tokenization.

  ```bash
  pip install tokenizers
  ```

- **Requests** (commonly pre-installed): For handling HTTP requests.

  ```bash
  pip install requests
  ```

- **Note**: If you have a `requirements.txt` file, you can install all dependencies at once with:

  ```bash
  pip install -r requirements.txt
  ```

  Example `requirements.txt` content:

  ```
  flask
  transformers
  torch
  tokenizers
  requests
  ```

### 3. Start the Server

Run the following command to start the Flask server:

```bash
python app.py
```

The server will start and be accessible at `http://127.0.0.1:5000/en_fi`.

### 4. Access the Application

Open your browser and visit `http://127.0.0.1:5000/en_fi` to use the translation feature.

## Technical Details

- **Backend**
  - Built using the Flask framework.
  - Utilizes the Hugging Face `Helsinki-NLP/opus-mt-en-fi` model for English-to-Finnish translation.
  - Exposes an API endpoint `/translater` for handling translation requests.

- **Frontend**
  - Built with HTML, CSS, and JavaScript.
  - JavaScript uses the `fetch` API to send POST requests, passing user input to the backend and receiving the translation result.

## How to Use

1. Enter the English text you wish to translate in the text box.
2. Click the "Compute" button.
3. Wait for the translated result to appear in the "translated content here" area.

## Notes

- **Model Download**

  - The Transformers library will automatically download the `Helsinki-NLP/opus-mt-en-fi` model on first run, which may take some time. Please be patient.

- **Network Connection**

  - Ensure a stable internet connection to download the model and dependencies.

- **System Performance**

  - Translation speed depends on system performance, typically taking 2-4 seconds.

- **Python Version**

  - Use Python 3.7 or newer.
