# EzeCrypto - AI-Powered Cryptocurrency Insights Chatbot

EzeCrypto is a lightweight Flask-based chatbot that offers intelligent insights and summaries about popular cryptocurrencies. It helps users explore eco-friendly coins, track trending cryptocurrencies, get long-term investment suggestions, and access market overviews—all via a conversational interface.

## Features

- **Chat-based Interface**: Ask questions about crypto trends, prices, sustainability, or investment suggestions.
- **Real-Time Analysis**: Get curated responses based on pre-defined cryptocurrency data.
- **Sustainability Focus**: Highlight eco-friendly coins using sustainability scores and energy efficiency.
- **Full Market Summary**: Access a structured JSON summary of crypto data, ideal for visualizations or analytics.
- **Health Endpoint**: Check server status and availability.

---

## Project Structure

ezecrypto/
├── app.py # Main Flask application
├── paste.txt # (Optional) HTML interface file
├── README.md # Project documentation

## Getting Started
Follow the steps below to set up the project locally:
1. **Clone the Repository**
```bash
Copy code
git clone https://github.com/octaviav/AI-4-SE.git
cd ezecrypto
```

2. **Run the Server**
```bash
Copy code
python app.py
```

3. Once started, open your browser and go to:
 http://localhost:5000.

## API Endpoints
POST /chat
Send a message to the chatbot and receive a contextual response.

## Example Request
```bash
Copy code
curl -X POST http://localhost:5000/chat \
-H "Content-Type: application/json" \
-d '{"message": "show me sustainable coins"}'

## Example Response
json
Copy code
```{
  "success": true,
  "response": {
    "message": "🌱 Here are the most sustainable cryptocurrencies...",
    "type": "text"
  }
}```

GET /full_summary
Returns a detailed JSON summary of all cryptocurrencies and statistics.

```bash
Copy code
curl http://localhost:5000/full_summary
GET /health
Returns a basic health check and metadata.

```bash
Copy code
curl http://localhost:5000/health
🖥️ Optional: HTML Chat Interface
If you have a custom HTML UI (e.g., paste.txt), place it in the project root. It will be rendered when visiting the root route /.

## Example Use Cases
 Discover which cryptocurrencies are currently trending.

## Find out the most eco-friendly options for conscious investing.

## Get investment suggestions tailored to long-term goals.

Use full_summary to power dashboards or reports.

# License
This project is licensed under the MIT License.

# Powered by
Python & Flask

JSON-based local dataset

Custom NLP logic for smart keyword detection
