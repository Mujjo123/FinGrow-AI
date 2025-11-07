# 💰 FinGrow AI 🚀  

**FinGrow AI** is a **comprehensive AI-powered personal finance advisor** that combines various intelligent features including **chatbot capabilities, financial analysis, and much more**. Built with a **modern tech stack**, it features a **React frontend** and a **Python Flask backend**.  

## 📽️ Demo

<video width="640" height="360" controls>
  <source src="demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## 🌟 Features  

✅ **AI-powered Financial Assistant** 🤖 with **LLM integration**  
📊 **Financial Path Planning** - Visual investment strategy generator 🗺️  
📈 **Stock Analyzer** - Real-time stock price analysis and historical data 📊  
🗣️ **Speech processing capabilities** 🎙️  
📰 **News aggregation & display** 🌍  
🔐 **Secure authentication** 🔑  
📊 **Clean visual dashboard** to summarize all your financial data 📉  
📂 **MyData tab** to update your financial information ✏️  
💡 **Recommendations tab** for the best investment options 💰  
📚 **Money Matters** – Learn about finance 🏦  
🧮 **Income Tax Calculator** – Calculate your tax liability based on Indian tax slabs 📅  
🧠 **AI Agent** – Get real-time financial insights using web & APIs 🌐  
🚀 **Money Plus** – Real-time financial news updates 📰  

---

## 🛠️ Tech Stack  

### 🎨 Frontend  
⚛️ **React (TypeScript)**  
🎨 **Tailwind CSS** for styling  
⚡ **Vite** as the build tool  
✅ **ESLint** for code quality  
🔄 **React Router** for navigation  
📊 **Recharts** for data visualization  

### 🖥️ Backend  
🐍 **Python Flask**  
🧠 **Google's Gemini AI**  
🤖 **Langchain** for AI agent implementation  
🔍 **yfinance** for stock data  
🦆 **DuckDuckGo Search** for web search  
💻 **Python REPL** for code execution  

---

## 📋 Prerequisites  

🖥️ **Node.js** (v16 or higher)  
🐍 **Python** (3.8+)  
📦 **npm** or **yarn**  
🔑 **Required API keys** (Gemini, etc.)  

---

## 🔧 Installation  

### 🖥️ Backend Setup  
1️⃣ Navigate to the backend directory:  
   ```bash
   cd backend
   ```  
2️⃣ Create and activate a virtual environment (recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```  
3️⃣ Install Python dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
4️⃣ Install additional required packages:
   ```bash
   pip install langchain-experimental ddgs yfinance
   ```
5️⃣ Set up **environment variables**:  
   - Create a `.env` file in the backend directory  
   - Add your **Google Gemini API key**: `GEMINI_API_KEY=your_api_key_here`

### 🎨 Frontend Setup  
1️⃣ Navigate to the frontend directory:  
   ```bash
   cd frontend
   ```  
2️⃣ Install dependencies:  
   ```bash
   npm install
   # or
   yarn install
   ```  
3️⃣ Set up **environment variables**:  
   - Create a `.env` file in the frontend directory  
   - Add necessary **configuration variables**  

---

## 🚀 Running the Application  

### 🖥️ Backend  
1️⃣ From the backend directory:  
   ```bash
   python app.py
   ```  
   ✅ The backend server will start on **http://localhost:5000**  

### 🎨 Frontend  
1️⃣ From the frontend directory:  
   ```bash
   npm run dev
   # or
   yarn dev
   ```  
   ✅ The frontend development server will start on **http://localhost:5173**  

---

## 🎯 Using the Application  

Once both servers are running, open your browser and navigate to **http://localhost:5173** to access the application.

### Main Features:

#### 1. **Financial Path Planner**
- Navigate to the "Financial Path" section
- Describe your investment goals and risk tolerance
- Get a visual flowchart of recommended investment strategies

#### 2. **AI Financial Assistant**
- Go to the "AI Assistant" section
- Ask questions like:
  - "What is the stock price of Adani Green?"
  - "Give me last 3 days stock price of TCS"
  - "What is the current time?"
- Get real-time financial information and analysis

#### 3. **Stock Analyzer**
- Visit the "Stock Analyzer" section
- Enter company names to get real-time stock prices
- View historical price data and basic analysis

#### 4. **Income Tax Calculator**
- Go to "My Data" → "Income" tab
- Add your income sources
- Click "Calculate Tax" to see your tax liability based on current Indian tax slabs

---

## 🔑 Environment Variables  

### ⚙️ Backend (`.env`)  
🔹 **GEMINI_API_KEY** - Google Gemini API key for AI features

### ⚙️ Frontend (`.env`)  
🔹 **VITE_API_URL** - Backend API URL (default: http://127.0.0.1:5000)
🔹 **Other frontend-specific configurations**  

---

## 📁 Project Structure  

```
FinGrow AI/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── agent.py            # AI agent implementation
│   ├── gemini_fin_path.py  # Financial path generation module
│   ├── tools/              # Utility functions and tools
│   │   └── mytools.py      # Financial tools (stock data, calculations, etc.)
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── src/                # React source files
│   │   ├── pages/          # Main page components
│   │   ├── components/     # Reusable UI components
│   │   └── utils.ts        # Utility functions
│   ├── public/             # Static assets
│   └── package.json        # Frontend dependencies
```

---

## 👥 Authors  

- 🚀 [Mujaffar Mujawar](https://www.linkedin.com/in/mujaffar-mujawar-636a251a6/)  
- 🤖 [Gayatri Nalavade](https://www.linkedin.com/in/gayatri-nalavade-578609262/)  
- 📈 [Navneet Kamurti](https://www.linkedin.com/in/navneet-kamurti-651124289/)
- 🧠 [Neeraj Adam](https://linkedin.com/in/neerajadam)  

---

## 🙏 Acknowledgments  

- 🧠 **Google Gemini AI**  
- 🤖 **Langchain**  
- 🔗 **yfinance** for stock data  
- 🦆 **DuckDuckGo** for search capabilities  
- 🎨 **Tailwind CSS** for styling  

---

## 📜 License

This project is licensed under a modified MIT License with an additional consent requirement. For personal or non-commercial use, you must obtain explicit written consent from the project owner.

See the [LICENSE](./LICENSE) file for details.