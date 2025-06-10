# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## 🛠️ ขั้นตอนการติดตั้งและใช้งานโปรเจกต์

### 1️⃣ ติดตั้ง `uv` (ถ้ายังไม่เคยติดตั้ง)

`uv` คือเครื่องมือที่ใช้แทน `pip` และ `virtualenv` เพื่อจัดการ dependencies อย่างรวดเร็ว

##### 🪟 Windows 
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

##### 🍎 macOS/ 🐧 Linux
```bash
curl -sSfL https://astral.sh/uv/install.sh | sh
```
### 2️⃣ สร้าง virtual environment และติดตั้ง dependencies

ให้เปิด Terminal หรือ Command Prompt แล้วทำตามขั้นตอนด้านล่างตามระบบปฏิบัติการ


##### 🪟 Windows 
```bash
# สร้าง virtual environment
uv venv

# เช้าใช้งาน virtual environment
.venv\Scripts\activate

# ติดตั้ง dependencies
uv pip install -r pyproject.toml
```

##### 🍎 macOS/ 🐧 Linux
```bash
# สร้าง virtual environment
uv venv

# เช้าใช้งาน virtual environment
source .venv/bin/activate

# ติดตั้ง dependencies
uv pip install -r pyproject.toml
```

### 3️⃣ เริ่มใช้งานโปรเจกต์
กำหนด config.ymal โดยการ copy ไฟล์ `config.example.yaml` วางไว้ใน Folder 🗂️ `config/` แล้วเปลี่ยนชื่อเป็น `config.yaml` 

### คำอธิบาย: โครงสร้างโปรเจกต์

```
{{ cookiecutter.repo_name }}
├── .gitignore                 # ไฟล์กำหนดสิ่งที่ไม่ต้องการให้ติด version control เช่น .venv, __pycache__
├── config/
│   └── config.yaml            # ไฟล์ตั้งค่าต่าง ๆ ของโปรเจกต์ เช่น path ข้อมูล, พารามิเตอร์ของโมเดล
├── data/
│   ├── external/              # ข้อมูลจากแหล่งภายนอก เช่น open data, API, CSV จากภายนอก
│   ├── interim/               # ข้อมูลระหว่างกระบวนการแปลง เช่น cleaned แต่ยังไม่สมบูรณ์
│   ├── processed/             # ข้อมูลที่พร้อมนำไปใช้ เช่น train/test set หรือ export
│   └── raw/                   # ข้อมูลดิบที่ยังไม่ได้แก้ไขใด ๆ
├── data_loader/
│   ├── __init__.py            # ระบุว่าเป็น package ของ Python
│   └── base.py                # ฟังก์ชันโหลดข้อมูลจาก data/raw, database, หรือ API
├── notebooks/
│   └── 00_exploration.ipynb   # Notebook สำหรับ EDA (Exploratory Data Analysis) และการทดลองเบื้องต้น
├── pyproject.toml             # ไฟล์กำหนด dependencies และ metadata สำหรับ `uv`
├── README.md                  # เอกสารแนะนำการใช้งานโปรเจกต์
└── src/
    ├── __init__.py            # ระบุว่าเป็น package ของ Python
    ├── 01_pre_process.py      # โค้ดสำหรับ pre-processing ข้อมูล เช่น clean, transform, encode
    ├── main.py                # จุดเริ่มต้นหลักของโปรเจกต์ เช่น รวม pipeline หรือรันงานแบบอัตโนมัติ
    └── utils.py               # ฟังก์ชันช่วยเหลือ เช่น logging, config loader, แปลง timestamp ฯลฯ
```
