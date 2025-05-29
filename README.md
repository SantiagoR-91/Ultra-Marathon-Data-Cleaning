# Ultra-Marathon-Data-Cleaning
 Practice project for data cleaning using Python and pandas
# 🏃‍♂️ Ultramarathon Data Cleaning Project

This project is a hands-on data cleaning exercise using a global ultramarathon race results dataset, consisting of over **7 million records**. The focus is on preparing real-world, unstructured data for analysis using **Python** and **pandas**.

> 📌 Inspired by the [Ryan & Matt Data Science](https://youtu.be/4sZFkPw87ng?si=Pkm2K48GMqrqhsHt) YouTube tutorial  
> Adapted, extended, and customized for personal learning and portfolio development.

---

## 🔧 Tools & Technologies

- Python 3.x  
- pandas  
- seaborn (optional for visualization)  
- Jupyter Notebook or PyCharm  
- CSV input/output

---

## 🧹 Key Cleaning Tasks

- ✅ Filtered for **50km and 50mi races** held in the **USA in 2020**
- ✅ Extracted country names embedded in event titles using string parsing
- ✅ Engineered a new column for **athlete age**
- ✅ Cleaned performance time strings and handled missing values
- ✅ Dropped redundant columns and standardized column names
- ✅ Converted data types for numerical fields
- ✅ Exported a clean, analysis-ready CSV file for further BI/visualization

---

## 📁 File Structure

| File                          | Description                                      |
|------------------------------|--------------------------------------------------|
| `clean_ultramarathon_data.py`| Python script for cleaning the raw dataset       |
| `cleaned_ultra_races_USA_2020.csv` | Output CSV with cleaned and filtered data (optional) |
| `README.md`                  | This project overview                            |

---

## 📊 Sample Output

```bash
Columns: race name, race length, race date, athlete performance, athlete gender, athlete age, total finishers, etc.
Filtered rows: 50km and 50mi USA races in 2020 only
