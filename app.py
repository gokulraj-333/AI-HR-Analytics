from flask import Flask, render_template, request, jsonify

from sql_generator import generate_sql
from sql_executor import run_query
from insight_generator import generate_insight
from utils import clean_sql

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()
    question = data.get("question", "").strip()

    if question == "":
        return jsonify({
            "success": False,
            "error": "Please enter a question."
        })

    try:

        sql = clean_sql(generate_sql(question))

        columns, rows = run_query(sql)

        insight = generate_insight(
            question,
            sql,
            columns,
            rows
        )

        return jsonify({
            "success": True,
            "sql": sql,
            "columns": columns,
            "rows": rows,
            "insight": insight
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        })


@app.route("/kpis")
def kpis():

    total = run_query(
        "SELECT COUNT(*) FROM Employees"
    )[1][0][0]

    active = run_query(
        "SELECT COUNT(*) FROM Employees WHERE Attrition='No'"
    )[1][0][0]

    left = run_query(
        "SELECT COUNT(*) FROM Employees WHERE Attrition='Yes'"
    )[1][0][0]

    attrition = run_query(
        """
        SELECT ROUND(
        (SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) * 100.0)
        / COUNT(*),2)
        FROM Employees
        """
    )[1][0][0]

    salary = run_query(
        """
        SELECT ROUND(AVG(MonthlyIncome),2)
        FROM Employees
        """
    )[1][0][0]

    performance = run_query(
        """
        SELECT ROUND(AVG(PerformanceRating),2)
        FROM Employees
        """
    )[1][0][0]

    satisfaction = run_query(
        """
        SELECT ROUND(AVG(JobSatisfaction),2)
        FROM Employees
        """
    )[1][0][0]

    years = run_query(
        """
        SELECT ROUND(AVG(YearsAtCompany),1)
        FROM Employees
        """
    )[1][0][0]

    return jsonify({

        "total": total,

        "active": active,

        "left": left,

        "attrition": attrition,

        "salary": salary,

        "performance": performance,

        "satisfaction": satisfaction,

        "years": years

    })


if __name__ == "__main__":
    app.run(debug=True)