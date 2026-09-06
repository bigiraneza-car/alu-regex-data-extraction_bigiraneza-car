"""
 =================== Data extraction, validation, and security =========
"""
In short this program is supposed to:
  1. read one big file of raw text.
  2. In my case it looks and extracts for four kinds of information, being: 
      - Email address
      - Phone number
      - Time in 24-hour format
      - Credit card numbers
  3. It takes the found information as not trustworthy, and it only validate information falling in determined format.
  4. Afterward, It secured sensitive information such as credit car number and emails by masking their output.
  5. Lastly, it prints the results/output in another file and format. From python to json.

================= HOW TO RUN THE CODE ====================

  1. Get the code onto your machine

```bash
git clone https://github.com/bigiraneza-car/alu-regex-data-extraction_bigiraneza-car.git
```

  2. Go into the project folder

```bash
cd alu-regex-data-extraction_bigiraneza-car
```

  3. Check Python is installed (3.8 or newer)

```bash
python3 --version
```
On Windows it may be `python --version` instead.

  4. Run the program

```bash
python3 src/main.py
```


  5. Open the full results

```bash
cat output/sample-output.json
```
