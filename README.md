# 🤖 AI HR Analytics Dashboard

An AI-powered HR Analytics Dashboard that enables users to ask HR-related questions in natural language. The application automatically converts questions into SQL queries using a Large Language Model (Ollama), executes them on a MySQL database, visualizes the results with interactive charts, and generates AI-driven business insights.

---

## 🚀 Features

- 🤖 Natural Language to SQL using Ollama
- 🗄️ MySQL Database Integration
- 📊 Interactive Dashboard with KPI Cards
- 📈 Automatic Data Visualization (Chart.js)
- 💡 AI-generated HR Insights
- 📋 Query Results Table
- 📥 Export Results to CSV
- 📝 Generated SQL Display
- 📱 Responsive User Interface
- 📌 Recent Question History

---

## 📸 Screenshots

### Dashboard

> Add your dashboard screenshot here.

```
screenshots/dashboard.png
```

### AI Generated SQL

> Add SQL screenshot here.

```
screenshots/sql.png
```

### Visualization

> Add chart screenshot here.

```
screenshots/chart.png
```

### AI Insight

> Add insight screenshot here.

```
screenshots/insight.png
```

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Database
- MySQL

### AI
- Ollama
- Llama 3.2

### Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js

---

## 📂 Project Structure

```
AI-HR-Analytics/
│
├── app.py
├── sql_generator.py
├── sql_executor.py
├── insight_generator.py
├── utils.py
├── requirements.txt
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── screenshots/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/gokulraj-333/AI-HR-Analytics.git
```

```bash
cd AI-HR-Analytics
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Start Ollama

```bash
ollama serve
```

### Pull Model

```bash
ollama pull llama3.2:3b
```

### Configure MySQL

Update your database configuration inside:

```
sql_executor.py
```

### Run Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 💬 Example Questions

- How many employees are in each department?
- Show average salary by department.
- Which department has the highest attrition?
- Show gender distribution.
- Top 10 highest-paid employees.
- Average job satisfaction by department.
- Employees working overtime.
- Performance rating by department.

---

## 📊 Dashboard Includes

- Total Employees
- Active Employees
- Employees Left
- Attrition Rate
- Average Salary
- Performance Rating
- Job Satisfaction
- Average Years at Company

---

## 💡 How It Works

1. User enters an HR-related question.
2. Ollama converts the question into SQL.
3. Flask executes the SQL query on MySQL.
4. Results are displayed in a table.
5. Chart.js visualizes the results.
6. Ollama generates HR insights and recommendations.

---

## 🎯 Skills Demonstrated

- Python
- Flask
- MySQL
- SQL
- Prompt Engineering
- REST APIs
- Data Visualization
- Business Analytics
- AI Integration
- Dashboard Development

---

## 🔮 Future Enhancements

- PDF Report Export
- Excel Export
- Authentication
- Department Filters
- Multiple Chart Types
- Advanced AI Analytics
- Cloud Deployment

---

## 👨‍💻 Author

**Gokul Raj R S**

GitHub: https://github.com/gokulraj-333

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
