import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "llama3.2:3b"


def generate_sql(question):

    prompt = f"""
You are an expert MySQL developer.

Database Name:
HR

Table Name:
Employees

Columns:
EmployeeNumber
Age
Attrition
BusinessTravel
DailyRate
Department
DistanceFromHome
Education
EducationField
EmployeeCount
EnvironmentSatisfaction
Gender
HourlyRate
JobInvolvement
JobLevel
JobRole
JobSatisfaction
MaritalStatus
MonthlyIncome
MonthlyRate
NumCompaniesWorked
Over18
OverTime
PercentSalaryHike
PerformanceRating
RelationshipSatisfaction
StandardHours
StockOptionLevel
TotalWorkingYears
TrainingTimesLastYear
WorkLifeBalance
YearsAtCompany
YearsInCurrentRole
YearsSinceLastPromotion
YearsWithCurrManager

Rules:

1. Return ONLY MySQL.
2. No explanation.
3. No markdown.
4. No ```sql```.
5. Use Employees table only.
6. Generate valid MySQL 8 syntax.

Question:

{question}

SQL:
"""

    response = requests.post(

        OLLAMA_URL,

        json={

            "model": MODEL,

            "prompt": prompt,

            "stream": False

        }

    )

    response.raise_for_status()

    sql = response.json()["response"].strip()

    return sql